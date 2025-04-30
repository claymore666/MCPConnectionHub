"""
Database initialization and session management.

This module handles database connection, session creation,
and provides helper functions for database operations.
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

# Will be replaced with settings import in future milestones
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./mcp_hub.db")

# Check if we're using SQLite
is_sqlite = DATABASE_URL.startswith("sqlite")

# Create engine (will be replaced with async engine in future)
if is_sqlite:
    # Ensure the database directory exists
    db_path = DATABASE_URL.replace("sqlite:///", "")
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    # SQLite-specific configuration
    engine = create_engine(
        DATABASE_URL, 
        connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for models
Base = declarative_base()

# Session dependency
def get_db():
    """
    Get database session for dependency injection.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def init_db():
    """
    Initialize the database, creating tables if they don't exist.
    
    This function will be expanded in future milestones.
    """
    # Will be implemented to create tables in future milestones
    # Base.metadata.create_all(bind=engine)
    pass
