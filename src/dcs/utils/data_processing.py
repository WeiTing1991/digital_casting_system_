import csv
import json
import os
from datetime import datetime


class DataProcessing:
    """
    This is a class that provides the data collection, processing, handlering.

    """
    def __init__(self, filename=str, data=dict):
        """ Initialize the class with the filename and data. """
        # Date
        NOW_DATA = datetime.now().date().strftime("%Y%m%d")
        HERE = os.path.dirname(__file__)
        HOME = os.path.abspath(os.path.join(HERE, "../../../"))
        DATA = os.path.abspath(os.path.join(HOME, "data"))

        self.__date = NOW_DATA
        self.default_filename = self.__date + "_" + filename

        self.__data = DATA
        JSON_DIR = os.path.join(self.__data, "json")
        CSV_DIR = os.path.join(self.__data, "csv")

        self.filepath_json = JSON_DIR
        self.filepath_csv = CSV_DIR

        self.data = data
        self.number_recorded = 0

    @property
    def data_dict(self) -> None:
        return self.data

    @data_dict.setter
    def update_data(self, new_data) -> None:
        """ """
        self.data = new_data

    def __is_file_existed(self, filepath=str) -> bool:
        """
        check the file is aready in the folder.
        """
        if os.path.isfile(filepath):
            return True
        else:
            return False

    def write_dict_to_json(self):
        """
        write python dictionary to json format profile.

        """
        __filename = os.path.join(self.filepath_json, self.default_filename) + ".json"

        if self.__is_file_existed(__filename) != True:
            # Write the python dictionary to json file
            with open(__filename, "w") as f:
                json.dump(self.data, f, sort_keys=True, indent=2)
                print("\nThe json file is sucessfully exported!!!")
        else:
            self.number_recorded += 1
            __next_filename = __filename + str(self.number_recorded)

            with open(__next_filename, "w") as f:
                json.dump(self.data, f, sort_keys=True, indent=2)
                print("\nThe json file is sucessfully exported!!!")

            # raise Exception("The file is existed, PLEASE change the name")

    def write_dict_to_csv(self, header):
        """ """
        __filepath = os.path.join(self.filepath_csv, self.default_filename) + ".csv"
        # Write the python dictionary to csv file
        if self.__is_file_existed(__filepath) != True:
            with open(__filepath, "w+", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=header)
                writer.writeheader()
                writer.writerows(self.data)
                print("\nThe csv file is sucessfully exported!!!")
        else:
            raise Exception("The file is existed, PLEASE change the name")
