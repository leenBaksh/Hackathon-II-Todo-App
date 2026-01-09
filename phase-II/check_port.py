import socket

def check_port(host, port):
    """Check if a port is open on a given host"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)  # 5 second timeout
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except Exception as e:
        print(f"Error checking port: {e}")
        return False

if __name__ == "__main__":
    print("Checking if server is running on 127.0.0.1:8000...")
    if check_port("127.0.0.1", 8000):
        print("✓ Port 8000 is open and accessible")
    else:
        print("✗ Port 8000 is not accessible")

    print("\nChecking if server is running on localhost:8000...")
    if check_port("localhost", 8000):
        print("✓ Port 8000 is open and accessible via localhost")
    else:
        print("✗ Port 8000 is not accessible via localhost")

    print("\nChecking if server is running on 127.0.0.1:8001...")
    if check_port("127.0.0.1", 8001):
        print("✓ Port 8001 is open and accessible")
    else:
        print("✗ Port 8001 is not accessible")

    print("\nChecking if server is running on localhost:8001...")
    if check_port("localhost", 8001):
        print("✓ Port 8001 is open and accessible via localhost")
    else:
        print("✗ Port 8001 is not accessible via localhost")