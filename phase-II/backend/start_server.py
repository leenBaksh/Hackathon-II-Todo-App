import sys
import os
import logging
import uvicorn

# Set up logging to see what's happening
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    # Add the backend directory to the Python path
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    
    # Import the app to check for import errors
    from app.main import app
    logger.info("Successfully imported the app")
    
    print("Starting server...")
    
    # Start the server
    if __name__ == "__main__":
        uvicorn.run(
            "app.main:app",
            host="127.0.0.1",
            port=8000,
            reload=False,  # Disable reload to see errors
            log_level="info"
        )
        
except Exception as e:
    logger.error(f"Error starting server: {e}")
    import traceback
    traceback.print_exc()
    input("Press Enter to continue...")