# Milestone 1.5: CLI Foundation

This milestone implements the Command Line Interface (CLI) for the MCP Connection Hub, providing administrators with a powerful tool for system management.

## Overview

The CLI follows design principles similar to the Docker CLI, providing a single binary with multiple commands:

- **Single Binary, Multiple Commands**: One CLI tool with various subcommands for different operations
- **Command Structure**: `mcp-cli [global-options] command [command-options]`

## Features Implemented

1. **CLI Framework with Command Structure**
   - Main command groups: `tool`, `config`, `system`, `job`, `user`
   - Global options for verbosity and configuration file
   - Consistent command structure and help documentation
   - Rich formatting for tables, progress bars, and JSON output

2. **Tool Management Commands**
   - `mcp-cli tool list`: List all available tools
   - `mcp-cli tool enable <n>`: Enable a tool
   - `mcp-cli tool disable <n>`: Disable a tool
   - `mcp-cli tool info <n>`: Show detailed information about a tool
   - `mcp-cli tool configure <n>`: Configure a tool's parameters

3. **Configuration Viewing and Editing**
   - `mcp-cli config get [path]`: Get configuration values
   - `mcp-cli config set <path> <value>`: Set configuration values
   - `mcp-cli config import <file>`: Import configuration from file
   - `mcp-cli config export <file>`: Export configuration to file

4. **System Status Commands**
   - `mcp-cli system status`: Show detailed system status
   - `mcp-cli system restart`: Restart the system
   - `mcp-cli system backup`: Backup system data
   - `mcp-cli system restore <file>`: Restore system from backup
   - `mcp-cli system logs`: View system logs
   - `mcp-cli system health`: Run system health check
   
5. **Job Management Commands** (for future implementation)
   - `mcp-cli job list`: List all jobs
   - `mcp-cli job status <id>`: Check specific job status
   - `mcp-cli job cancel <id>`: Cancel a running job
   - `mcp-cli job purge`: Purge old jobs
   - `mcp-cli job results <id>`: Get job results

6. **User Management Commands** (for future implementation)
   - `mcp-cli user list`: List all users
   - `mcp-cli user add <n>`: Add a new user
   - `mcp-cli user remove <n>`: Remove a user
   - `mcp-cli user update <n>`: Update a user's properties
   - `mcp-cli user key-list`: List API keys
   - `mcp-cli user key-create <n>`: Create a new API key
   - `mcp-cli user key-revoke <id>`: Revoke an API key

## Implementation Details

### Technologies Used

- **Typer**: For creating the CLI framework with commands and options
- **Rich**: For formatted output with tables, progress bars, and colors
- **Python Entry Points**: For making the CLI available as a system command

### Architecture

The CLI follows a modular architecture:

- **Main CLI Application**: Defines global options and assembles command groups
- **Command Modules**: Separate modules for each command category
- **Utility Modules**: Shared functionality for formatting, configuration, and API connection

### Installation

The CLI can be installed in multiple ways:

1. **Inside Docker Container**: Automatically installed during container build
2. **Development Mode**: Installed with `pip install -e .`
3. **Host Installation Script**: Wrapper that forwards commands to the Docker container

## Usage

To use the CLI, run:

```bash
./mcp-cli [command] [options]
```

For example:

```bash
# Show help
./mcp-cli --help

# List all tools
./mcp-cli tool list

# Show system status
./mcp-cli system status

# View configuration
./mcp-cli config get
```

## Documentation

Comprehensive documentation has been created:

- **CLI Usage Examples**: Examples of common CLI commands and workflows
- **Development Guide**: Instructions for extending the CLI with new commands
- **Command Help**: Built-in help text for all commands and options

## Future Enhancements

- Connect CLI commands to actual system functionality once implemented
- Implement proper API client for communicating with the backend
- Add support for authentication token management
- Add interactive mode for complex operations
- Implement autocomplete for command parameters
