from http.server import HTTPServer , SimpleHTTPRequestHandler
import ssl

httpd = HTTPServer(('localhost',443),SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket()
