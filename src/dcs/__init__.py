"""
********************************************************************************
dcs
********************************************************************************

.. currentmodule:: dcs


.. toctree::
    :maxdepth: 1


"""

from __future__ import print_function

import os


__author__ = ["WeiTingChen"]
__copyright__ = ""
__license__ = "MIT License"
__email__ = "chenw@usi.ch"
__version__ = "0.1.0"


HERE = os.path.dirname(__file__)

HOME = os.path.abspath(os.path.join(HERE, "../../"))
DATA = os.path.abspath(os.path.join(HOME, "data"))
DOCS = os.path.abspath(os.path.join(HOME, "docs"))
TEMP = os.path.abspath(os.path.join(HOME, "temp"))


__all__ = ["HOME", "DATA", "DOCS", "TEMP"]
