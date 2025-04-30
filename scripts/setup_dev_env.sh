#!/bin/bash
# MCP Connection Hub Development Environment Setup

# Set script to exit on error
set -e

echo "=== Setting up MCP Connection Hub Development Environment ==="
echo

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python -m venv venv
    echo "Virtual environment created at ./venv"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# Install package in development mode
echo "Installing package in development mode..."
pip install -e .

# Make CLI script executable
echo "Making CLI script executable..."
chmod +x mcp-cli

# Create symbolic link to mcp-cli in a PATH directory if requested
if [ "$1" == "--link" ]; then
    LINK_DIR="$HOME/.local/bin"
    
    # Create directory if it doesn't exist
    if [ ! -d "$LINK_DIR" ]; then
        echo "Creating directory $LINK_DIR..."
        mkdir -p "$LINK_DIR"
    fi
    
    # Create symbolic link
    echo "Creating symbolic link in $LINK_DIR..."
    ln -sf "$(pwd)/mcp-cli" "$LINK_DIR/mcp-cli"
    
    # Check if directory is in PATH
    if [[ ":$PATH:" != *":$LINK_DIR:"* ]]; then
        echo "Adding $LINK_DIR to PATH in .bashrc"
        echo "export PATH=\"\$PATH:$LINK_DIR\"" >> "$HOME/.bashrc"
        echo "Please restart your shell or run 'source ~/.bashrc' to update your PATH"
    fi
fi

echo
echo "=== Development Environment Setup Complete ==="
echo
echo "To run the CLI directly:"
echo "  ./mcp-cli [command] [options]"
echo
echo "To activate the virtual environment in the future:"
echo "  source venv/bin/activate"
echo
echo "For usage examples, see: docs/cli_examples.md"
