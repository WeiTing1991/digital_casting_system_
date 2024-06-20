from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Any, Dict


class Machine(ABC):

    @abstractmethod
    def device_id(self) -> int:
        pass
    @abstractmethod
    def input_list(self) -> List:
        pass
    @abstractmethod
    def output_list(self) -> List:
        pass


@dataclass
class InlineMixer(Machine):
    """

    """
    machine_id: int
    machine_input: List
    machine_output: List
    machine_error_num: int = 0

    def device_id(self) -> int:
        return self.machine_id

    def input_list(self) -> List[object]:
        return self.machine_input

    def output_list(self) -> List[object]:
        return self.machine_input

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

    def __str__(self) -> str:
        return f"Machine ID: {self.machine_id}, Machine Input: {self.input_list}, Machine Output: {self.output_list}"
