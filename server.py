import os,sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
PORT = int(os.environ.get('PORT', 8080))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
httpd = HTTPServer(('0.0.0.0', PORT), SimpleHTTPRequestHandler)
print(f'Serving on port {PORT}')
httpd.serve_forever()
