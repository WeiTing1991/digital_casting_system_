from abc import ABC, abstractmethod
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


class InlineMixer(Machine):

    def __init__(self, machine_id: int, machine_input: list, machine_output: list):
        self.machine_id = machine_id
        self.machine_input = machine_input
        self.machine_output = machine_output

    def device_id(self) -> int:
        return self.machine_id

    def input_list(self) -> List:
        return self.machine_input

    def output_list(self) -> List:
        return self.machine_input




