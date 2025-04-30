#!/bin/bash
# MCP Connection Hub CLI Installation Script

# Set script to exit on error
set -e

echo "=== MCP Connection Hub CLI Installation ==="
echo

# Check if running in a Docker environment
if [ -f /.dockerenv ]; then
    echo "Running in Docker environment..."
    # Install the CLI within the container
    cd /app
    pip install -e .
    echo "CLI installed successfully as 'mcp-cli'"
else
    # For host installation
    echo "Installing MCP CLI on host system..."
    
    # Determine installation directory
    if [ -z "$1" ]; then
        INSTALL_DIR="$HOME/.local/bin"
    else
        INSTALL_DIR="$1"
    fi
    
    # Check if installation directory exists
    if [ ! -d "$INSTALL_DIR" ]; then
        echo "Creating installation directory: $INSTALL_DIR"
        mkdir -p "$INSTALL_DIR"
    fi
    
    # Create CLI script
    CLI_PATH="$INSTALL_DIR/mcp-cli"
    echo "Creating CLI script at $CLI_PATH"
    
    cat > "$CLI_PATH" << 'EOF'
#!/bin/bash
# MCP Connection Hub CLI wrapper

# This script forwards commands to the CLI inside the Docker container
CONTAINER_NAME="mcp-connection-hub"

if ! docker ps -q --filter "name=$CONTAINER_NAME" | grep -q .; then
    echo "Error: MCP Connection Hub container not running."
    echo "Start the container with: docker-compose up -d"
    exit 1
fi

# Forward all arguments to the CLI inside the container
docker exec "$CONTAINER_NAME" mcp-cli "$@"
EOF
    
    # Make script executable
    chmod +x "$CLI_PATH"
    
    # Add to PATH if needed
    if [[ ":$PATH:" != *":$INSTALL_DIR:"* ]]; then
        echo "Adding $INSTALL_DIR to PATH in .bashrc"
        echo "export PATH=\"\$PATH:$INSTALL_DIR\"" >> "$HOME/.bashrc"
        echo "Please restart your shell or run 'source ~/.bashrc' to update your PATH"
    fi
    
    echo "CLI installed successfully as 'mcp-cli'"
    echo "You may need to restart your terminal or run 'source ~/.bashrc'"
fi

# Test the CLI
echo
echo "Testing CLI installation..."
if command -v mcp-cli >/dev/null 2>&1; then
    echo "CLI command found. Checking version:"
    mcp-cli version || echo "CLI command found but execution failed."
else
    echo "CLI command not found in PATH. Please check installation."
fi

echo
echo "=== Installation Complete ==="
echo "For usage examples, see: docs/cli_examples.md"
