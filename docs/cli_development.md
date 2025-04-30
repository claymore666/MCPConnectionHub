# MCP Connection Hub CLI Development Guide

This document provides guidance for developing and extending the MCP Connection Hub CLI.

## Architecture Overview

The CLI is built with a modular architecture using Typer and Rich:

```
app/cli/
├── __init__.py            # Package initialization
├── entry.py               # Entry point for installed CLI
├── main.py                # Main CLI application definition
├── README.md              # CLI documentation
├── commands/              # Command modules
│   ├── __init__.py        # Package initialization
│   ├── tool.py            # Tool management commands
│   ├── config.py          # Configuration commands
│   ├── system.py          # System management commands
│   ├── job.py             # Job management commands
│   └── user.py            # User management commands
└── utils/                 # Utility modules
    ├── __init__.py        # Package initialization
    ├── formatting.py      # Output formatting utilities
    ├── config.py          # CLI configuration handling
    └── connection.py      # API connection utilities
```

## Adding New Commands

### 1. Create a Command Module

To add a new command category:

1. Create a new module in the `commands` directory
2. Define a Typer app for the command group
3. Add commands using the `@app.command()` decorator

Example (`commands/example.py`):

```python
"""
Example commands for the MCP Connection Hub CLI.
"""

import typer
from rich.console import Console

# Create Typer app for example commands
app = typer.Typer(name="example", help="Example commands")

# Create Console for rich output
console = Console()

@app.command("hello")
def hello_world(
    name: str = typer.Argument("World", help="Name to greet")
):
    """
    Say hello to the specified name.
    """
    console.print(f"[green]Hello, {name}![/green]")
```

### 2. Register the Command Group

Update `main.py` to include the new command group:

```python
# Add import
from app.cli.commands import example

# Add command group
app.add_typer(example.app, name="example", help="Example commands")
```

### 3. Using Utilities

Use the utility modules for consistent formatting and API access:

```python
from app.cli.utils.formatting import print_json, create_status_table
from app.cli.utils.connection import get_api_client

@app.command("status")
def example_status():
    """
    Show example status.
    """
    # Create a status table
    data = {
        "Component 1": {"Status": "Active", "Details": "Running normally"},
        "Component 2": {"Status": "Warning", "Details": "High resource usage"}
    }
    
    table = create_status_table("Example Status", data)
    console.print(table)
    
    # Make API request
    api_client = get_api_client()
    result = await api_client.get("/api/example/status")
    print_json(result)
```

## Best Practices

### Command Structure

Follow these best practices for command structure:

1. **Consistent Naming**: Use verb-noun format (e.g., `list-tools`, `get-config`)
2. **Logical Grouping**: Group related commands into appropriate command groups
3. **Clear Help Text**: Provide clear help messages for commands and options
4. **Consistent Options**: Use similar option names across commands (e.g., `--force`, `--verbose`)

### Output Formatting

Use the formatting utilities for consistent output:

1. **Tables**: Use Rich tables for tabular data
2. **Color**: Use consistent colors for status indicators (green for success, etc.)
3. **JSON**: Offer JSON output option for machine-readable results

### Error Handling

Follow these guidelines for error handling:

1. **Informative Errors**: Provide clear error messages
2. **Exit Codes**: Use appropriate exit codes for different error types
3. **Graceful Failures**: Handle API connection errors gracefully

## Testing Commands

Run individual commands for testing:

```bash
# Install package in development mode
pip install -e .

# Run specific command
mcp-cli example hello "Test User"

# With debug output
MCP_HUB_LOG_LEVEL=DEBUG mcp-cli example hello "Test User"
```

## Documenting Commands

Update documentation when adding new commands:

1. Add to the CLI's help text
2. Update the `cli_examples.md` file with usage examples
3. Update this development guide if necessary
