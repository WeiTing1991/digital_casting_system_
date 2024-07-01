import os
import pyads
from datetime import datetime
import time

from threading import Thread
from utilities.data_processing import DataProcessing
from data_processing.data_processing import DataHandler, DataGathering
from hal.device import InlineMixer
from hal.plc import PLC

# =================================================================================
"""Global value"""

CLIENT_ID = '5.57.158.168.1.1'                          # PLC AMSNETID

NOW_DATE = datetime.now().date().strftime("%Y%m%d")     # Date

# File name
DEFAULT_FILENAME = NOW_DATE + '_' + '50_agg_74S_3FW__ETH_acc_test'
# 50_agg_1.5FW_ETH_temperature_test

HERE = os.path.dirname(__file__)
HOME = os.path.abspath(os.path.join(HERE, "../../"))
DATA = os.path.abspath(os.path.join(HOME, "data"))

JSON_DIR = os.path.join(DATA, 'json')
CSV_DIR = os.path.join(DATA, 'csv')

# Value for Dry Run without inline mixer
REAL_PLC = True
DRY_RUN = True
# Record time slot
RECODED_DELAY_TIME = 1
LOOP_TIME = 10


# ===============================================================================
"""Global value for research data from PLC script"""
# ------------------------------------------------------------------------------#

machine_data = DataHandler()
machine_data._set_robot_mode_config()
machine_data._load_json_to_instance()

inline_mixer = InlineMixer(
    machine_data.machine["inline_mixer"].machine_id,
    machine_data.machine["inline_mixer"].machine_input,
    machine_data.machine["inline_mixer"].machine_output,
)

# ------------------------------------------------------------------------------#
# Inline mixer reactor

inline_mixer_params = [ param for param in inline_mixer.set_output_dict() ]


# Accelerator pump
plc_output = "P_Robot_Operate.fb_getOutputData"
plc_input = "P_Robot_Operate.fb_SetOutputDataToIO"



# Superplasticizer pump
# NONE


# ------------------------------------------------------------------------------#
# Concrete pump

cc_pump_Forward_On = plc_input + "GVL_ROB.b_RED_Concrete_Pump_Forward_On"
cc_pump_Backward_On = "GVL_ROB.b_RED_Concrete_Pump_Backward_On"
cc_pump_flowrate = "GVL_ROB.f_RED_Concrete_Pump_Flowrate"

cc_pump_params = dict(
    cp_flowrate = plc_input + "." + "n_CP1_Operate_Flowrate",
    cp_pressure = plc_output + "." + "f_CP1_status_pressure_Concrete_pump",
    cp_temperature_fresh = plc_output + "." + "f_CP1_status_temperature_concrete_fresh",
    cp_temperature = plc_output + "." +  "f_CP1_status_temperature_Concrete_pump"
)


def read_from_plc_and_store(data:dict, key:str, value):
    """
    """
    if key != 'Time':
        r_value_plc = plc.get_variable(value)
        data[key] = r_value_plc
    else:
        data[key] = value
        print(f"{key}:{value}")


if __name__ == "__main__" :

    if REAL_PLC:
        plc = PLC(netid=CLIENT_ID, ip="")
        plc.connect()

        if not DRY_RUN:

            counter = 0
            param_mixer_is_run = inline_mixer_params[0]
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
                    recording_data["Time"] = str(NOW_TIME)

                    for params in inline_mixer_params:
                        for key, value in params.items():
                            thread_1 = Thread(target=read_from_plc_and_store, args=(recording_data, log, key, value))
                            thread_1.start()

                # Delay time to reduce real time data
                time.sleep(RECODED_DELAY_TIME)

                # Write dictionary to JSON file
                data_recorder.write_dict_to_json(recording_data)

                if not mixer_is_run:
                    print("Mixer is not running")
                    break

            # Write dictionary to CSV file
            # Flip the data
            recording_data_no_log = []
            for k in recording_data.keys():
                # add log in to column
                recording_data[k]["Log"] = k
                recording_data_no_log.append(recording_data[k])

            header = list(recording_data[1].keys())
            header.reverse()

            # To CSV file
            data_recorder.write_dict_to_csv(recording_data_no_log, header)

        else:
            pass

    else:
        print("Offline mode")
