"""
SQLAlchemy models for the MCP Connection Hub.

This module contains database models for the application.
"""

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.sql import func
from .database import Base

class APIKey(Base):
    """
    Model for storing API keys for authentication.
    """
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, unique=True, index=True)
    name = Column(String)
    description = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    last_used = Column(DateTime, nullable=True)

# Additional models will be added in future milestones:
# - Tool configurations
# - Job records
# - System settings
