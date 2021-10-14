import http.server
import socketserver

port = 8080
hostname='fibonacci.com'
ip= '127.0.0.1'
as_ip='127.0.0.1'
as_port='9090'

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", port), handler) as httpd:
    print("Server started at localhost:" + str(port))
    httpd.serve_forever()
