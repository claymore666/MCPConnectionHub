"""
Brave Search tool implementation.

This module provides the BraveSearchTool class for integration with Brave Search API.
"""

from typing import Dict, List, Any
import httpx
from app.tools.base import BaseTool
from app.core.config import settings

class BraveSearchTool(BaseTool):
    """
    Tool for performing web searches using Brave Search API.
    """
    
    def __init__(self):
        """Initialize the Brave Search tool."""
        super().__init__(
            name="brave_web_search",
            description="Performs a web search using the Brave Search API"
        )
    
    def _get_functions(self) -> List[str]:
        """
        Get the list of functions provided by this tool.
        
        Returns:
            List of function names
        """
        return ["web_search", "local_search"]
    
    def _execute_function(self, function: str, parameters: Dict[str, Any]) -> Any:
        """
        Execute the specified function with the given parameters.
        
        Args:
            function: The function to execute
            parameters: The parameters to pass to the function
            
        Returns:
            The result of the function execution
        """
        if function == "web_search":
            return self._web_search(parameters)
        elif function == "local_search":
            return self._local_search(parameters)
        else:
            raise ValueError(f"Unknown function: {function}")
    
    def _web_search(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform a web search using Brave Search API.
        
        Args:
            parameters: Search parameters including:
                - query: Search query
                - count: Number of results (default: 10)
                - offset: Result offset for pagination (default: 0)
                
        Returns:
            Dictionary with search results
        """
        # This is a placeholder implementation
        # Will be fully implemented in Milestone 2.4
        return {
            "search_query": parameters.get("query", ""),
            "count": parameters.get("count", 10),
            "offset": parameters.get("offset", 0),
            "results": [
                {
                    "title": "Placeholder Search Result",
                    "url": "https://example.com",
                    "description": "This is a placeholder result. The Brave Search API will be fully implemented in a future milestone."
                }
            ]
        }
    
    def _local_search(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform a local search using Brave Search API.
        
        Args:
            parameters: Search parameters including:
                - query: Search query
                - count: Number of results (default: 5)
                
        Returns:
            Dictionary with local search results
        """
        # This is a placeholder implementation
        # Will be fully implemented in Milestone 2.4
        return {
            "search_query": parameters.get("query", ""),
            "count": parameters.get("count", 5),
            "results": [
                {
                    "name": "Placeholder Local Result",
                    "address": "123 Main St, Anytown, USA",
                    "rating": 4.5,
                    "type": "Restaurant"
                }
            ]
        }
    
    def _get_execution_modes(self) -> List[str]:
        """
        Get the supported execution modes for this tool.
        
        Returns:
            List of supported modes
        """
        return ["sync", "async"]
    
    def _get_default_timeout(self) -> int:
        """
        Get the default timeout for synchronous execution in seconds.
        
        Returns:
            Timeout in seconds
        """
        return 10
    
    def get_default_config(self) -> Dict[str, Any]:
        """
        Get the default configuration for the tool.
        
        Returns:
            Dictionary with default configuration settings
        """
        config = super().get_default_config()
        config.update({
            "api_key": settings.BRAVE_SEARCH_API_KEY or "",
            "max_results": 10,
            "timeout": 10
        })
        return config
    
    def _validate_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform tool-specific configuration validation.
        
        Args:
            config: The configuration to validate
            
        Returns:
            Dictionary with validation results
        """
        valid = True
        errors = []
        
        # Check for API key
        if not config.get("api_key"):
            valid = False
            errors.append("Brave Search API key is required")
        
        # Check max_results
        if "max_results" in config:
            max_results = config["max_results"]
            if not isinstance(max_results, int) or max_results < 1 or max_results > 20:
                valid = False
                errors.append("max_results must be an integer between 1 and 20")
        
        return {
            "valid": valid,
            "errors": errors
        }
