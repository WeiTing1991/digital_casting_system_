from data_processing.data_processing import DataHandler
from hal.device import InlineMixer
from hal.plc import PLC
import time
from gui.app import DCSApp

if __name__ == "__main__":
    machine_data = DataHandler()

    # set the path to the PLC config file
    # machine_data._set_plc_config()
    machine_data._set_robot_mode_config()
    machine_data._load_json_to_instance()

    inline_mixer = InlineMixer(
        machine_data.machine["inline_mixer"].machine_id,
        machine_data.machine["inline_mixer"].machine_input,
        machine_data.machine["inline_mixer"].machine_output,
    )

    inline_mixer_params_output = [ param for param in inline_mixer.set_output_dict() ]

    # for input in inline_mixer.get_input_var_name():
    #     print(input)
    # for output in inline_mixer.get_output_var_name():
    #     print(output)

    # inline_mixer.get_output_var_name()j
    # for input in inline_mixer.set_input_dict():
    #     print(input)

    app = DCSApp()
    while True:
        plc = PLC(netid="5.57.158.168.1.1", ip="")
        plc.connect()
        plc.set_plc_vars_output_list(inline_mixer.output_list())

        time.sleep(2)

        for params in inline_mixer_params_output:
            for key, value in params.items():
                r_value_plc = plc.get_variable(value[0])
                print(r_value_plc)

"""

Variable GVL_ROB.ob_MI1_is_run:False read from plc.
False
Variable GVL_ROB.ob_MI1_is_ready:True read from plc.
True
Variable GVL_ROB.on_MI1_status_speed_motor_1:0 read from plc.
0
Variable GVL_ROB.on_MI1_status_speed_motor_2:0 read from plc.
0
Variable GVL_ROB.on_MI1_status_torque_motor_1:0.6796800494194031 read from plc.
0.6796800494194031
Variable GVL_ROB.on_MI1_status_torque_motor_2:0.33984002470970154 read from plc.
0.33984002470970154
Variable GVL_ROB.on_MI1_status_temperature_funnel_outlet:282.0 read from plc.
282.0
Variable GVL_ROB.on_MI1_status_pressure_funnel_inlet:0.0 read from plc.
0.0
Variable GVL_ROB.on_MI1_status_temperature_motor_1:245.0 read from plc.
245.0
Variable GVL_ROB.on_MI1_status_temperature_motor_2:270.0 read from plc.
270.0
Connection: True
"""

    # tk.Button(window, text="Hello World", command=window.quit).pack()
    # window.mainloop()



'''
Variable GVL_ROB.ob_MI1_is_run:False read from plc.
Variable GVL_ROB.ob_MI1_is_ready:True read from plc.
Variable GVL_ROB.on_MI1_status_speed_motor_1:0 read from plc.
Variable GVL_ROB.on_MI1_status_speed_motor_2:0 read from plc.
Variable GVL_ROB.on_MI1_status_torque_motor_1:0.49088001251220703 read from plc.
Variable GVL_ROB.on_MI1_status_torque_motor_2:0.3020800054073334 read from plc.
Variable GVL_ROB.on_MI1_status_temperature_funnel_outlet:278.0 read from plc.
Variable GVL_ROB.on_MI1_status_pressure_funnel_inlet:0.0 read from plc.
Variable GVL_ROB.on_MI1_status_temperature_motor_1:254.0 read from plc.
Variable GVL_ROB.on_MI1_status_temperature_motor_2:270.0 read from plc.'''
