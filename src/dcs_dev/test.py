from data_processing.data_processing import DataHandler
from hal.device import InlineMixer

if __name__ == "__main__":

    machine_data = DataHandler()
    print(machine_data.__str__())

    # set the path to the PLC config file
    machine_data._set_plc_config()
    data = machine_data._load_json_to_instance()

    #print(path.machine["inline_mixer"])
    #print(path.machine["inline_mixer"].machine_id)
    #print(path.machine["inline_mixer"].machine_input)

    inline_mixer = InlineMixer(machine_data.machine["inline_mixer"].machine_id, machine_data.machine["inline_mixer"].machine_input, machine_data.machine["inline_mixer"].machine_output)

    print (inline_mixer.machine_id)
    print (inline_mixer.input_list())
    print (inline_mixer.output_list())

    # print(path.machine["inline_mixer"].machine_output)

    print(type(machine_data.machine))
