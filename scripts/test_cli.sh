#!/bin/bash
# MCP Connection Hub CLI Test Script

# Set script to exit on error
set -e

# Color output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}=== MCP Connection Hub CLI Test ===${NC}"
echo

# Make sure CLI is executable
chmod +x mcp-cli

# Test basic commands
echo -e "${YELLOW}Testing basic commands:${NC}"
echo

echo -e "${GREEN}Version command:${NC}"
./mcp-cli version
echo

echo -e "${GREEN}Help command:${NC}"
./mcp-cli --help
echo

# Test tool commands
echo -e "${YELLOW}Testing tool commands:${NC}"
echo

echo -e "${GREEN}List tools:${NC}"
./mcp-cli tool list
echo

echo -e "${GREEN}Tool info:${NC}"
./mcp-cli tool info brave_web_search
echo

# Test config commands
echo -e "${YELLOW}Testing config commands:${NC}"
echo

echo -e "${GREEN}Get config:${NC}"
./mcp-cli config get
echo

# Test system commands
echo -e "${YELLOW}Testing system commands:${NC}"
echo

echo -e "${GREEN}System status:${NC}"
./mcp-cli system status
echo

echo -e "${GREEN}System health:${NC}"
./mcp-cli system health
echo

# Test job commands
echo -e "${YELLOW}Testing job commands:${NC}"
echo

echo -e "${GREEN}List jobs:${NC}"
./mcp-cli job list
echo

# Test user commands
echo -e "${YELLOW}Testing user commands:${NC}"
echo

echo -e "${GREEN}List users:${NC}"
./mcp-cli user list
echo

echo -e "${YELLOW}All tests completed successfully!${NC}"
