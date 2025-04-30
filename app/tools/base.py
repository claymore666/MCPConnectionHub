"""
Base tool implementation for MCP Connection Hub.

This module provides the BaseTool class that all tools should inherit from.
"""

import pluggy
from typing import Dict, List, Any, Optional
from abc import ABC, abstractmethod

# Define the hookimpl marker
hookimpl = pluggy.HookimplMarker("mcp_connection_hub")

class BaseTool(ABC):
    """
    Base class for all tools.
    
    This class implements the common functionality for all tools and
    defines the interface that specific tool implementations must provide.
    """
    
    def __init__(self, name: str, description: str):
        """
        Initialize the base tool.
        
        Args:
            name: Unique name for the tool
            description: Description of the tool's purpose
        """
        self.name = name
        self.description = description
        self.version = "0.1.0"
        self.author = "MCP Connection Hub"
        self.config = self.get_default_config()
    
    @hookimpl
    def get_tool_info(self) -> Dict[str, Any]:
        """
        Get information about the tool.
        
        Returns:
            Dictionary with tool information
        """
        return {
            "name": self.name,
            "description": self.description,
            "version": self.version,
            "author": self.author
        }
    
    @hookimpl
    def get_tool_capabilities(self) -> Dict[str, Any]:
        """
        Get the capabilities of the tool.
        
        Returns:
            Dictionary describing the tool's capabilities
        """
        return {
            "functions": self._get_functions(),
            "execution_modes": self._get_execution_modes(),
            "timeout": self._get_default_timeout()
        }
    
    @hookimpl
    def execute_tool(self, function: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the tool with the given function and parameters.
        
        Args:
            function: The function to execute
            parameters: The parameters to pass to the function
            
        Returns:
            Dictionary with the results of the execution
        """
        # Check if the function exists
        if function not in self._get_functions():
            return {
                "error": f"Function '{function}' not found",
                "status": "error"
            }
        
        # Execute the appropriate function
        try:
            result = self._execute_function(function, parameters)
            return {
                "result": result,
                "status": "success"
            }
        except Exception as e:
            return {
                "error": str(e),
                "status": "error"
            }
    
    @hookimpl
    def get_default_config(self) -> Dict[str, Any]:
        """
        Get the default configuration for the tool.
        
        Returns:
            Dictionary with default configuration settings
        """
        return {
            "enabled": True,
            "execution_mode": "sync",
            "timeout": self._get_default_timeout()
        }
    
    @hookimpl
    def validate_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate the configuration for the tool.
        
        Args:
            config: The configuration to validate
            
        Returns:
            Dictionary with validation results
        """
        # Basic validation that all tools should have
        valid = True
        errors = []
        
        # Check required fields
        required_fields = ["enabled", "execution_mode", "timeout"]
        for field in required_fields:
            if field not in config:
                valid = False
                errors.append(f"Missing required field: {field}")
        
        # Check execution mode
        if "execution_mode" in config and config["execution_mode"] not in ["sync", "async"]:
            valid = False
            errors.append(f"Invalid execution mode: {config['execution_mode']}")
        
        # Check timeout
        if "timeout" in config and not isinstance(config["timeout"], (int, float)):
            valid = False
            errors.append(f"Timeout must be a number")
        
        # Let the specific tool do additional validation
        additional_validation = self._validate_config(config)
        if not additional_validation.get("valid", True):
            valid = False
            errors.extend(additional_validation.get("errors", []))
        
        return {
            "valid": valid,
            "errors": errors
        }
    
    @abstractmethod
    def _get_functions(self) -> List[str]:
        """
        Get the list of functions provided by this tool.
        
        Returns:
            List of function names
        """
        pass
    
    @abstractmethod
    def _execute_function(self, function: str, parameters: Dict[str, Any]) -> Any:
        """
        Execute the specified function with the given parameters.
        
        Args:
            function: The function to execute
            parameters: The parameters to pass to the function
            
        Returns:
            The result of the function execution
        """
        pass
    
    def _get_execution_modes(self) -> List[str]:
        """
        Get the supported execution modes for this tool.
        
        Returns:
            List of supported modes ("sync", "async", or both)
        """
        return ["sync"]
    
    def _get_default_timeout(self) -> int:
        """
        Get the default timeout for synchronous execution in seconds.
        
        Returns:
            Timeout in seconds
        """
        return 10
    
    def _validate_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform tool-specific configuration validation.
        
        Args:
            config: The configuration to validate
            
        Returns:
            Dictionary with validation results
        """
        # Default implementation assumes configuration is valid
        return {"valid": True, "errors": []}
