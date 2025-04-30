#!/bin/bash
# Make scripts executable

# Make CLI executable
chmod +x mcp-cli
echo "Made mcp-cli executable"

# Make test script executable
chmod +x scripts/test_cli.sh
echo "Made test_cli.sh executable"

# Make install script executable
chmod +x scripts/install_cli.sh
echo "Made install_cli.sh executable"

# Make dev environment script executable
chmod +x scripts/setup_dev_env.sh
echo "Made setup_dev_env.sh executable"

echo "All scripts are now executable"
