"""
Hook specifications for MCP Connection Hub tools.

This module defines the interface that tool plugins must implement.
"""

import pluggy
from typing import Dict, List, Any, Optional

# Define the hookspec namespace
hookspec = pluggy.HookspecMarker("mcp_connection_hub")

class ToolSpec:
    """
    Tool hook specifications.
    
    These methods define the interface that tool implementations
    must provide to be compatible with the MCP Connection Hub.
    """
    
    @hookspec
    def get_tool_info(self) -> Dict[str, Any]:
        """
        Get information about the tool.
        
        Returns:
            Dictionary with tool information including:
            - name: Tool's unique name
            - description: Tool's description
            - version: Tool's version
            - author: Tool's author
        """
    
    @hookspec
    def get_tool_capabilities(self) -> Dict[str, Any]:
        """
        Get the capabilities of the tool.
        
        Returns:
            Dictionary describing the tool's capabilities including:
            - functions: List of functions the tool provides
            - parameters: Parameter schemas for each function
            - execution_modes: Supported execution modes (sync/async)
            - timeout: Default timeout for synchronous execution
        """
    
    @hookspec
    def execute_tool(self, function: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the tool with the given function and parameters.
        
        Args:
            function: The function to execute
            parameters: The parameters to pass to the function
            
        Returns:
            Dictionary with the results of the execution
        """
    
    @hookspec
    def get_default_config(self) -> Dict[str, Any]:
        """
        Get the default configuration for the tool.
        
        Returns:
            Dictionary with default configuration settings
        """
    
    @hookspec
    def validate_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate the configuration for the tool.
        
        Args:
            config: The configuration to validate
            
        Returns:
            Dictionary with validation results:
            - valid: Boolean indicating if the configuration is valid
            - errors: List of error messages if invalid
        """
