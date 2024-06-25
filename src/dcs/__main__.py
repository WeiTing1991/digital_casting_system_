import os
import pyads
from datetime import datetime
import time

from threading import Thread

from data_gathering.data_gathering import write_dict_to_csv, write_dict_to_json

# this version only works on the robotic mode
# =================================================================================
'''Global value'''

CLIENT_ID = '5.57.158.168.1.1'                          # PLC AMSNETID

NOW_DATE = datetime.now().date().strftime("%Y%m%d")     # Date

# file name
DEFAULT_FILENAME = NOW_DATE + '_' + '50_agg_74S_3FW__ETH_acc_test'
#50_agg_1.5FW_ETH_temperature_test

# HVAE TO FINISH NOT OVERRkIDE THE FILE
# direction for data storing
HERE = os.path.dirname(__file__)
HOME = os.path.abspath(os.path.join(HERE, "../../"))
DATA = os.path.abspath(os.path.join(HOME, "data"))

JSON_DIR = os.path.join(DATA, 'json')
CSV_DIR = os.path.join(DATA, 'csv')

# Record time slot
RECODED_DELAY_TIME = 1 # second

# Value for Dry Run without concrete pump
DRY_RUN = False
LOOP_TIME = 1000


# ===============================================================================
"""Global value for research data from PLC script"""
# ------------------------------------------------------------------------------#
# Accelerator pump
plc_output = "P_Robot_Operate.fb_getOutputData"
plc_input = "P_Robot_Operate.fb_SetOutputDataToIO"


# ------------------------------------------------------------------------------#
# Accelerator pump

acc_pump_params = dict(
    accHigh_flowrate = plc_input + "." + "n_AP1_Operate_Flowrate",
    accLow_flowrate = plc_input + "." + "n_SP1_Operate_Flowrate"
)

# ------------------------------------------------------------------------------#
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

# ------------------------------------------------------------------------------#
# Inline mixer reactor

mixer_On = plc_output + "." + "b_MI1_Is_Run"
curved_speed_mode = "GVL_ROB.b_RED_Mixer_Curved_Speed_On"

inline_mixer_params = dict(

    mixer_speed_M1 =  plc_output + "." + "n_MI1_status_SpeedM1",
    mixer_speed_M2 =  plc_output + "." + "n_MI1_status_SpeedM2",

    mixer_torque_M1 =  plc_output + "." + "f_Status_Torque_Motor_1",
    mixer_torque_M2 =  plc_output + "." + "f_Status_Torque_Motor_2",

    mixer_motor_temperature_M1 =  plc_output + "." + "f_MI1_status_temperature_motor_1",
    mixer_motor_temperature_M2 =  plc_output + "." + "f_MI1_status_temperature_motor_2",

    mixer_temperature_outlet = plc_output + "." + "f_MI1_status_temperature_funnel_outlet",
    mixer_pressure = plc_output + "." + "f_MI1_status_Pressure_funnel_inlet"

)

# =================================================================================

def read_from_plc_and_store(data:dict, key:str, value):
    """
    """
    if key != 'Time':
        r_value_plc = plc.read_by_name(value)
        # reduce the decimal to 0.0000
        r_value_plc = round(abs(r_value_plc), 3)

        data[key] = r_value_plc
        #print(f"{key}:{r_value_plc}")

    else:
        data[key] = value
        print(f"{key}:{value}")


def read_from_plc_and_store_noDecimal(data:dict, key:str, value):
    """
    """

    if key != 'Time':
        r_value_plc = plc.read_by_name(value)
        # reduce the decimal to 0.0000
        if abs(r_value_plc) < 0.5:
            r_value_plc = 0
        else:
            r_value_plc = round(abs(r_value_plc), 4)

        data[key] = r_value_plc
        #print(f"{key}:{r_value_plc}")

    else:
        data[key] = value
        print(f"{key}:{value}")


