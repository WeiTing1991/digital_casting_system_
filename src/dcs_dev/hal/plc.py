import pyads
from threading import Lock
from typing import Any, Dict, List
from attr import define, field, validators


@define
class PLC:
    """Hardware abstraction class for reading and writing variables from and to PLC."""

    netid: str = field(validator=validators.instance_of(str))
    ip: str

    plc_vars_input:List = field(factory=list)
    plc_vars_output:List = field(factory=list)

    connection: Any = field(default=None)
    lock_dict: Lock = field(factory=Lock)
    lock_ads: Lock = field(factory=Lock)

    def __attrs_post_init__(self):
        self.connection = pyads.Connection(self.netid, pyads.PORT_TC3PLC1)

    def __del__(self):
        # NOT GOOD
        """Close the connection to the PLC."""
        if self.connection.is_open:
            self.connection.close()
        print("PLC connection closed")

    def connect(self) -> bool:
        """Connect to the PLC."""
        with self.lock_ads:
            if not self.connection.is_open:
                self.connection.open()
            try:
                self.connection.read_device_info()
            except pyads.ADSError as e:
                print(f"Error: {e}")
                return False
            else:
                print(f"Connection: {self.connection.is_open}")
                return True
    def set_plc_vars_input_list(self, plc_vars_input: List):
        """ load the machine variables from the plc """
        self.plc_vars_input = [vars for vars in plc_vars_input]

    def set_plc_vars_output_list(self, plc_vars_output: List):
        """ load the machine variables from the plc """
        self.plc_vars_output = [vars for vars in plc_vars_output]

    def read_variables(self):
        """Reads all structs from PLC and stores inside class."""
        if not self.connect():
            raise AdsConnectionError("Could not read variable from PLC, PLC connection failed.")
        with self.lock_ads:
            pass

    def write_variables(self):
        """Writes all variables that have been set."""
        if not self.connect():
            raise AdsConnectionError("Could not read variable from PLC, PLC connection failed.")
        pass

    def get_variable(self, variable_name: str):
        """Get a variable from the PLC."""
        with self.lock_dict:
            for data in self.plc_vars_output:
                if variable_name == str(data.var_name):
                    try:
                        value = self.connection.read_by_name(data.var_name_IN)
                        print(f"Variable {variable_name}:{value} read from plc.")
                        return {variable_name : value}
                    except KeyError:
                        error_msg = f"Error{variable_name}"
                        raise VariableNotFoundInRepositoryError(error_msg)


    def set_variable(self, variable_name: str, value: Any):
        """Get a variable from the PLC."""
        raise NotImplementedError


class LocalRepositoryEmptyError(Exception):
    pass

class VariableNotFoundInRepositoryError(Exception):
    pass

class AdsConnectionError(Exception):
    pass
