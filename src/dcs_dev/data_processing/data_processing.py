import json
import os
from typing import Protocol


class PathConfig():
    """ """

    _HERE: str
    _config: str

    def __init__(self) -> None:
        """ """
        self._HERE = os.path.dirname(__file__)
        self._HOME = os.path.abspath(os.path.join(self._HERE, "../../../"))
        self._config = os.path.abspath(os.path.join(self._HERE, "..", "_config"))
        self.filename = ""

    def _init_machine_dict(self) -> None:
        self.machine_dict = dict()

    def _set_plc_config(self) -> None:
        self.filename = os.path.join(self._config, "beckhoff_controller.json")

    def _set_robot_config(self) -> None:
        self.filename = os.path.join(self._config, "abb_irb4600.json")

    def __str__(self) -> str:
        return str(f"Here: {self._HERE} \nHome: {self._HOME} \nConfig: {self._config}")

    def _load_form_json(self) -> None:
        with open(self.filename, "r") as file:
            try:
                self.machine_dict = json.load(file)
            except ValueError as e:
                print(f"Error: {e}")

    def get_machine_dict(self) -> dict:
        return self.machine_dict

class DataHandler(Protocol):
    """ """

    def load_file(self) -> None:
        raise NotImplementedError

    def write_file(self) -> None:
        raise NotImplementedError

