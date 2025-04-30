"""
CLI entry point for the MCP Connection Hub.

This module provides the entry point for the CLI when installed as a package.
"""

from app.cli.main import app

def main():
    """Run the CLI application."""
    app()

if __name__ == "__main__":
    main()
