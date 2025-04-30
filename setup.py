from setuptools import setup, find_packages

setup(
    name="mcp-connection-hub",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "fastapi>=0.95.0",
        "uvicorn>=0.21.1",
        "pydantic>=2.0.0",
        "sqlalchemy>=2.0.0",
        "alembic>=1.10.0",
        "pluggy>=1.0.0",
        "loguru>=0.6.0",
        "python-dotenv>=1.0.0",
        "typer>=0.9.0",
        "rich>=13.0.0",
    ],
    entry_points={
        "console_scripts": [
            "mcp-cli=app.cli.entry:main",
        ],
    },
)
