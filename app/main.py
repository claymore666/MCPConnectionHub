"""
Main application module for the MCP Connection Hub.

This module initializes the FastAPI application, sets up middleware,
and includes all the necessary routers.
"""

import os
from fastapi import FastAPI, Request, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Import modules that will be implemented in later steps
# from app.db.database import init_db
# from app.core.config import settings
# from app.api.routes import router as api_router
# from app.core.auth import get_api_key

# Create FastAPI application
app = FastAPI(
    title="MCP Connection Hub",
    description="A unified Model Context Protocol Gateway",
    version="0.1.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health", tags=["health"])
async def health_check():
    """
    Health check endpoint to verify service is running.
    """
    return {"status": "healthy"}

# Basic root endpoint
@app.get("/", tags=["root"])
async def root():
    """
    Root endpoint providing basic service information.
    """
    return {
        "service": "MCP Connection Hub",
        "version": "0.1.0",
        "status": "initializing"
    }

# Startup event to initialize database and other components
@app.on_event("startup")
async def startup_event():
    """
    Initialize components during application startup.
    """
    # This will be implemented in later milestones
    # await init_db()
    pass

# Include routers (to be added in future milestones)
# app.include_router(api_router, prefix="/api")

# Run the application (when executed directly)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
