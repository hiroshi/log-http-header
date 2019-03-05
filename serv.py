#!/usr/bin/env python
# https://gist.github.com/phrawzty/62540f146ee5e74ea1ab#gistcomment-2358615
import SimpleHTTPServer
import SocketServer
import os

PORT = int(os.environ.get('PORT', 8000))

class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_head()
        for h in self.headers:
            self.send_header(h, self.headers[h])
        self.end_headers()
        self.send_response(200, "")


Handler = GetHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

httpd.serve_forever()
