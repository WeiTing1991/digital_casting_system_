# device.py
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Any, Dict


class Machine(ABC):

    @abstractmethod
    def device_id(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def parameter_id(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def input_list(self) -> List:
        raise NotImplementedError

    @abstractmethod
    def output_list(self) -> List:
        raise NotImplementedError

    @abstractmethod
    def get_input_var_name(self) -> Any:
        raise NotImplementedError

    @abstractmethod
    def get_output_var_name(self) -> Any:
        raise NotImplementedError

    @abstractmethod
    def set_input_dict(self):
        raise NotImplementedError

    @abstractmethod
    def set_output_dict(self):
        raise NotImplementedError


@dataclass
class InlineMixer(Machine):
    """
    InlineMixer is a class that represents the Inline Mixer machine.

    """
    machine_id: int
    machine_input: List
    machine_output: List
    machine_error_num: int = 0

    def device_id(self) -> int:
        return self.machine_id

    def parameter_id(self, param_name:str) -> int:
        for params in [self.machine_input, self.machine_output]:
            for param in params:
                if param_name == param.var_name:
                    return param.id if param.id is not None else 0

    def input_list(self) -> List[object]:
        return self.machine_input

    def output_list(self) -> List[object]:
        return self.machine_output

    def get_input_var_name(self) -> Any:
        for input in self.machine_input:
            yield input.var_name

    def get_output_var_name(self) -> Any:
        for output in self.machine_output:
            yield output.var_name

    def set_input_dict(self):
        for input in self.machine_input:
            if input.active:
                yield {input.var_name : [input.var_name_IN, "pyads."+ input.data_type, 1]}

    def set_output_dict(self):
        for output in self.machine_output:
            if output.active:
                yield {output.var_name : [output.var_name_IN, "pyads."+ output.data_type, 1]}

    def __str__(self) -> str:
        return f"Machine ID: {self.machine_id}, Machine Input: {self.input_list}, Machine Output: {self.output_list}"


@dataclass
class ConcretePump(Machine):
    """
    ConcretePump is a class that represents the Concrete Pump machine.

    """
    machine_id: int
    machine_input: List
    machine_output: List
    machine_error_num: int = 0

    def device_id(self) -> int:
        return self.machine_id

    def parameter_id(self, param_name:str) -> int:
        for params in [self.machine_input, self.machine_output]:
            for param in params:
                if param_name == param.var_name:
                    return param.id if param.id is not None else 0

    def input_list(self) -> List[object]:
        return self.machine_input

    def output_list(self) -> List[object]:
        return self.machine_output

    def get_input_var_name(self) -> Any:
        for input in self.machine_input:
            yield input.var_name

    def get_output_var_name(self) -> Any:
        for output in self.machine_output:
            yield output.var_name

    def set_input_dict(self):
        for input in self.machine_input:
            if input.active:
                yield {input.var_name : [input.var_name_IN, "pyads."+ input.data_type, 1]}

    def set_output_dict(self):
        for output in self.machine_output:
            if output.active:
                yield {output.var_name : [output.var_name_IN, "pyads."+ output.data_type, 1]}

    def __str__(self) -> str:
        return f"Machine ID: {self.machine_id}, Machine Input: {self.input_list}, Machine Output: {self.output_list}"



@dataclass
class DosingPumpHigh(Machine):
    """
    DosingPumpHigh is a class that represents the Dosing pump machine with high dosing.

    """
    machine_id: int
    machine_input: List
    machine_output: List
    machine_error_num: int = 0

    def device_id(self) -> int:
        return self.machine_id

    def parameter_id(self, param_name:str) -> int:
        for params in [self.machine_input, self.machine_output]:
            for param in params:
                if param_name == param.var_name:
                    return param.id if param.id is not None else 0

    def input_list(self) -> List[object]:
        return self.machine_input

    def output_list(self) -> List[object]:
        return self.machine_output

    def get_input_var_name(self) -> Any:
        for input in self.machine_input:
            yield input.var_name

    def get_output_var_name(self) -> Any:
        for output in self.machine_output:
            yield output.var_name

    def set_input_dict(self):
        for input in self.machine_input:
            if input.active:
                yield {input.var_name : [input.var_name_IN, "pyads."+ input.data_type, 1]}

    def set_output_dict(self):
        for output in self.machine_output:
            if output.active:
                yield {output.var_name : [output.var_name_IN, "pyads."+ output.data_type, 1]}

    def __str__(self) -> str:
        return f"Machine ID: {self.machine_id}, Machine Input: {self.input_list}, Machine Output: {self.output_list}"


@dataclass
class DosingPumpLow(Machine):
    """
    DosingPumpLow is a class that represents the Dosing pump machine with low dosing.

    """
    machine_id: int
    machine_input: List
    machine_output: List
    machine_error_num: int = 0

    def device_id(self) -> int:
        return self.machine_id

    def parameter_id(self, param_name:str) -> int:
        for params in [self.machine_input, self.machine_output]:
            for param in params:
                if param_name == param.var_name:
                    return param.id if param.id is not None else 0

    def input_list(self) -> List[object]:
        return self.machine_input

    def output_list(self) -> List[object]:
        return self.machine_output

    def get_input_var_name(self) -> Any:
        for input in self.machine_input:
            yield input.var_name

    def get_output_var_name(self) -> Any:
        for output in self.machine_output:
            yield output.var_name

    def set_input_dict(self):
        for input in self.machine_input:
            if input.active:
                yield {input.var_name : [input.var_name_IN, "pyads."+ input.data_type, 1]}

    def set_output_dict(self):
        for output in self.machine_output:
            if output.active:
                yield {output.var_name : [output.var_name_IN, "pyads."+ output.data_type, 1]}

    def __str__(self) -> str:
        return f"Machine ID: {self.machine_id}, Machine Input: {self.input_list}, Machine Output: {self.output_list}"


@dataclass
class Controller(Machine):
    """
    Controller is a class that represents the parameters in controller.

    """
    machine_id: int
    machine_input: List
    machine_output: List
    machine_error_num: int = 0

    def device_id(self) -> int:
        return self.machine_id

    def parameter_id(self, param_name:str) -> int:
        for params in [self.machine_input, self.machine_output]:
            for param in params:
                if param_name == param.var_name:
                    return param.id if param.id is not None else 0

    def input_list(self) -> List[object]:
        return self.machine_input

    def output_list(self) -> List[object]:
        return self.machine_output

    def get_input_var_name(self) -> Any:
        for input in self.machine_input:
            yield input.var_name

    def get_output_var_name(self) -> Any:
        for output in self.machine_output:
            yield output.var_name

    def set_input_dict(self):
        for input in self.machine_input:
            if input.active:
                yield {input.var_name : [input.var_name_IN, "pyads."+ input.data_type, 1]}

    def set_output_dict(self):
        for output in self.machine_output:
            if output.active:
                yield {output.var_name : [output.var_name_IN, "pyads."+ output.data_type, 1]}

    def __str__(self) -> str:
        return f"Machine ID: {self.machine_id}, Machine Input: {self.input_list}, Machine Output: {self.output_list}"
