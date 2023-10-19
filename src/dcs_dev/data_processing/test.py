from data_struct import DataObject, DataDict, MachineDataStruct
from data_processing import PathConfig



if __name__ == "__main__":
    path = PathConfig()
    print(path)


    DataObject1 = DataObject(var_id=101,
                             var_name="mixer_on",
                             var_name_IN = "GVL_ResearchData.b_RED_Laptop_MI1_Run",
                             data_type= "REAL",
                             is_write_value=True,
                             is_read_value=True,
                             active=True)


    DataObject2 = DataObject(var_id=101,
                             var_name="mixer_on",
                             var_name_IN = "GVL_ResearchData.b_RED_Laptop_MI1_Run",
                             data_type= "REAL",
                             is_write_value=True,
                             is_read_value=True,
                             active=True)

    DataObject3 = DataObject(var_id=101,
                             var_name="mixer_on",
                             var_name_IN = "GVL_ResearchData.b_RED_Laptop_MI1_Run",
                             data_type= "REAL",
                             is_write_value=True,
                             is_read_value=True,
                             active=True)

    DataObject_a = [DataObject1, DataObject2, DataObject3]
    DataDict1 =DataDict(101, DataObject_a)
    print(str(DataDict1))
    print("\n")

    inline_mixer = MachineDataStruct(machine_name ="inline_mixer", machine_data = DataDict(machine_id=101, machine_params=DataObject_a))

    print((inline_mixer._to_dict()))
    print("\n")

    print((inline_mixer.__dict__))
