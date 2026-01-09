import sys
import os
import logging

# Set up logging to see what's happening
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    # Add the backend directory to the Python path
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    
    # Import the app to check for import errors
    from app.main import app
    logger.info("Successfully imported the app")
    
    # Import the database to check for database errors
    from app.core.db import engine, SQLModel
    logger.info("Successfully imported database components")
    
    # Try to create tables
    SQLModel.metadata.create_all(bind=engine)
    logger.info("Successfully created database tables")
    
    # Import models
    from app.models.user import User
    from app.models.task import Task
    logger.info("Successfully imported models")
    
    print("All imports successful. The backend should work correctly.")
    
except Exception as e:
    logger.error(f"Error during import: {e}")
    import traceback
    traceback.print_exc()