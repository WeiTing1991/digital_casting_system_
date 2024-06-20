import json
import os

from .data_struct import DataObject
from .data_struct import DataParam


class PathConfig:
    """
    A class to handle paths and configurations.

    Attributes:
        _HERE (str): The directory path of the current file.
        _HOME (str): The absolute path of the home directory.
        _config (str): The absolute path of the configuration directory.
        filename (str): The filename of the configuration file.
    """

    def __init__(self) -> None:
        """
        _HERE: str
        _config: str

        """
        self._HERE = os.path.dirname(__file__)
        self._HOME = os.path.abspath(os.path.join(self._HERE, "../../../"))
        self._config = os.path.abspath(os.path.join(self._HERE, "..", "_config"))
        self.filename = ""

    def _init_machine_dict(self) -> None:
        self.machine_dict = dict()

    def _set_plc_mode_config(self) -> None:
        self.filename = os.path.join(self._config, "beckhoff_controller.json")

    def _set_robot_mode_config(self) -> None:
        self.filename = os.path.join(self._config, "abb_irb4600.json")

    def __str__(self) -> str:
        return str(f"Here: {self._HERE} \nHome: {self._HOME} \nConfig: {self._config}")


class DataHandler(PathConfig):
    """
    A class to handle data loading and manipulation.

    Inherits from:
        PathConfig

    Attributes:
        machine_dict (dict): A dictionary to store machine data.
        machine (DataParam): An instance of DataParam to hold machine data.
    """

    def __init__(self) -> None:
        super().__init__()
        self.machine_dict = dict()
        self.machine = DataParam(0, [], [])

    def _load_json_to_dict(self) -> None:
        with open(self.filename, "r") as file:
            try:
                self.machine_dict = json.load(file)
            except ValueError as e:
                print(f"Error: {e}")

    def _load_json_to_instance(self) -> None:
        with open(self.filename, "r") as file:
            try:
                self.machine = json.load(file, object_hook=self.data_object_decoder)
            except ValueError as e:
                print(f"Error: {e}")

    def get_machine_dict(self) -> dict:
        return self.machine_dict

    @staticmethod
    def data_object_decoder(obj) -> object:
        if "machine_id" in obj:
            machine_id = obj["machine_id"]
            inputs = [DataObject(**input_data) for input_data in obj.get("input", [])]
            outputs = [DataObject(**output_data) for output_data in obj.get("output", [])]
            return DataParam(machine_id, inputs, outputs)
        return obj
