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
print("    Importing libs.")
import textwrap
from six.moves.BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urllib.request import urlopen
import certifi
import json
from json2html import *
print("    Libs imported successfully.")
print("    Class HelloRequestHandler starting.")

class HelloRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        print("        do_GET(self) starting.")

        def get_jsonparsed_data(url):
            print("        get_jsonparsed_data(url) starting.")
            response = urlopen(url, cafile=certifi.where())
            data = response.read().decode("utf-8")
            print("        get_jsonparsed_data(url) completed.")
            return json.loads(data)

        def get_findata_fromAPI():
            print("        Getting FMP url.")
            url = ("https://financialmodelingprep.com/api/v3/quote-short/VMW?apikey=a6019491e15dbeaaeb41242ad459a370")
            print("        url: "+url)
            print("        Getting stock info.")
            stockinfo = get_jsonparsed_data(url)
            print("        Stock Info obtained.")
            return stockinfo

        def convert_findata_toHTML(stockinfo):        
            print("        Converting stockinfo to table.")
            stockinfoTableHTML = (json2html.convert(json = stockinfo))
            print("        stockinfoTableHTML: "+stockinfoTableHTML)
            return stockinfoTableHTML

        def compile_finalHTML(stockinfoTableHTML):
            print("        Compiling final HTML.")
            html1 = ('''\
            <html>
            <head>
            <title>Options Tracker App Version 1.0</title>
            </head>
            <body>
            <h1>Options Trader Application</h1>
            ''')
            html2 = ('''\
            </body>
            </html> 
            ''')
            htmlFinal = html1+stockinfoTableHTML+html2
            print("        Final HTML compiled: ")
            print("* * * * * * * * * * * * * * * * * * * ")
            print("")
            print(htmlFinal)
            print("")
            print("* * * * * * * * * * * * * * * * * * * ")
            print("")
            print("        Starting textwrap.")
            response_text = textwrap.dedent(htmlFinal)
            print("        Textwrap completed.")
            return response_text

        if self.path != '/':
            self.send_error(404, "Object not found")
            return
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        stockinfo = get_findata_fromAPI()
        stockinfoTableHTML = convert_findata_toHTML(stockinfo)
        response_text = compile_finalHTML(stockinfoTableHTML)
        self.wfile.write(response_text.encode('utf-8'))
 
    
server_address = ('', 8000)
print("    Starting Web Server on port 8000!")
httpd = HTTPServer(server_address, HelloRequestHandler)
httpd.serve_forever()
