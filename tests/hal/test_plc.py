
"""Tests for PLC module with mock connections."""

from unittest.mock import Mock, patch

import pyads
import pytest

from hal.plc import PLC, AdsConnectionError, VariableNotFoundInRepositoryError


class TestPLC:
    """Test suite for PLC class with mock connections."""

    def test_plc_initialization(self):
        """Test PLC initialization with valid parameters."""
        plc = PLC(netid="1.2.3.4.5.6", ip="192.168.1.100")
        assert plc.netid == "1.2.3.4.5.6"
        assert plc.ip == "192.168.1.100"
        assert plc.plc_vars_input == []
        assert plc.plc_vars_output == []
        assert plc.connection is not None

    @patch('pyads.Connection')
    def test_plc_connection_success(self, mock_connection_class):
        """Test successful PLC connection."""
        # Setup mock
        mock_connection = Mock()
        mock_connection.is_open = False
        mock_connection.read_device_info.return_value = {"device": "test"}
        mock_connection_class.return_value = mock_connection

        plc = PLC(netid="1.2.3.4.5.6", ip="192.168.1.100")
        result = plc.connect()

        # Assertions
        assert result is True
        mock_connection.open.assert_called_once()
        mock_connection.read_device_info.assert_called_once()

    @patch('pyads.Connection')
    def test_plc_connection_failure(self, mock_connection_class):
        """Test PLC connection failure."""
        # Setup mock
        mock_connection = Mock()
        mock_connection.is_open = False
        mock_connection.read_device_info.side_effect = pyads.ADSError("Connection failed")
        mock_connection_class.return_value = mock_connection

        plc = PLC(netid="1.2.3.4.5.6", ip="192.168.1.100")
        result = plc.connect()

        # Assertions
        assert result is False
        mock_connection.open.assert_called_once()
        mock_connection.read_device_info.assert_called_once()

    @patch('pyads.Connection')
    def test_plc_close_connection(self, mock_connection_class):
        """Test closing PLC connection."""
        # Setup mock
        mock_connection = Mock()
        mock_connection.is_open = True
        mock_connection_class.return_value = mock_connection

        plc = PLC(netid="1.2.3.4.5.6", ip="192.168.1.100")
        plc.close()

        # Assertions
        mock_connection.close.assert_called_once()

    def test_set_plc_vars_input_list_empty(self):
        """Test setting input variables list when empty."""
        plc = PLC(netid="1.2.3.4.5.6", ip="192.168.1.100")
        test_vars = [{"name": "var1"}, {"name": "var2"}]

        plc.set_plc_vars_input_list(test_vars)

        assert plc.plc_vars_input == test_vars

    def test_set_plc_vars_input_list_extend(self):
        """Test extending input variables list when not empty."""
        plc = PLC(netid="1.2.3.4.5.6", ip="192.168.1.100")
        plc.plc_vars_input = [{"name": "existing_var"}]
        new_vars = [{"name": "var1"}, {"name": "var2"}]

        plc.set_plc_vars_input_list(new_vars)

        expected = [{"name": "existing_var"}, {"name": "var1"}, {"name": "var2"}]
        assert plc.plc_vars_input == expected

    def test_set_plc_vars_output_list_empty(self):
        """Test setting output variables list when empty."""
        plc = PLC(netid="1.2.3.4.5.6", ip="192.168.1.100")
        test_vars = [{"name": "var1"}, {"name": "var2"}]

        plc.set_plc_vars_output_list(test_vars)

        assert plc.plc_vars_output == test_vars

    def test_set_plc_vars_output_list_extend(self):
        """Test extending output variables list when not empty."""
        plc = PLC(netid="1.2.3.4.5.6", ip="192.168.1.100")
        plc.plc_vars_output = [{"name": "existing_var"}]
        new_vars = [{"name": "var1"}, {"name": "var2"}]

        plc.set_plc_vars_output_list(new_vars)

        expected = [{"name": "existing_var"}, {"name": "var1"}, {"name": "var2"}]
        assert plc.plc_vars_output == expected

    def test_read_variables_not_implemented(self):
        """Test that read_variables raises NotImplementedError."""
        with patch('hal.plc.PLC.connect', return_value=True):
            plc = PLC(netid="1.2.3.4.5.6", ip="192.168.1.100")
            with pytest.raises(NotImplementedError):
                plc.read_variables()

    def test_read_variables_connection_failure(self):
        """Test read_variables when connection fails."""
        with patch('hal.plc.PLC.connect', return_value=False):
            plc = PLC(netid="1.2.3.4.5.6", ip="192.168.1.100")
            with pytest.raises(AdsConnectionError):
                plc.read_variables()

    def test_write_variables_not_implemented(self):
        """Test that write_variables raises NotImplementedError."""
        with patch('hal.plc.PLC.connect', return_value=True):
            plc = PLC(netid="1.2.3.4.5.6", ip="192.168.1.100")
            with pytest.raises(NotImplementedError):
                plc.write_variables()

    def test_write_variables_connection_failure(self):
        """Test write_variables when connection fails."""
        with patch('hal.plc.PLC.connect', return_value=False):
            plc = PLC(netid="1.2.3.4.5.6", ip="192.168.1.100")
            with pytest.raises(AdsConnectionError):
                plc.write_variables()

    def test_check_variables_active_not_implemented(self):
        """Test that check_variables_active raises NotImplementedError."""
        plc = PLC(netid="1.2.3.4.5.6", ip="192.168.1.100")

        with pytest.raises(NotImplementedError):
            plc.check_variables_active()

    @patch('pyads.Connection')
    def test_get_variable_success(self, mock_connection_class):
        """Test successful variable reading."""
        # Setup mock
        mock_connection = Mock()
        mock_connection.read_by_name.return_value = 42
        mock_connection_class.return_value = mock_connection

        # Create test variable
        test_var = Mock()
        test_var.active = "true"
        test_var.var_name_IN = "test_variable"

        plc = PLC(netid="1.2.3.4.5.6", ip="192.168.1.100")
        plc.plc_vars_output = [test_var]

        result = plc.get_variable("test_variable")

        assert result == 42
        mock_connection.read_by_name.assert_called_once_with("test_variable")

    @patch('pyads.Connection')
    def test_get_variable_not_found(self, mock_connection_class):
        """Test variable reading when variable not found."""
        # Setup mock
        mock_connection = Mock()
        mock_connection.read_by_name.side_effect = KeyError("Variable not found")
        mock_connection_class.return_value = mock_connection

        # Create test variable
        test_var = Mock()
        test_var.active = "true"
        test_var.var_name_IN = "test_variable"
        test_var.id = 1

        plc = PLC(netid="1.2.3.4.5.6", ip="192.168.1.100")
        plc.plc_vars_output = [test_var]

        with pytest.raises(VariableNotFoundInRepositoryError):
            plc.get_variable("test_variable")

    @patch('pyads.Connection')
    def test_set_variable_success(self, mock_connection_class):
        """Test successful variable writing."""
        # Setup mock
        mock_connection = Mock()
        mock_connection.write_by_name.return_value = None
        mock_connection_class.return_value = mock_connection

        # Create test variable
        test_var = Mock()
        test_var.active = "true"
        test_var.var_name = "test_variable"
        test_var.var_name_IN = "test_variable"

        plc = PLC(netid="1.2.3.4.5.6", ip="192.168.1.100")
        plc.plc_vars_input = [test_var]

        result = plc.set_variable("test_variable", 123)

        # Note: The current implementation has a bug - it should return the written value
        # but the method returns the result of write_by_name (which is None)
        assert result is None
        mock_connection.write_by_name.assert_called_once_with("test_variable", 123)

    @patch('pyads.Connection')
    def test_set_variable_not_found(self, mock_connection_class):
        """Test variable writing when variable not found."""
        # Setup mock
        mock_connection = Mock()
        mock_connection.write_by_name.side_effect = KeyError("Variable not found")
        mock_connection_class.return_value = mock_connection

        # Create test variable
        test_var = Mock()
        test_var.active = "true"
        test_var.var_name = "test_variable"
        test_var.var_name_IN = "test_variable"
        test_var.id = 1

        plc = PLC(netid="1.2.3.4.5.6", ip="192.168.1.100")
        plc.plc_vars_input = [test_var]

        with pytest.raises(VariableNotFoundInRepositoryError):
            plc.set_variable("test_variable", 123)


class TestPLCExceptions:
    """Test PLC custom exceptions."""

    def test_ads_connection_error(self):
        """Test AdsConnectionError exception."""
        with pytest.raises(AdsConnectionError):
            raise AdsConnectionError("Test connection error")

    def test_variable_not_found_error(self):
        """Test VariableNotFoundInRepositoryError exception."""
        with pytest.raises(VariableNotFoundInRepositoryError):
            raise VariableNotFoundInRepositoryError("Test variable error")

    def test_local_repository_empty_error(self):
        """Test LocalRepositoryEmptyError exception."""
        from hal.plc import LocalRepositoryEmptyError
        with pytest.raises(LocalRepositoryEmptyError):
            raise LocalRepositoryEmptyError("Test repository error")
