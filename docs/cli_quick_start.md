# MCP Connection Hub CLI Quick Start Guide

This guide provides instructions for getting started with the MCP Connection Hub CLI.

## Installation Options

There are multiple ways to install and use the CLI:

### 1. Docker Container (Recommended)

The CLI is automatically installed inside the Docker container:

```bash
# Start the container
docker-compose up -d

# Run CLI commands inside the container
docker exec mcp-connection-hub mcp-cli --help
```

### 2. Host Installation

You can install a wrapper script on the host that forwards commands to the container:

```bash
# Run the installation script
./scripts/install_cli.sh

# Use the CLI directly
mcp-cli --help
```

### 3. Development Mode

For development, you can set up a Python environment:

```bash
# Set up development environment
./scripts/setup_dev_env.sh

# Run CLI directly
./mcp-cli --help
```

## Basic Usage

Once installed, you can use the CLI with the following commands:

```bash
# Show version
mcp-cli version

# Show help for all commands
mcp-cli --help

# Show help for a specific command
mcp-cli tool --help
```

## Command Groups

The CLI provides several command groups:

1. **Tool Management**: `mcp-cli tool [command]`
2. **Configuration**: `mcp-cli config [command]`
3. **System Operations**: `mcp-cli system [command]`
4. **Job Management**: `mcp-cli job [command]`
5. **User Management**: `mcp-cli user [command]`

## Testing the CLI

You can test all CLI commands using the test script:

```bash
# Make sure scripts are executable
./make_scripts_executable.sh

# Run the test script
./scripts/test_cli.sh
```

The test script will run through all major CLI commands to verify functionality.

## Example Commands

### Tool Management

```bash
# List all tools
mcp-cli tool list

# Get information about a specific tool
mcp-cli tool info brave_web_search

# Enable a tool
mcp-cli tool enable brave_web_search

# Configure a tool
mcp-cli tool configure brave_web_search --param timeout --value 20
```

### Configuration

```bash
# View all configuration
mcp-cli config get

# View specific configuration value
mcp-cli config get database.url

# Set configuration value
mcp-cli config set api.port 9000
```

### System Management

```bash
# View system status
mcp-cli system status

# Run health check
mcp-cli system health

# View logs
mcp-cli system logs
```

## Further Reading

For more detailed information, see:

- [CLI Examples](cli_examples.md): Comprehensive examples of CLI usage
- [CLI Development Guide](cli_development.md): Guide for extending the CLI
- [Milestone 1.5 Documentation](milestone_1_5.md): Overview of the CLI implementation
