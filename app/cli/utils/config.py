"""
Configuration utilities for the CLI.

This module provides helpers for working with configuration in the CLI.
"""

import os
import json
from typing import Dict, Any, Optional
from rich.console import Console
import configparser

console = Console()

class CLIConfig:
    """
    Configuration manager for the CLI.
    
    This class handles loading and saving CLI-specific configuration.
    """
    
    def __init__(self, config_file: Optional[str] = None):
        """
        Initialize the configuration manager.
        
        Args:
            config_file: Path to configuration file (default: ~/.mcp-cli.ini)
        """
        self.config_file = config_file or os.path.expanduser("~/.mcp-cli.ini")
        self.config = configparser.ConfigParser()
        self.load()
    
    def load(self):
        """Load configuration from file."""
        if os.path.exists(self.config_file):
            try:
                self.config.read(self.config_file)
            except Exception as e:
                console.print(f"[red]Error loading configuration: {str(e)}[/red]")
                # Initialize with defaults
                self._init_defaults()
        else:
            # Initialize with defaults
            self._init_defaults()
    
    def _init_defaults(self):
        """Initialize with default configuration."""
        self.config["api"] = {
            "url": "http://localhost:8000",
            "key": os.getenv("MCP_HUB_API_KEY", "default_dev_key_change_me")
        }
        
        self.config["cli"] = {
            "verbose": "false",
            "color": "true"
        }
    
    def save(self):
        """Save configuration to file."""
        try:
            with open(self.config_file, "w") as f:
                self.config.write(f)
        except Exception as e:
            console.print(f"[red]Error saving configuration: {str(e)}[/red]")
    
    def get(self, section: str, option: str, fallback: Any = None) -> str:
        """
        Get a configuration value.
        
        Args:
            section: Configuration section
            option: Option name
            fallback: Fallback value if not found
            
        Returns:
            Configuration value
        """
        return self.config.get(section, option, fallback=fallback)
    
    def set(self, section: str, option: str, value: str):
        """
        Set a configuration value.
        
        Args:
            section: Configuration section
            option: Option name
            value: Value to set
        """
        if not self.config.has_section(section):
            self.config.add_section(section)
        
        self.config.set(section, option, value)
    
    def get_all(self) -> Dict[str, Dict[str, str]]:
        """
        Get all configuration values.
        
        Returns:
            Dictionary of all configuration values
        """
        result = {}
        for section in self.config.sections():
            result[section] = dict(self.config[section])
        return result

# Create a global config instance
cli_config = CLIConfig()

def get_cli_config() -> CLIConfig:
    """
    Get the global CLI configuration instance.
    
    Returns:
        CLIConfig instance
    """
    return cli_config
