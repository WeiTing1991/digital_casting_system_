import pyads
from threading import Lock
from typing import Any, Dict, List
from attr import define, field, validators
from itertools import chain


@define
class PLC:
    """Hardware abstraction class for reading and writing variables from and to PLC."""

    netid: str = field(validator=validators.instance_of(str))
    ip: str

    plc_vars_input: List = field(factory=list)
    plc_vars_output: List = field(factory=list)

    connection: Any = field(default=None)
    lock_dict: Lock = field(factory=Lock)
    lock_ads: Lock = field(factory=Lock)

    def __attrs_post_init__(self):
        self.connection = pyads.Connection(self.netid, pyads.PORT_TC3PLC1)

    def close(self):
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
        """load the machine variables from the plc"""
        if not self.plc_vars_input:
            self.plc_vars_input = [vars for vars in plc_vars_input]
        else:
            self.plc_vars_input.extend([vars for vars in plc_vars_input])

    def set_plc_vars_output_list(self, plc_vars_output: List):
        """load the machine variables from the plc"""
        if not self.plc_vars_output:
            self.plc_vars_output = [vars for vars in plc_vars_output]
        else:
            self.plc_vars_output.extend([vars for vars in plc_vars_output])

    def read_variables(self):
        """Reads all structs from PLC and stores inside class."""
        if not self.connect():
            raise AdsConnectionError(
                "Could not read variable from PLC, PLC connection failed."
            )
        with self.lock_ads:
            raise NotImplementedError

    def write_variables(self):
        """Writes all variables that have been set."""
        if not self.connect():
            raise AdsConnectionError(
                "Could not read variable from PLC, PLC connection failed."
            )
        with self.lock_ads:
            raise NotImplementedError

    def check_variables_active(self):
        raise NotImplementedError

    def get_variable(self, variable_name: str) -> Any:
        """Get a variable from the PLC."""
        with self.lock_dict:
            for data in chain(self.plc_vars_output, self.plc_vars_input):
                if data.active != "false" and variable_name == str(data.var_name_IN):
                    try:
                        value = self.connection.read_by_name(data.var_name_IN)
                        print(f"Variable {variable_name}:{value} read from plc.")
                        return value
                    except KeyError:
                        error_msg = f"Error{variable_name}, Error number: {data.id}"
                        raise VariableNotFoundInRepositoryError(error_msg)

    def set_variable(self, variable_name: str, value: Any) -> Any:
        """Get a variable from the PLC."""
        with self.lock_dict:
            for data in self.plc_vars_input:
                if data.active != "false" and variable_name == str(data.var_name):
                    try:
                        value = self.connection.write_by_name(data.var_name_IN, value)
                        print(f"Variable {variable_name}:{value} write to plc.")
                        return value
                    except KeyError:
                        error_msg = f"Error{variable_name}, Error number: {data.id}"
                        raise VariableNotFoundInRepositoryError(error_msg)


class LocalRepositoryEmptyError(Exception):
    pass


class VariableNotFoundInRepositoryError(Exception):
    pass


class AdsConnectionError(Exception):
    pass
