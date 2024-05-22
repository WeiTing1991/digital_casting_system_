from attrs import Attribute
from abc import ABC, abstractmethod


class Machine(ABC):

    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def set_run(self):
        pass


