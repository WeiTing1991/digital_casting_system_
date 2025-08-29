"""Configuration manager for project and machine settings.

This module provides centralized configuration management for the digital casting
system, handling robot configurations, PLC settings, and other system parameters
loaded from JSON configuration files.
"""

import json
import os
from typing import Any


class ConfigManager:
    """Manages configuration for project and machine settings.
    
    The ConfigManager provides a centralized interface for loading and accessing
    configuration data for various components of the digital casting system,
    including robot controllers, PLC settings, and machine parameters.
    
    Configuration files are stored in JSON format and loaded on demand. The
    manager handles file path resolution and error handling for missing or
    corrupted configuration files.
    
    Attributes:
        _HERE (str): Directory path of this module file.
        _HOME (str): Root directory path of the project.
        _config_dir (str): Directory path where configuration files are stored.
        
    Example:
        >>> config = ConfigManager()
        >>> robot_config = config.get_robot_config()
        >>> plc_config = config.get_plc_config()
        >>> print(f"Robot type: {robot_config.get('type', 'Unknown')}")
    """

    def __init__(self) -> None:
        """Initialize configuration manager with default paths.
        
        Sets up the directory paths used for locating configuration files
        relative to the current module location.
        """
        self._HERE = os.path.dirname(__file__)
        """Directory path of this module file."""

        self._HOME = os.path.abspath(os.path.join(self._HERE, "../../"))
        """Root directory path of the project."""

        self._config_dir = os.path.abspath(os.path.join(self._HERE, "../dcs/_config"))
        """Directory path where configuration files are stored."""

    def get_robot_config(self) -> dict[str, Any]:
        """Get robot configuration from JSON file.
        
        Loads and returns the ABB IRB4600 robot configuration including
        communication settings, coordinate systems, tool definitions,
        and operational parameters.
        
        Returns:
            Dict[str, Any]: Dictionary containing robot configuration data
                including network settings, coordinate frames, joint limits,
                and other robot-specific parameters.
                
        Raises:
            FileNotFoundError: If the robot configuration file is not found.
            ValueError: If the configuration file contains invalid JSON.
            
        Example:
            >>> config = ConfigManager()
            >>> robot_config = config.get_robot_config()
            >>> ip_address = robot_config.get('network', {}).get('ip')
            >>> joint_limits = robot_config.get('joint_limits', [])
        """
        config_path = os.path.join(self._config_dir, "abb_irb4600.json")
        return self._load_json_config(config_path)

    def get_plc_config(self) -> dict[str, Any]:
        """Get PLC configuration from JSON file.
        
        Loads and returns the Beckhoff TwinCAT PLC configuration including
        network settings, variable definitions, communication parameters,
        and device mappings.
        
        Returns:
            Dict[str, Any]: Dictionary containing PLC configuration data
                including ADS settings, network parameters, variable lists,
                and machine definitions.
                
        Raises:
            FileNotFoundError: If the PLC configuration file is not found.
            ValueError: If the configuration file contains invalid JSON.
            
        Example:
            >>> config = ConfigManager()
            >>> plc_config = config.get_plc_config()
            >>> netid = plc_config.get('network', {}).get('netid')
            >>> machines = plc_config.get('machines', [])
        """
        config_path = os.path.join(self._config_dir, "beckhoff_controller.json")
        return self._load_json_config(config_path)

    def _load_json_config(self, config_path: str) -> dict[str, Any]:
        """Load configuration from JSON file.
        
        Internal method for loading and parsing JSON configuration files
        with proper error handling for missing files and invalid JSON.
        
        Args:
            config_path (str): Full path to the JSON configuration file.
            
        Returns:
            Dict[str, Any]: Parsed JSON data as a dictionary.
            
        Raises:
            FileNotFoundError: If the specified configuration file does not exist.
            ValueError: If the file contains invalid JSON that cannot be parsed.
            
        Note:
            This method is used internally by get_robot_config() and get_plc_config()
            and should not be called directly unless implementing custom configuration
            loading methods.
        """
        try:
            with open(config_path) as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in configuration file: {config_path}")
