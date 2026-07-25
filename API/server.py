from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class NovaServer(BaseHTTPRequestHandler):

    def do_GET(self):
        response = {
            "status": "online",
            "message": "Nova Core funcionando"
        }

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        self.wfile.write(json.dumps(response).encode())


server = HTTPServer(("0.0.0.0", 8080), NovaServer)

print("Nova API iniciada")

server.serve_forever()
