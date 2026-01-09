#!/usr/bin/env python
"""
Database verification script for the Todo application.
This script checks the health and status of the database connection and schema.
"""

import sys
import os
from datetime import datetime

# Add the backend directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from sqlalchemy import text
from backend.app.core.db import engine
from backend.app.models.user import User
from backend.app.models.task import Task


def verify_database():
    """Verify the database connection and schema."""
    print("Verifying database connection and schema...")
    
    try:
        # Test database connection
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("✓ Database connection successful")
        
        # Verify tables exist and count records
        from backend.app.core.db import get_session
        
        session_gen = get_session()
        session = next(session_gen)
        
        try:
            # Count users
            user_count = session.query(User).count()
            print(f"✓ Users table exists - {user_count} records")
            
            # Count tasks
            task_count = session.query(Task).count()
            print(f"✓ Tasks table exists - {task_count} records")
            
            # Verify foreign key relationships by checking if tasks have valid user references
            if task_count > 0:
                # Try to join to verify foreign key constraints
                join_result = session.query(Task).join(User).limit(1).first()
                if join_result:
                    print("✓ Foreign key relationships are working correctly")
                else:
                    # If no join results but tasks exist, check if they have valid user_ids
                    sample_task = session.query(Task).first()
                    if sample_task:
                        user_exists = session.query(User).filter(User.id == sample_task.user_id).first()
                        if user_exists:
                            print("✓ Foreign key relationships are working correctly")
                        else:
                            print("⚠ Warning: Task references non-existent user")
            
            print("Database verification completed successfully!")
            return True
            
        finally:
            session.close()
            
    except Exception as e:
        print(f"✗ Error verifying database: {e}")
        import traceback
        traceback.print_exc()
        return False


def check_environment():
    """Check environment configuration."""
    print("\nChecking environment configuration...")
    
    try:
        from backend.app.core.config import settings
        
        # Check if DATABASE_URL is set
        if settings.DATABASE_URL:
            print("✓ DATABASE_URL is configured")
        else:
            print("✗ DATABASE_URL is not configured")
            return False
            
        # Print project info
        print(f"✓ Project: {settings.PROJECT_NAME}")
        print(f"✓ API Version: {settings.API_V1_STR}")
        
        return True
        
    except Exception as e:
        print(f"✗ Error checking environment: {e}")
        return False


if __name__ == "__main__":
    env_ok = check_environment()
    if not env_ok:
        sys.exit(1)
    
    db_ok = verify_database()
    if not db_ok:
        sys.exit(1)
    
    print("\nAll checks passed! Database infrastructure is ready.")