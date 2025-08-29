"""Configuration manager for project and machine settings."""

import json
import os
from typing import Any


class ConfigManager:
    """Manages configuration for project and machine settings."""

    def __init__(self) -> None:
        """Initialize configuration manager."""
        self._HERE = os.path.dirname(__file__)
        self._HOME = os.path.abspath(os.path.join(self._HERE, "../../"))
        self._config_dir = os.path.abspath(os.path.join(self._HERE, "../dcs/_config"))

    def get_robot_config(self) -> dict[str, Any]:
        """Get robot configuration from JSON file."""
        config_path = os.path.join(self._config_dir, "abb_irb4600.json")
        return self._load_json_config(config_path)

    def get_plc_config(self) -> dict[str, Any]:
        """Get PLC configuration from JSON file."""
        config_path = os.path.join(self._config_dir, "beckhoff_controller.json")
        return self._load_json_config(config_path)

    def _load_json_config(self, config_path: str) -> dict[str, Any]:
        """Load configuration from JSON file."""
        try:
            with open(config_path) as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in configuration file: {config_path}")
