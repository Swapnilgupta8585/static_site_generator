import os
import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler

def run(
    server_class=HTTPServer,
    handler_class=SimpleHTTPRequestHandler,
    port=8888,
    directory=None,
):
    """
    Starts an HTTP server that serves files from a specified directory.
    
    Parameters:
    - server_class: The HTTP server class to use (default: HTTPServer).
    - handler_class: The request handler class to use (default: SimpleHTTPRequestHandler).
    - port: The port number to bind the server to (default: 8888).
    - directory: The directory from which to serve files (default: None, which uses the current working directory).
    """
    if directory:  # Change the current working directory if directory is specified
        os.chdir(directory)
    server_address = ("", port)  # Set server address with the specified port
    httpd = server_class(server_address, handler_class)  # Create an instance of the server
    print(f"Serving HTTP on http://localhost:{port} from directory '{directory}'...")
    httpd.serve_forever()  # Start the server and keep it running

if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="HTTP Server")
    
    # Add argument for directory
    parser.add_argument(
        "--dir", type=str, help="Directory to serve files from", default="."
    )
    
    # Add argument for port
    parser.add_argument("--port", type=int, help="Port to serve HTTP on", default=8888)
    
    # Parse command-line arguments
    args = parser.parse_args()

    # Run the server with the specified port and directory
    run(port=args.port, directory=args.dir)

