from dcs_dev.data_processing.data_processing import DataHandler
from dcs_dev.hal.device import InlineMixer

if __name__ == "__main__":

    machine_data = DataHandler()
    print(machine_data.__str__())

    # set the path to the PLC config file
    # machine_data._set_plc_config()

    machine_data._set_robot_mode_config()
    data = machine_data._load_json_to_instance()

    inline_mixer = InlineMixer(
        machine_data.machine["inline_mixer"].machine_id,
        machine_data.machine["inline_mixer"].machine_input,
        machine_data.machine["inline_mixer"].machine_output,
    )

    print(inline_mixer.device_id())
    print(inline_mixer.parameter_id("mixer_is_run"))

    for input in inline_mixer.get_input_var_name():
        print(input)
    for output in inline_mixer.get_output_var_name():
        print(output)
