from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class RequestHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_response()

        # Leggi il contenuto del file JSON locale
        with open('a.json', 'r') as file:
            response = json.load(file)

        self.wfile.write(json.dumps(response).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        self._set_response()

        # Leggi il contenuto del file JSON locale
        with open('a.json', 'r') as file:
            response = json.load(file)

        response['data_received'] = json.loads(post_data)
        self.wfile.write(json.dumps(response).encode('utf-8'))

host = 'localhost'
port = 47512

server = HTTPServer((host, port), RequestHandler)
print(f'Server in esecuzione su http://{host}:{port}')

server.serve_forever()

