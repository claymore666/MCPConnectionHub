# MCP Connection Hub CLI

The Command Line Interface (CLI) for MCP Connection Hub provides administrators with a powerful tool for system management.

## Architecture

The CLI is built using Typer and Rich libraries, with a modular structure:

- **main.py**: Entry point and global options
- **commands/**: Command modules for each category
  - **tool.py**: Tool management commands
  - **config.py**: Configuration viewing and editing
  - **system.py**: System status and management commands

## Command Structure

The CLI follows a consistent command structure:

```
mcp-cli [global-options] command [command-options]
```

Global options:
- `--verbose, -v`: Enable verbose output
- `--config, -c`: Path to config file

## Available Commands

### Tool Management

- `mcp-cli tool list`: List all available tools
- `mcp-cli tool enable <name>`: Enable a tool
- `mcp-cli tool disable <name>`: Disable a tool
- `mcp-cli tool info <name>`: Show detailed information about a tool
- `mcp-cli tool configure <name>`: Configure a tool's parameters

### Configuration

- `mcp-cli config get [path]`: Get configuration values
- `mcp-cli config set <path> <value>`: Set configuration values
- `mcp-cli config import <file>`: Import configuration from file
- `mcp-cli config export <file>`: Export configuration to file

### System Management

- `mcp-cli system status`: Show detailed system status
- `mcp-cli system restart`: Restart the system
- `mcp-cli system backup`: Backup system data
- `mcp-cli system restore <file>`: Restore system from backup
- `mcp-cli system logs`: View system logs
- `mcp-cli system health`: Run system health check

## Development

To add new commands:

1. Create a new module in the `commands` directory
2. Define a Typer app for the command group
3. Add commands using the `@app.command()` decorator
4. Import and add the command group in `main.py`

Example:

```python
import typer
from rich.console import Console

app = typer.Typer(name="example", help="Example commands")
console = Console()

@app.command("demo")
def demo_command():
    """Demo command."""
    console.print("[green]Demo command executed[/green]")
```

Then in `main.py`:

```python
from app.cli.commands import example
app.add_typer(example.app, name="example", help="Example commands")
```

## Installation

The CLI is automatically installed when the MCP Connection Hub package is installed:

```bash
pip install -e .
```

This makes the `mcp-cli` command available in the environment.
