"""
********************************************************************************
digital_casting_system
********************************************************************************

.. currentmodule:: digital_casting_system


.. toctree::
    :maxdepth: 2


"""
from __future__ import print_function
from __future__ import absolute_import
import os


__author__ = ["wei ting chen"]
__copyright__ = ""
__license__ = "MIT License"
__email__ = "wei.ting.chen@usi.ch"
__version__ = "2.0.0"


HERE = os.path.dirname(__file__)

HOME = os.path.abspath(os.path.join(HERE, "../../"))
DATA = os.path.abspath(os.path.join(HOME, "data"))
DOCS = os.path.abspath(os.path.join(HOME, "docs"))
TEMP = os.path.abspath(os.path.join(HOME, "temp"))

__all__ = ["HOME", "DATA", "DOCS", "TEMP"]

