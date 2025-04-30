"""
Formatting utilities for the CLI.

This module provides helpers for formatting CLI output.
"""

from typing import Dict, List, Any, Union
from rich.console import Console
from rich.table import Table
from rich.syntax import Syntax
import json

console = Console()

def format_json(data: Union[Dict, List]) -> Syntax:
    """
    Format data as syntax-highlighted JSON.
    
    Args:
        data: Data to format as JSON
        
    Returns:
        Rich Syntax object for printing
    """
    json_str = json.dumps(data, indent=2)
    return Syntax(json_str, "json", theme="monokai", line_numbers=True)

def print_json(data: Union[Dict, List]):
    """
    Print data as syntax-highlighted JSON.
    
    Args:
        data: Data to print as JSON
    """
    console.print(format_json(data))

def create_status_table(title: str, data: Dict[str, Dict[str, str]]) -> Table:
    """
    Create a Rich table for status information.
    
    Args:
        title: Title for the table
        data: Dictionary mapping row names to dictionaries of column values
        
    Returns:
        Rich Table object
    """
    table = Table(title=title)
    
    # Add columns
    columns = set()
    for row_data in data.values():
        columns.update(row_data.keys())
    
    for column in ["Component"] + sorted(columns):
        style = "cyan" if column == "Component" else "green"
        table.add_column(column, style=style)
    
    # Add rows
    for component, row_data in data.items():
        values = [component]
        for column in sorted(columns):
            values.append(row_data.get(column, ""))
        table.add_row(*values)
    
    return table

def format_key_value(data: Dict[str, Any], title: str = None) -> Table:
    """
    Format a dictionary as a key-value table.
    
    Args:
        data: Dictionary to format
        title: Optional title for the table
        
    Returns:
        Rich Table object
    """
    table = Table(title=title)
    table.add_column("Key", style="cyan")
    table.add_column("Value", style="green")
    
    for key, value in data.items():
        if isinstance(value, (dict, list)):
            value = json.dumps(value)
        elif not isinstance(value, str):
            value = str(value)
        
        table.add_row(key, value)
    
    return table
