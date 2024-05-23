from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


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

    def input_list(self) -> List:
        return self.machine_input

    def output_list(self) -> List:
        return self.machine_input




