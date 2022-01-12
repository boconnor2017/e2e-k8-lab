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
print(" ")
print(" ")
print(" ")

import textwrap
from six.moves.BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urllib.request import urlopen
import certifi
import json
from json2html import *
import os

def get_templateHTML():
    file1 = open("template.html", "r")
    template_html = []
    idx=0
    for line in file1.readlines():
        line_num = str(idx)
        template_html.insert(idx, line)
        print("Line Number "+line_num+": "+template_html[idx])
        idx=idx+1
    return template_html

def get_findata_fromAPI():
    url = ("https://financialmodelingprep.com/api/v3/quote-short/VMW?apikey=a6019491e15dbeaaeb41242ad459a370")
    print("url: "+url)
    print("stockinfo: ")
    stockinfo = get_jsonparsed_data(url)
    print(stockinfo)
    return stockinfo

def get_jsonparsed_data(url):
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    jsonparsed_data = json.loads(data)
    print(jsonparsed_data)
    return jsonparsed_data

def convert_findata_toHTML(stockinfo):        
    stockinfoTableHTML = (json2html.convert(json = stockinfo))
    print(stockinfoTableHTML)
    return stockinfoTableHTML

def compile_finalHTML(template_html, stockinfoTableHTML):
    n=0
    htmlFinal = template_html
    for i in template_html:
        if "####APITABLEHERE####" in template_html[n]:
            htmlFinal[n] = stockinfoTableHTML
            print(str(n)+" "+htmlFinal[n])
        else:
            htmlFinal[n] = template_html[n]
            print(str(n)+" "+htmlFinal[n])
        n=n+1
    return htmlFinal

def format_finalHTML(htmlFinal):
    print(htmlFinal)
    print("")
    n=0
    htmlFinalFormatted=""
    for i in htmlFinal:
        htmlFinalFormatted=htmlFinalFormatted+htmlFinal[n]
        n=n+1

    print(htmlFinalFormatted)
    return htmlFinalFormatted

def create_indexHTML(htmlFinalFormatted):
    idxFile = open("/var/www/html/index.html", "w")
    idxFile.write(htmlFinalFormatted)
    idxFile.close()
    return

print("* * * * * * * * * * *")
print("")
print("Step 1: read template.html, store into variable template_html")
template_html = get_templateHTML()
print("")
print("Step 1: completed!")

print("* * * * * * * * * * *")
print("")
print("Step 2: get_findata_fromAPI(), return stockinfo")
stockinfo = get_findata_fromAPI()
print("")
print("Step 2: completed!")

print("* * * * * * * * * * *")
print("")
print("Step 3: convert_findata_toHTML(stockinfo), return stockinfoTableHTML")
stockinfoTableHTML = convert_findata_toHTML(stockinfo)
print("")
print("Step 3: completed!")

print("* * * * * * * * * * *")
print("")
print("Step 4: compile_finalHTML(template_html, stockinfoTableHTML), return htmlFinal")
htmlFinal = compile_finalHTML(template_html, stockinfoTableHTML)
print("")
print("Step 4: completed!")

print("* * * * * * * * * * *")
print("")
print("Step 5: format_finalHTML(htmlFinal), return htmlFinalFormatted")
htmlFinalFormatted = format_finalHTML(htmlFinal)
print("")
print("Step 5: completed!")

print("* * * * * * * * * * *")
print("")
print("Step 6: create_indexHTML(htmlFinalFormatted)")
create_indexHTML(htmlFinalFormatted)
print("")
print("Step 6: completed!")
