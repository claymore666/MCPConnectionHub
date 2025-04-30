"""
API routes for the MCP Connection Hub.

This module defines the routes for the API endpoints.
"""

from fastapi import APIRouter
# Import route modules as they are implemented
# from .openai import router as openai_router

# Create main router
router = APIRouter()

# Include sub-routers
# router.include_router(openai_router, prefix="/openai", tags=["openai"])

# Additional routers will be added in future milestones:
# - Tool management routes
# - Job management routes
# - System status routes
# - Configuration routes
