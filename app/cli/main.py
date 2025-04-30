"""
Command-line interface for MCP Connection Hub.

This module provides the main CLI entry point and command structure.
"""

import typer
from typing import Optional
from rich.console import Console
from rich.table import Table
import os
import sys

# Create Typer app
app = typer.Typer(
    name="mcp-cli",
    help="MCP Connection Hub CLI tool",
    add_completion=False,
)

# Create Console for rich output
console = Console()

# Add module imports for command groups
# These will be implemented in future milestones
from app.cli.commands import tool, config, system, job, user

# Add command groups to app
app.add_typer(tool.app, name="tool", help="Manage tools and plugins")
app.add_typer(config.app, name="config", help="View and edit configuration")
app.add_typer(system.app, name="system", help="System management commands")
app.add_typer(job.app, name="job", help="Manage long-running jobs")
app.add_typer(user.app, name="user", help="Manage users and API keys")

@app.callback()
def main(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose output"),
    config_file: Optional[str] = typer.Option(None, "--config", "-c", help="Path to config file"),
):
    """
    MCP Connection Hub CLI - Admin tool for system management.
    """
    # Set up environment based on options
    if verbose:
        os.environ["LOG_LEVEL"] = "DEBUG"
    
    # Load config file if specified
    if config_file:
        # This will be implemented in future milestones
        pass

@app.command("version")
def version():
    """
    Show version information.
    """
    from app import __version__
    console.print(f"MCP Connection Hub CLI v{__version__}")

@app.command("status")
def status():
    """
    Show system status overview.
    """
    table = Table(title="MCP Connection Hub Status")
    table.add_column("Component", style="cyan")
    table.add_column("Status", style="green")
    
    # Add rows with placeholder data
    # Will be implemented properly in future milestones
    table.add_row("API Server", "Online")
    table.add_row("Database", "Connected")
    table.add_row("Tool Registry", "3 Tools Loaded")
    
    console.print(table)

if __name__ == "__main__":
    app()
