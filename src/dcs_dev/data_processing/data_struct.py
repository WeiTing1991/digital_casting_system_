from dataclasses import dataclass, asdict
from typing import List


# Serialization/Deserialization


@dataclass
class DataObject:
    """
    This moudle is the base data strcture to define the machine and its variables.

    var_id (str): variavle Id
    var_name (str)L variable name
    var_name_IN (str) variable name from plc, followed by plc naming
    is_write_value (bool): if the variable can be write to PLC
    is_read_value (bool): if the variable can be read form PLC
    data_type (str): data type in PLC, followed by C/C++ type
    active (bool): if the varible is active and can be read and/or write.

    """

    var_id: int
    var_name: str
    var_name_IN: str
    data_type: str
    active: bool


@dataclass
class DataDict:
    """
    This moudle is a data dictionary, which  wraps from DataObject with a machine id and params list.

    """

    machine_id: int
    machine_input: List[DataObject]
    machine_output: List[DataObject]

    def __str__(self) -> str:
        return f"machine id: {self.machine_id} \
        \nmachine input: {self.machine_input} \
        \nmachine output: {self.machine_output}"


@dataclass
class MachineDataStruct:
    """
    This moudle is data structure, representing the machine.

    """

    machine_name: str
    machine_data: DataDict

    def _to_dict(self) -> dict:
        return asdict(self)

    def __str__(self) -> str:
        return f"machine name {self.machine_name} \nmachine data: {self.machine_data}"
