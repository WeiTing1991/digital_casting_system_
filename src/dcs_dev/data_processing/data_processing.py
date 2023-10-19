from typing import Protocol, Any
import os



class PathConfig():
    """
    """
    _HERE:str
    # path = "_config"
    # SRC_DIR = os.path.join(HERE, path)

    def __init__(self):
        """
        """
        self._HERE = os.path.dirname(__file__)
        self._HOME = os.path.abspath(os.path.join(self._HERE, "../../../"))
        os.path.abspath(os.path.join(self._HOME, "data"))

    def get_data_path(self) -> str:
        pass

    def __str__(self) -> str:
        return str(f"Here: {self._HERE} \nHome: {self._HOME} \n")



class DataHandler(Protocol):
    """
    """

    def load_file(self) -> None:
        raise NotImplementedError

    def write_file(self) -> None:
        raise NotImplementedError



class XMLDataHandler(DataHandler):
    pass

if __name__ == "__main__":
    path = PathConfig()
    print(path.get_data_path())


import xml.dom.minidom as xmldom


domtree = xmldom.parse("src\GVL_Data_Com.xml")

group = domtree.documentElement

variables = group.getElementsByTagName("variable")

for variable in variables:
    print(variable.getAttribute("name"))
    print()
    if "Temperature" in variable.getAttribute("name"):
        print(variable.getAttribute("name"))
