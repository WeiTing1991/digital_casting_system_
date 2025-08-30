import csv
import json
import os

from .struct import DataObject, DataParam


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
    self.machine_id = 0
    self.machine_input = []
    self.machine_output = []
    self.machine = DataParam(self.machine_id, self.machine_input, self.machine_output)

  def _load_json_to_dict(self) -> None:
    with open(self.filename) as file:
      try:
        self.machine_dict = json.load(file)
      except ValueError as e:
        print(f"Error: {e}")

  def _load_json_to_instance(self) -> None:
    with open(self.filename) as file:
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


class DataGathering(PathConfig):
  """
  A class to handle data gathering from the PLC.
  Inherits from:
      PathConfig

  Attributes:
      _DATA (str): The absolute path of the data directory.
      _JSON_DIR (str): The absolute path of the json directory.
      _CSV_DIR (str): The absolute path of the csv directory.

  """

  def __init__(self, filename) -> None:
    super().__init__()
    self._DATA = os.path.abspath(os.path.join(self._HOME, "data"))
    self._JSON_DIR = os.path.join(self._DATA, "json")
    self._CSV_DIR = os.path.join(self._DATA, "csv")
    self.filename = filename

  def write_dict_to_json(self, data):
    path = os.path.join(self._JSON_DIR, self.filename) + ".json"
    # Write the python dictionary to json file
    with open(path, "w") as f:
      json.dump(data, f, sort_keys=True, indent=5)
      print(f"\nThe json file is sucessfully exported! in {path}")

  def write_dict_to_csv(self, data, header):
    path = os.path.join(self._CSV_DIR, self.filename) + ".csv"
    # Write the python dictionary to csv file
    with open(path, "w+", newline="") as f:
      writer = csv.DictWriter(f, fieldnames=header)
      writer.writeheader()
      writer.writerows(data)
      print(f"\nThe csv file is sucessfully exported! in {self._CSV_DIR}")
