from data_struct import DataObject, DataDict, MachineDataStruct
from data_processing import PathConfig

if __name__ == "__main__":

    path = PathConfig()
    print(path.__str__())

    path._set_plc_config()
    path._load_form_json()

    # print(path.get_machine_dict()["inline_mixer"])

    temp_dict = path.get_machine_dict()["inline_mixer"]

    new_machine = MachineDataStruct(machine_name="", machine_data=DataDict(0, [], []))

    for key, value in temp_dict.items():
        new_machine = MachineDataStruct(machine_name=key, machine_data=value)
        print(new_machine.__str__())

    # DataObject1 = DataObject(
    #     var_id=101,
    #     var_name="mixer_on",
    #     var_name_IN="GVL_ResearchData.b_RED_Laptop_MI1_Run",
    #     data_type="REAL",
    #     active=True,
    # )
    #
    # DataObject2 = DataObject(
    #     var_id=101,
    #     var_name="mixer_on",
    #     var_name_IN="GVL_ResearchData.b_RED_Laptop_MI1_Run",
    #     data_type="REAL",
    #     active=True,
    # )
    #
    # DataObject3 = DataObject(
    #     var_id=101,
    #     var_name="mixer_on",
    #     var_name_IN="GVL_ResearchData.b_RED_Laptop_MI1_Run",
    #     data_type="REAL",
    #     active=True,
    # )
    #
    # DataObject_i = [DataObject1, DataObject2, DataObject3]
    # DataObject_o = [DataObject1, DataObject2, DataObject3]
    # DataDict1 = DataDict(101, DataObject_i, DataObject_o)
    #
    # print(str(DataDict1))
    # print("\n")
    #
    # inline_mixer = MachineDataStruct(
    #     machine_name="inline_mixer",
    #     machine_data=DataDict(machine_id=101, machine_params=DataObject_a),
    # )
    #
    # print((inline_mixer._to_dict()))
    # print("\n")
    #
    # print((inline_mixer.__dict__))
