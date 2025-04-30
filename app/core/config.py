"""
Configuration management for MCP Connection Hub.

This module handles loading configuration from environment variables,
configuration files, and provides a central settings object.
"""

import os
from typing import List, Dict, Any, Optional
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """
    # Application settings
    APP_NAME: str = "MCP Connection Hub"
    VERSION: str = "0.1.0"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    # API settings
    API_KEY: str = os.getenv("API_KEY", "default_dev_key_change_me")
    
    # Database settings
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./mcp_hub.db")
    
    # CORS settings
    CORS_ORIGINS: List[str] = ["*"]
    
    # Tool settings (placeholder for future expansion)
    TOOLS_ENABLED: bool = True
    BRAVE_SEARCH_API_KEY: Optional[str] = os.getenv("BRAVE_SEARCH_API_KEY")
    
    # File paths
    DATA_DIR: str = "/data"
    DB_DIR: str = "/data/db"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Create global settings instance
settings = Settings()

def get_settings() -> Settings:
    """
    Get application settings for dependency injection.
    """
    return settings
