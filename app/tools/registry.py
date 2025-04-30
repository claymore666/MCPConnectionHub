"""
Tool registry for the MCP Connection Hub.

This module implements the tool registry using Pluggy,
handling tool discovery, registration, and management.
"""

import pluggy
from typing import Dict, List, Any, Callable, Optional

# Define the namespace for the hook specification
hookspec_namespace = "mcp_connection_hub"

class ToolRegistry:
    """
    Registry for tool plugins.
    
    This class manages tool discovery, registration, and access.
    """
    
    def __init__(self):
        """Initialize the tool registry."""
        self.plugin_manager = pluggy.PluginManager(hookspec_namespace)
        self.tools = {}
        self._setup_hookspecs()
    
    def _setup_hookspecs(self):
        """Set up hook specifications for tools."""
        # This is a placeholder that will be expanded in Milestone 1.3
        pass
    
    def register_tool(self, name: str, tool: Any):
        """
        Register a tool with the registry.
        
        Args:
            name: The unique name of the tool
            tool: The tool implementation
        """
        self.tools[name] = tool
    
    def get_tool(self, name: str) -> Optional[Any]:
        """
        Get a tool by name.
        
        Args:
            name: The name of the tool to retrieve
            
        Returns:
            The tool implementation or None if not found
        """
        return self.tools.get(name)
    
    def list_tools(self) -> List[str]:
        """
        List all registered tools.
        
        Returns:
            A list of tool names
        """
        return list(self.tools.keys())
    
    def get_tool_capabilities(self, name: str) -> Dict[str, Any]:
        """
        Get the capabilities of a tool.
        
        Args:
            name: The name of the tool
            
        Returns:
            A dictionary describing the tool's capabilities
        """
        tool = self.get_tool(name)
        if not tool:
            return {}
        
        # This is a placeholder that will be expanded in Milestone 1.3
        # It will call a method on the tool to get its capabilities
        return {"name": name, "status": "registered"}
    
    def get_all_tool_capabilities(self) -> Dict[str, Dict[str, Any]]:
        """
        Get capabilities of all registered tools.
        
        Returns:
            A dictionary mapping tool names to their capabilities
        """
        capabilities = {}
        for name in self.list_tools():
            capabilities[name] = self.get_tool_capabilities(name)
        return capabilities

# Create a global instance of the tool registry
tool_registry = ToolRegistry()

def get_tool_registry() -> ToolRegistry:
    """
    Get the global tool registry instance for dependency injection.
    """
    return tool_registry
