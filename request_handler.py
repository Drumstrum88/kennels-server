from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_animals
import json

class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def _set_headers(self, status):
        """Sets the status code, Content-Type, and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        """Handles GET requests to the server
        """
        # Set the response code to 'Ok'
        self._set_headers(200)

        # Your new console.log() that outputs to the terminal
        print(self.path)

        # It's an if..else statement
        if self.path == "/animals":
            response = get_all_animals()
        else:
            response = []

        # Convert the response to JSON
        response_json = json.dumps(response)

        # Send the JSON response back to the client
        self.wfile.write(response_json.encode())

    def do_POST(self):
        """Handles POST requests to the server
        """
        # Set response code to 'Created'
        self._set_headers(201)

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        response = {"message": f"received post request: {post_body}"}

        # Convert the response to JSON
        response_json = json.dumps(response)

        # Send the JSON response back to the client
        self.wfile.write(response_json.encode())

    def do_PUT(self):
        """Handles PUT requests to the server
        """
        self.do_POST()

def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()

