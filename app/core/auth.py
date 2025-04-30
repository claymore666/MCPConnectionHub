"""
Authentication and authorization for the MCP Connection Hub.

This module handles API key validation and access control.
"""

from fastapi import Depends, HTTPException, status, Security
from fastapi.security.api_key import APIKeyHeader
from .config import settings

# Define API key header
API_KEY_HEADER = APIKeyHeader(name="X-API-Key", auto_error=False)

async def get_api_key(api_key_header: str = Security(API_KEY_HEADER)):
    """
    Validate the API key from the request header.
    
    This is a simple implementation that will be expanded in future milestones
    to check against the database of valid API keys.
    """
    if not api_key_header:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API Key header is missing",
        )
    
    # In this initial version, just check against the configured API key
    # Later versions will check against the database
    if api_key_header != settings.API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API Key",
        )
    
    return api_key_header

# This function will be expanded in future milestones for more granular access control
async def verify_tool_access(api_key: str = Depends(get_api_key), tool_name: str = None):
    """
    Verify that the API key has access to the requested tool.
    
    Future versions will implement proper access control.
    """
    # Currently, if API key is valid, all tools are accessible
    return True
