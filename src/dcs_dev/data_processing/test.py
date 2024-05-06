from data_processing import DataHandler

if __name__ == "__main__":

    path = DataHandler()
    print(path.__str__())

    # set the path to the PLC config file
    path._set_plc_config()
    data = path._load_json_to_instance()

    print(path.machine["inline_mixer"])
    print(path.machine["inline_mixer"].machine_id)
    print(path.machine["inline_mixer"].machine_input)
    print(path.machine["inline_mixer"].machine_output)

    print(type(path.machine))
