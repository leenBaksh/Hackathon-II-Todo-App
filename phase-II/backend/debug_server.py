import sys
import os
import socket
import threading
import time

# Add the backend directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.main import app
import uvicorn

def check_port():
    """Check if port 8000 is available"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', 8000))
    sock.close()
    return result == 0  # 0 means the port is open and connectable

def start_server():
    """Start the uvicorn server in a separate thread"""
    config = uvicorn.Config(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        log_level="info"
    )
    server = uvicorn.Server(config)
    server.run()

if __name__ == "__main__":
    print("Checking if port 8000 is available...")
    
    # Try to start the server in a thread
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    
    # Wait a bit for the server to start
    time.sleep(3)
    
    if check_port():
        print("✓ Server appears to be running on port 8000")
        print("You should be able to access it at http://localhost:8000")
    else:
        print("✗ Server does not appear to be running on port 8000")
    
    # Keep the main thread alive to see if there are any error messages
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping server...")