if __name__ == "__main__":

    # Connect to plc and open connection
    plc = pyads.Connection(CLIENT_ID, pyads.PORT_TC3PLC1)
    plc.open()

    try:
        plc.read_device_info()
        print(f"Connection.:{plc.is_open}")
        print(f"{plc.read_state}")
        print(f"plc address :{plc.get_local_address()}")

    except EOFError:
        print(f"Connection failed")

    if not DRY_RUN:

        # process start
        counter = 0
        research_data = {}

        # Read the state from PLC
        mixer_On_state = plc.read_by_name(mixer_On)


        while mixer_On_state:

            print (f"mixer:{mixer_On_state}")
            #print (f"cc_pump_Backward_On:{cc_pump_Backward_On_state}")
            #print (f"cc_pump_Forward_On:{cc_pump_Forward_On_state}")

            # Set the log
            counter+=1
            log = counter

            # Update the time
            NOW_TIME = datetime.now().time().strftime("%H:%M:%S.%f")[:-3]

            # intergted to class moudle
            if research_data is not None:
                research_data[log] = {}

                # Store to dictionary
                # Time
                read_from_plc_and_store(research_data[log], 'Time', str(NOW_TIME))

                # Inline mixer
                for k, v in inline_mixer_params.items():
                    Thread1 = Thread(target=read_from_plc_and_store, args=(research_data[log], k, v))
                    Thread1.start()
                    #read_from_plc_and_store(research_data[log], k, v)

                # Concrete pump
                for k, v in cc_pump_params.items():
                    Thread2 = Thread(target=read_from_plc_and_store, args=(research_data[log], k, v))
                    Thread2.start()
                    #read_from_plc_and_store(research_data[log], k, v)

                # Accelerator pump
                for k, v in acc_pump_params.items():
                    Thread3 = Thread(target=read_from_plc_and_store, args=(research_data[log], k, v))
                    Thread3.start()
                    #read_from_plc_and_store(research_data[log], k, v)

                # Superplastizer pump

            time.sleep(RECODED_DELAY_TIME)
            # DATA is the folder path from setup

            # Write dictionary to JSON file
            write_dict_to_json(os.path.join(JSON_DIR, DEFAULT_FILENAME) + ".json" , research_data)


            # MAKE SURE WHICH PART YOU WANT STOP
            mixer_On_state = plc.read_by_name(mixer_On)

            if not mixer_On_state:
                print (f"mixer:{mixer_On_state}")
                break

        # Write dictionary to CSV file
        # Flip the data
        research_data_without_log = []
        for k in research_data.keys():
            # add log in to column
            research_data[k]["Log"] = k
            research_data_without_log.append(research_data[k])

        header = list(research_data[1].keys())
        header.reverse()

        # To CSV file
        write_dict_to_csv(os.path.join(CSV_DIR,DEFAULT_FILENAME) + ".csv" , research_data_without_log, header)

    # DRY RUN
    else:

        #process start
        counter = 0
        research_data = {}

        while counter < LOOP_TIME:
            counter+=1
            log = counter

            # update the time
            NOW_TIME = datetime.now().time().strftime("%H:%M:%S")

            # test the write value
            var_handle = plc.get_handle(mixer_On)

            # intergted TODO
            if research_data is not None:
                research_data[log] = {}

                # Store to dictionary
                # Time
                read_from_plc_and_store(research_data[log], 'Time', NOW_TIME)

                # Inline mixer
                for k, v in inline_mixer_params.items():
                    read_from_plc_and_store(research_data[log], k, v)
                # Concrete pump
                for k, v in cc_pump_params.items():
                    read_from_plc_and_store(research_data[log], k, v)

                # Write dictionary to JSON file
                write_dict_to_json(os.path.join(JSON_DIR, DEFAULT_FILENAME) + ".json" , research_data)

            time.sleep(RECODED_DELAY_TIME)


        # Write dictionary to CSV file
        # Flip the data
        research_data_without_log = []
        for k in research_data.keys():
            # add log in to column
            research_data[k]["Log"] = k
            research_data_without_log.append(research_data[k])

        header = list(research_data[1].keys())
        header.reverse()

        # To CSV file
        write_dict_to_csv(os.path.join(CSV_DIR,DEFAULT_FILENAME) + ".csv" , research_data_without_log, header)


    # Close the conection
    print('Closing the Connections..')
    plc.close()
    print(f"Conected.:{plc.is_open}")
    print("Discontected")
