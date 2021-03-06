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
import requests

tickr = ["VMW", "GM", "NOK", "F", "INTC", "IDEX", "KGC"]
#fin_src = "YHF" for Yahoo Finance
#fin_src = "FMP" for financialmodelingprep.com
#fin_src = "LSM" for live-stock-market
fin_src = "LSM"

def get_templateHTML():
    file1 = open("template.html", "r")
    template_html = []
    idx=0
    for line in file1.readlines():
        line_num = str(idx)
        template_html.insert(idx, line)
        #print("Line Number "+line_num+": "+template_html[idx])
        idx=idx+1
    return template_html

def get_findata_fromAPI(tickr):
    idx=0;
    stockinfo = []
    for i in tickr:
        url = ("https://financialmodelingprep.com/api/v3/quote-short/"+tickr[idx]+"?apikey=a6019491e15dbeaaeb41242ad459a370")
        stockinfo.insert(idx, get_jsonparsed_data(url))
        idx=idx+1
    #print("stockinfo list length: "+str(len(stockinfo)))
    return stockinfo

def get_findata_fromAPI_v2(tickr):
    stockinfo = []
    url = "https://yh-finance.p.rapidapi.com/stock/v2/get-options"
    idx=0
    for i in tickr:
        querystring = {"symbol":tickr[idx],"date":"1562284800","region":"US"}
        headers = {
            'x-rapidapi-host': "yh-finance.p.rapidapi.com",
            'x-rapidapi-key': "53fcd0c825msh7a1a2f8f3846288p141427jsne888db9745f9"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        stockinfo.insert(idx, get_jsonparsed_data_v2(response.text))
        idx=idx+1
    return stockinfo

def get_findata_fromAPI_v3(tickr):
    stockinfo = []
    url = "https://live-stock-market.p.rapidapi.com/yahoo-finance/v1/options"
    idx=0
    for i in tickr:
        querystring = {"symbol":tickr[idx]}
        headers = {
            'x-rapidapi-host': "live-stock-market.p.rapidapi.com",
            'x-rapidapi-key': "53fcd0c825msh7a1a2f8f3846288p141427jsne888db9745f9"
            }
        response = requests.request("GET", url, headers=headers, params=querystring)
        stockinfo.insert(idx, get_jsonparsed_data_v2(response.text))
        idx=idx+1
    return stockinfo

def get_jsonparsed_data(url):
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    jsonparsed_data = json.loads(data)
    #print(jsonparsed_data)
    return jsonparsed_data

def get_jsonparsed_data_v2(data):
    jsonparsed_data = json.loads(data)
    return jsonparsed_data

def convert_findata_toHTML(stockinfo):        
    stockinfoTableHTML = (json2html.convert(json = stockinfo))
    #print(stockinfoTableHTML)
    return stockinfoTableHTML

def compile_finalHTML(template_html, stockinfoTableHTML):
    n=0
    htmlFinal = template_html
    for i in template_html:
        if "####APITABLEHERE####" in template_html[n]:
            htmlFinal[n] = stockinfoTableHTML
            #print(str(n)+" "+htmlFinal[n])
        else:
            htmlFinal[n] = template_html[n]
            #print(str(n)+" "+htmlFinal[n])
        n=n+1
    return htmlFinal

def format_finalHTML(htmlFinal):
    #print(htmlFinal)
    #print("")
    n=0
    htmlFinalFormatted=""
    for i in htmlFinal:
        htmlFinalFormatted=htmlFinalFormatted+htmlFinal[n]
        n=n+1

    x1=htmlFinalFormatted.replace("<ul>", "")
    x2=x1.replace("</ul>", "")
    x3=x2.replace("</li>", "")
    x4=x3.replace("<li>", "")
    x5=x4.replace("<table border=\"1\"><thead><tr><th>symbol</th><th>price</th><th>volume</th></tr></thead><tbody>", "")
    x6=x5.replace("</tbody></table>", "")
    x7=x6.replace("</body>", "</table></body>")
    x8=x7.replace("<body>", "<body> <table style=\"width:100%\">")
    htmlFinalFormatted =x8
    #print(htmlFinalFormatted)
    return htmlFinalFormatted

def create_indexHTML(htmlFinalFormatted):
    idxFile = open("/var/www/html/index.html", "w")
    idxFile.write(htmlFinalFormatted)
    idxFile.close()
    return

print("Step 1: read template.html, store into variable template_html")
template_html = get_templateHTML()
print("Step 1: completed!")
print("")
print("Step 2: get_findata_fromAPI(tickr) from "+fin_src+", return stockinfo")
if(fin_src == "FMP"):
    stockinfo = get_findata_fromAPI(tickr)
if(fin_src == "YHF"):
    stockinfo = get_findata_fromAPI_v2(tickr)
if(fin_src == "LSM"):
    stockinfo = get_findata_fromAPI_v3(tickr)
print("Step 2: completed!")
print("")
print("Step 3: convert_findata_toHTML(stockinfo), return stockinfoTableHTML")
stockinfoTableHTML = convert_findata_toHTML(stockinfo)
print("Step 3: completed!")
print("")
print("Step 4: compile_finalHTML(template_html, stockinfoTableHTML), return htmlFinal")
htmlFinal = compile_finalHTML(template_html, stockinfoTableHTML)
print("Step 4: completed!")
print("")
print("Step 5: format_finalHTML(htmlFinal), return htmlFinalFormatted")
htmlFinalFormatted = format_finalHTML(htmlFinal)
print("Step 5: completed!")
print("")
print("Step 6: create_indexHTML(htmlFinalFormatted)")
create_indexHTML(htmlFinalFormatted)
print("Step 6: completed!")
