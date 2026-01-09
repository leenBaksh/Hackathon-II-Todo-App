#!/usr/bin/env python
"""
Database seeding script for the Todo application.
This script populates the database with sample user and task data.
"""

import asyncio
import sys
import os
from datetime import datetime
import uuid

# Add the backend directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from backend.app.core.db import get_session
from backend.app.models.user import User
from backend.app.models.task import Task


def seed_database():
    """Seed the database with sample data."""
    print("Seeding the database with sample data...")
    
    try:
        # Get a database session
        session_gen = get_session()
        session = next(session_gen)
        
        try:
            # Check if data already exists
            existing_users = session.query(User).count()
            if existing_users > 0:
                print("Database already has data, skipping seeding.")
                return True
            
            # Create sample users
            user1 = User(
                id=uuid.uuid4(),
                email="john.doe@example.com",
                first_name="John",
                last_name="Doe",
                hashed_password="hashed_password_123",  # In real app, use proper hashing
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
            
            user2 = User(
                id=uuid.uuid4(),
                email="jane.smith@example.com",
                first_name="Jane",
                last_name="Smith",
                hashed_password="hashed_password_456",  # In real app, use proper hashing
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
            
            session.add(user1)
            session.add(user2)
            session.commit()
            session.refresh(user1)
            session.refresh(user2)
            
            # Create sample tasks for user1
            task1 = Task(
                id=uuid.uuid4(),
                title="Complete project proposal",
                description="Write and submit the project proposal document",
                is_completed=False,
                user_id=user1.id,
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
            
            task2 = Task(
                id=uuid.uuid4(),
                title="Schedule team meeting",
                description="Arrange a meeting with the development team",
                is_completed=True,
                user_id=user1.id,
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
            
            # Create sample tasks for user2
            task3 = Task(
                id=uuid.uuid4(),
                title="Review code changes",
                description="Perform code review for PR #123",
                is_completed=False,
                user_id=user2.id,
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
            
            task4 = Task(
                id=uuid.uuid4(),
                title="Update documentation",
                description="Update API documentation with new endpoints",
                is_completed=False,
                user_id=user2.id,
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
            
            session.add(task1)
            session.add(task2)
            session.add(task3)
            session.add(task4)
            session.commit()
            
            print(f"Database seeded successfully with {session.query(User).count()} users and {session.query(Task).count()} tasks!")
            return True
            
        finally:
            session.close()
            
    except Exception as e:
        print(f"Error seeding database: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = seed_database()
    if not success:
        sys.exit(1)
    print("Database seeding completed successfully!")