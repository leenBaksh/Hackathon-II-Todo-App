import sys
import os
import threading
import time
import requests

# Add the backend directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_connection():
    """Test if the server is responding"""
    time.sleep(5)  # Wait for server to start
    try:
        response = requests.get('http://127.0.0.1:8000')
        print(f"Connected successfully! Status: {response.status_code}")
        print(f"Response: {response.text[:200]}...")
    except requests.exceptions.ConnectionError:
        print("Could not connect to server - server may not be running")
    except Exception as e:
        print(f"Error connecting to server: {e}")

if __name__ == "__main__":
    # Start connection test in a separate thread
    test_thread = threading.Thread(target=test_connection)
    test_thread.start()
    
    # Start the server
    from app.main import app
    import uvicorn
    
    print("Starting server on 127.0.0.1:8000...")
    uvicorn.run(
        app, 
        host="127.0.0.1", 
        port=8000, 
        log_level="info",
        access_log=True
    )