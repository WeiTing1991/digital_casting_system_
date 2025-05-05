import os
import pyads
from datetime import datetime
import time

from threading import Thread
from utilities.data_processing import DataProcessing
from data_processing.data_processing import DataHandler, DataGathering
from hal.device import *
from hal.plc import PLC

# =================================================================================
"""Global value"""

CLIENT_ID = '5.57.158.168.1.1'                          # PLC AMSNETID

NOW_DATE = datetime.now().date().strftime("%Y%m%d")     # Date

# File name
DEFAULT_FILENAME = NOW_DATE + '_' + 'HIF_test'
# 50_agg_1.5FW_ETH_temperature_test

HERE = os.path.dirname(__file__)
HOME = os.path.abspath(os.path.join(HERE, "../../"))
DATA = os.path.abspath(os.path.join(HOME, "data"))

JSON_DIR = os.path.join(DATA, 'json')
CSV_DIR = os.path.join(DATA, 'csv')

# Value for Dry Run without inline mixer
REAL_PLC = True
DRY_RUN = False
# Record time slot
RECODED_DELAY_TIME = 1
LOOP_TIME = 10


# ===============================================================================
"""Global value for research data from PLC script"""
# ------------------------------------------------------------------------------#

machine_data = DataHandler()
machine_data._set_robot_mode_config()
machine_data._load_json_to_instance()


# ------------------------------------------------------------------------------#
# Inline mixer reactor
inline_mixer = InlineMixer(
    machine_data.machine["inline_mixer"].machine_id,
    machine_data.machine["inline_mixer"].machine_input,
    machine_data.machine["inline_mixer"].machine_output,
)
inline_mixer_params_output = [ param for param in inline_mixer.set_output_dict() ]

# ------------------------------------------------------------------------------#
# Concrete pump
concrete_pump = ConcretePump(
    machine_data.machine["concrete_pump"].machine_id,
    machine_data.machine["concrete_pump"].machine_input,
    machine_data.machine["concrete_pump"].machine_output,
)
concrete_pump_params_output = [ param for param in concrete_pump.set_output_dict() ]

# ------------------------------------------------------------------------------#
# Accelerator pump

accelerator_pump = DosingPumpHigh(
    machine_data.machine["dosing_pump_high"].machine_id,
    machine_data.machine["dosing_pump_high"].machine_input,
    machine_data.machine["dosing_pump_high"].machine_output,
)
accelerator_pump_params_output = [ param for param in accelerator_pump.set_output_dict() ]

# ------------------------------------------------------------------------------#
# Superplasticizer pump
xseed_superplasticizer_pump = DosingPumpLow(
    machine_data.machine["dosing_pump_low"].machine_id,
    machine_data.machine["dosing_pump_low"].machine_input,
    machine_data.machine["dosing_pump_low"].machine_output,
)

xseed_superplasticizer_pump_params_output = [ param for param in xseed_superplasticizer_pump.set_output_dict() ]


#TODO: Move to PLC class and refactor
def read_from_plc_and_store(data:dict, key:str, value):
    r_value_plc = plc.get_variable(value)
    if "temperature" in value or "pressure" in value:
        r_value_plc /= 10
    elif type(r_value_plc) is float:
        print(type(r_value_plc) )
        r_value_plc = round(r_value_plc, 2)
    data[key] = r_value_plc

if __name__ == "__main__" :

    if REAL_PLC:
        plc = PLC(netid=CLIENT_ID, ip="")
        plc.connect()

        # initialize the plc variables for the machine
        plc.set_plc_vars_input_list(inline_mixer.input_list())
        plc.set_plc_vars_output_list(inline_mixer.output_list())

        plc.set_plc_vars_input_list(concrete_pump.input_list())
        plc.set_plc_vars_output_list(concrete_pump.output_list())

        plc.set_plc_vars_input_list(accelerator_pump.input_list())
        plc.set_plc_vars_output_list(accelerator_pump.output_list())

        plc.set_plc_vars_input_list(xseed_superplasticizer_pump.input_list())
        plc.set_plc_vars_output_list(xseed_superplasticizer_pump.output_list())

        if not DRY_RUN:

            counter = 0
            param_mixer_is_run = inline_mixer_params_output[0]

            print(param_mixer_is_run)
            mixer_is_run = plc.get_variable(param_mixer_is_run["mixer_is_run"][0])

            recording_data = {}

            # process start
            while mixer_is_run:

                # Set the log
                counter+=1
                log = counter

                # Update the time
                NOW_TIME = datetime.now().time().strftime("%H:%M:%S.%f")[:-3]

                data_recorder = DataGathering(DEFAULT_FILENAME)

                if recording_data is not None:
                    recording_data[log] = {}
                    recording_data[log]["Time"] = NOW_TIME

                    for params in inline_mixer_params_output:
                        for key, value in params.items():
                            thread_1 = Thread(target=read_from_plc_and_store, args=(recording_data[log], key, value[0]))
                            thread_1.start()
                    for params in concrete_pump_params_output:
                        for key, value in params.items():
                            thread_2 = Thread(target=read_from_plc_and_store, args=(recording_data[log], key, value[0]))
                            thread_2.start()
                    for params in accelerator_pump_params_output:
                        for key, value in params.items():
                            thread_3 = Thread(target=read_from_plc_and_store, args=(recording_data[log], key, value[0]))
                            thread_3.start()
                    for params in xseed_superplasticizer_pump_params_output:
                        for key, value in params.items():
                            thread_4 = Thread(target=read_from_plc_and_store, args=(recording_data[log], key, value[0]))
                            thread_4.start()


                # Delay time to reduce real time data
                time.sleep(RECODED_DELAY_TIME)

                # Write dictionary to JSON file
                data_recorder.write_dict_to_json(recording_data)

                # Update the mixer status
                mixer_is_run = plc.get_variable(param_mixer_is_run["mixer_is_run"][0])

                if not mixer_is_run:
                    print("Stop recording data")
                    plc.close()
                    break

            print("Mixer is not running")

            # Write dictionary to CSV file
            recording_data_no_log = []
            for k in recording_data.keys():
                # add log in to column
                recording_data[k]["Log"] = k
                recording_data_no_log.append(recording_data[k])

            header = list(recording_data[1].keys())
            header.reverse()

            # save to CSV file
            data_recorder.write_dict_to_csv(recording_data_no_log, header)

        else:
            pass

    else:
        print("Offline mode")
