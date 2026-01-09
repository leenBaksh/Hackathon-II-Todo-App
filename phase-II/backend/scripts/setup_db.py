#!/usr/bin/env python
"""
Database setup script for the Todo application.
This script initializes the database tables based on the defined models.
"""

import asyncio
import sys
import os

# Add the backend directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from alembic.config import Config
from alembic import command
from app.core.db import create_db_and_tables


def setup_database():
    """Set up the database by creating all tables."""
    print("Setting up the database...")

    try:
        # Create all tables defined in the models
        create_db_and_tables()
        print("Database tables created successfully!")

        # Also run Alembic migrations to ensure everything is up to date
        alembic_cfg = Config("alembic.ini")
        command.upgrade(alembic_cfg, "head")
        print("Alembic migrations applied successfully!")

        return True
    except Exception as e:
        print(f"Error setting up database: {e}")
        return False


if __name__ == "__main__":
    success = setup_database()
    if not success:
        sys.exit(1)
    print("Database setup completed successfully!")