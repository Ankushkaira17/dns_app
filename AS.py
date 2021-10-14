import http.server
import socketserver

port=9090
ip='172.0.0.2'
hostname='fibonacci.com'
as_ip= '172.0.0.2'
as_port=8080


handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", port), handler) as httpd:
    print("Server started at localhost:" + str(port))
    httpd.serve_forever()
