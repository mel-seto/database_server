from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json

# In-memory key-value store
store = {}

class SimpleKVHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query_params = parse_qs(parsed_url.query)

        if path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"Hello World")
        elif path == '/set':
            self.handle_set(query_params)
        elif path == '/get':
            self.handle_get(query_params)
        else:
            self.send_error(404, "Not Found")

    def handle_set(self, query_params):
        if not query_params:
            self.send_error(400, "No query parameters provided")
            return

        # Assume exactly one key-value pair
        key, value_list = next(iter(query_params.items()))
        value = value_list[0]
        store[key] = value

        self.respond_json({
            "message": "Stored successfully",
            "key": key,
            "value": value
        })

    def handle_get(self, query_params):
        key_list = query_params.get('key')
        if not key_list:
            self.send_error(400, "Missing 'key' parameter")
            return

        key = key_list[0]
        if key not in store:
            self.send_error(404, f"Key '{key}' not found")
            return

        self.respond_json({
            "key": key,
            "value": store[key]
        })

    def respond_json(self, data_dict):
        response = json.dumps(data_dict).encode()
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(response)))
        self.end_headers()
        self.wfile.write(response)

def run_server():
    server_address = ('', 4000)
    httpd = HTTPServer(server_address, SimpleKVHandler)
    print("Server running on http://localhost:4000 ...")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
