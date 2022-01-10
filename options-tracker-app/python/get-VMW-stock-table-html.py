#!/usr/bin/env python

from urllib.request import urlopen
import certifi
import json
from json2html import *

def get_jsonparsed_data(url):

    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)

url = ("https://financialmodelingprep.com/api/v3/quote-short/VMW?apikey=a6019491e15dbeaaeb41242ad459a370")
stockinfo = get_jsonparsed_data(url)
print(json2html.convert(json = stockinfo))
