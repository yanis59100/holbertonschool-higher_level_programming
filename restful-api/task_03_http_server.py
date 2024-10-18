#!/usr/bin/python3
import http.server
import socketserver
import json

PORT = 8000


class serveur(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            json_string = '{"name": "John", "age": 30, "city": "New York"}'
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(json_string).encode())
        elif self.path == '/status':
            self.send_response(200)
            json_string = "404 Not Found status"
            self.wfile.write(json.dumps(json_string).encode())
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(json_string).encode())
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            json_strings = '{"version": "1.0","description": "A simple API built with http.server"}'
            self.wfile.write(json.dumps(json_strings).encode())
        else:
            self.send_error(404)
            self.wfile.write(b"404")


with socketserver.TCPServer(("", PORT), serveur) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
