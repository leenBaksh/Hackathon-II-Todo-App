import http.server
import socketserver
import threading
import time

PORT = 8001

class TestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Test server is running!")

def start_test_server():
    with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
        print(f"Test server running on port {PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    # Start server in a thread
    server_thread = threading.Thread(target=start_test_server, daemon=True)
    server_thread.start()
    
    print(f"Test server started on http://127.0.0.1:{PORT}")
    print("Waiting for connections...")
    
    try:
        # Keep the main thread alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down test server...")
