from unittest.mock import Mock

import pyads
import pytest

from dcs.hal.plc import PLC


@pytest.fixture(scope='function')
def pyads_mock():
    mock = Mock()
    connection = pyads.Connection
    pyads.Connection = mock
    yield mock
    pyads.Connection = connection


@pytest.fixture(scope='function')
def plc_mock(pyads_mock):
    return PLC(ip="192.168.99.99", netid="1.2.3.4.5.6")


@pytest.fixture(scope='function')
def plc_hardware():
    plc = PLC(ip="192.168.11.234", netid="192.168.11.234.1.1")
    if not plc.is_connected():
        pytest.skip("Cannot connect to PLC, skip test.")
    return plc

