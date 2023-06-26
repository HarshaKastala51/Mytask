import http.server
import socketserver
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, World!')
PORT = 80
handler = socketserver.TCPServer(('', PORT), MyHandler)

print(f'Server running on port {PORT}')
handler.serve_forever()
