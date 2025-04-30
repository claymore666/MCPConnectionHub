## Job Management

### Listing and Checking Jobs

```bash
# List all jobs
./mcp-cli job list

# List only running jobs
./mcp-cli job list --status running

# List all jobs (override default limit)
./mcp-cli job list --all

# Check specific job status
./mcp-cli job status job_001

# Get job results
./mcp-cli job results job_001

# Get job results in JSON format
./mcp-cli job results job_001 --format json

# Export job results to file
./mcp-cli job results job_001 --format json --output results.json
```

### Managing Jobs

```bash
# Cancel a running job
./mcp-cli job cancel job_001

# Force cancel without confirmation
./mcp-cli job cancel job_001 --force

# Purge completed jobs older than 7 days
./mcp-cli job purge

# Purge failed jobs older than 24 hours
./mcp-cli job purge --status failed --older-than 24h

# Purge all jobs without confirmation
./mcp-cli job purge --status all --force
```

## User Management

### Listing and Managing Users

```bash
# List all users
./mcp-cli user list

# Add a new user
./mcp-cli user add api-client

# Add admin user without API key
./mcp-cli user add admin-user --role admin --no-create-key

# Update user role
./mcp-cli user update api-client --role admin

# Remove a user
./mcp-cli user remove api-client

# Force remove without confirmation
./mcp-cli user remove api-client --force
```

### Managing API Keys

```bash
# List all API keys
./mcp-cli user key-list

# List API keys for specific user
./mcp-cli user key-list api-client

# Create a new API key
./mcp-cli user key-create "Deployment Key" --user api-client

# Revoke an API key
./mcp-cli user key-revoke 2

# Force revoke without confirmation
./mcp-cli user key-revoke 2 --force
```

# MCP Connection Hub CLI Examples

This document provides examples of how to use the MCP Connection Hub CLI for common administrative tasks.

## Basic Commands

### Getting Help

```bash
# Show main help
./mcp-cli --help

# Show help for a specific command
./mcp-cli tool --help
./mcp-cli config --help
./mcp-cli system --help

# Show help for a specific subcommand
./mcp-cli tool list --help
```

### Checking System Status

```bash
# Show system version
./mcp-cli version

# Show basic status
./mcp-cli status

# Show detailed system status
./mcp-cli system status

# Run system health check
./mcp-cli system health
```

## Tool Management

### Listing and Inspecting Tools

```bash
# List all tools
./mcp-cli tool list

# Show detailed tool list
./mcp-cli tool list --verbose

# Get detailed information about a specific tool
./mcp-cli tool info brave_web_search
```

### Managing Tools

```bash
# Enable a tool
./mcp-cli tool enable brave_web_search

# Disable a tool
./mcp-cli tool disable brave_web_search

# Configure a tool
./mcp-cli tool configure brave_web_search --param max_results --value 5
```

## Configuration Management

### Viewing Configuration

```bash
# Show all configuration
./mcp-cli config get

# Show specific configuration path
./mcp-cli config get api.port
./mcp-cli config get database.url
```

### Modifying Configuration

```bash
# Set configuration value
./mcp-cli config set api.port 9000
./mcp-cli config set database.url "sqlite:////data/db/custom.db"

# Import configuration from file
./mcp-cli config import my_config.json

# Export configuration to file
./mcp-cli config export backup_config.json
```

## System Operations

### Log Management

```bash
# View recent logs
./mcp-cli system logs

# View more log lines
./mcp-cli system logs --lines 50

# View only warnings and errors
./mcp-cli system logs --level WARNING

# Follow logs in real-time
./mcp-cli system logs --follow
```

### Backup and Restore

```bash
# Create system backup
./mcp-cli system backup

# Create backup with custom filename
./mcp-cli system backup --output /data/backups/mcp_backup_20230601.zip

# Restore from backup
./mcp-cli system restore /data/backups/mcp_backup_20230601.zip

# Force restore without confirmation
./mcp-cli system restore /data/backups/mcp_backup_20230601.zip --force
```

### System Control

```bash
# Restart the system
./mcp-cli system restart

# Force restart without confirmation
./mcp-cli system restart --force
```

## Advanced Usage

### Using with Docker

```bash
# Run CLI commands inside the Docker container
docker exec mcp-connection-hub mcp-cli status
docker exec mcp-connection-hub mcp-cli tool list
docker exec mcp-connection-hub mcp-cli system health
```

### Using with Configuration File

```bash
# Specify custom configuration file
./mcp-cli --config /path/to/custom/config.ini status

# With verbose output
./mcp-cli --verbose --config /path/to/custom/config.ini tool list
```

## Job Management

### Listing and Checking Jobs

```bash
# List all jobs
./mcp-cli job list

# List only running jobs
./mcp-cli job list --status running

# List all jobs (override default limit)
./mcp-cli job list --all

# Check specific job status
./mcp-cli job status job_001

# Get job results
./mcp-cli job results job_001

# Get job results in JSON format
./mcp-cli job results job_001 --format json

# Export job results to file
./mcp-cli job results job_001 --format json --output results.json
```

### Managing Jobs

```bash
# Cancel a running job
./mcp-cli job cancel job_001

# Force cancel without confirmation
./mcp-cli job cancel job_001 --force

# Purge completed jobs older than 7 days
./mcp-cli job purge

# Purge failed jobs older than 24 hours
./mcp-cli job purge --status failed --older-than 24h

# Purge all jobs without confirmation
./mcp-cli job purge --status all --force
```

## User Management

### Listing and Managing Users

```bash
# List all users
./mcp-cli user list

# Add a new user
./mcp-cli user add api-client

# Add admin user without API key
./mcp-cli user add admin-user --role admin --no-create-key

# Update user role
./mcp-cli user update api-client --role admin

# Remove a user
./mcp-cli user remove api-client

# Force remove without confirmation
./mcp-cli user remove api-client --force
```

### Managing API Keys

```bash
# List all API keys
./mcp-cli user key-list

# List API keys for specific user
./mcp-cli user key-list api-client

# Create a new API key
./mcp-cli user key-create "Deployment Key" --user api-client

# Revoke an API key
./mcp-cli user key-revoke 2

# Force revoke without confirmation
./mcp-cli user key-revoke 2 --force
```
