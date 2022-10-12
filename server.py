import http.server

http.server.__path__ = ""
http.server.test(http.server.SimpleHTTPRequestHandler)