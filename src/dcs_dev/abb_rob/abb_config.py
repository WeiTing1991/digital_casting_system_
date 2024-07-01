import os
import json

class AbbConfig():

    def __init__(self):

        config = self._load_from_json()
        self.TIMEOUT = int(config["TIMEOUT"])  #[s]    avoid freezing the main thread forever in case controller (virtual or real) is not available.
        self.TIMEOUT_LONG = int(config["TIMEOUT_LONG"])  #[s]    avoid freezing the main thread forever, for time consuming processes (slow motions)


    def _load_from_json(self):

        dir_path = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(dir_path, ".." ,"config", "setup.json")
        with open(filename, 'r') as f:
            try:
                output = json.load(f)
            except ValueError:
                print('Decoding JSON has failed')
        return output
