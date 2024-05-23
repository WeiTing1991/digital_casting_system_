from data_processing.data_processing import DataHandler
from hal.device import InlineMixer
from hal.plc import PLC


if __name__ == "__main__":
    machine_data = DataHandler()
    print(machine_data.__str__())

    # set the path to the PLC config file
    machine_data._set_plc_config()
    data = machine_data._load_json_to_instance()


    inline_mixer = InlineMixer(
        machine_data.machine["inline_mixer"].machine_id,
        machine_data.machine["inline_mixer"].machine_input,
        machine_data.machine["inline_mixer"].machine_output,
    )

    print(inline_mixer.machine_id)
    print(inline_mixer.input_list())
    print(inline_mixer.output_list())

    plc = PLC(netid="5.57.158.168.1.1", ip="")

    plc.set_plc_vars_input_list(inline_mixer.input_list())

    plc.get_variable("mixer_is_run")

    # plc.connect()

    # print(path.machine["inline_mixer"].machine_output)

    print(type(machine_data.machine))
