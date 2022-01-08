#!/usr/bin/env python
# This is an open source project from the E2E lab.
# Code and documentation can be found at https://github.com/boconnor2017/e2e-k8-lab/tree/main/options-tracker-app
#
# Options Tracker App Version 1.0
# January 2022
# Author: Brendan O'Connor

print("*****************************************************")
print("*****************************************************")
print(" ")
print("Welcome to the Options Tracker App -- Version 1.0")
print(" ")
print("*****************************************************")
print("*****************************************************")
print(" ")
print("Starting Web Service... ")

import textwrap
from six.moves.BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class HelloRequestHandler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        if self.path != '/':
            self.send_error(404, "Object not found")
            return
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Options Tracker App Version 1.0</title>
            </head>
            <body>
                <h1>Options Trader Application</h1>
            </body>
            </html>
        ''')
        self.wfile.write(response_text.encode('utf-8'))
 
 
server_address = ('', 8000)
httpd = HTTPServer(server_address, HelloRequestHandler)
httpd.serve_forever()
