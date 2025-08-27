""" A class to load the configuration parameters via given path json."""

import json
import os


class AbbConfig:
    """ a class to load the configuration parameters via given path json."""

    def __init__(self):

        config = self._load_from_json()
        self.TIMEOUT = int(config["TIMEOUT"])  #[s]    avoid freezing the main thread forever in case controller (virtual or real) is not available.
        self.TIMEOUT_LONG = int(config["TIMEOUT_LONG"])  #[s]    avoid freezing the main thread forever, for time consuming processes (slow motions)


    def _load_from_json(self):
        """ Load the configuration parameters from a json file."""

        dir_path = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(dir_path, ".." ,"config", "setup.json")
        with open(filename) as f:
            try:
                output = json.load(f)
            except ValueError:
                print('Decoding JSON has failed')
        return output

