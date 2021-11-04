#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 21:05:33 2021

@author: emmye
"""

import requests
import time

# import os
# os.chdir("/Users/emmye/Downloads")

apikey='QPN49jIxeY62QLtvyhYd3M0PByHeSFV9RGWRXzFf'


url = "https://yfapi.net/v6/finance/quote"
#querystring = {"symbols":"AAPL,BTC-USD,EURUSD=X"}
querystring = {"symbols": input("Enter a ticker: ")}
headers = {'x-api-key': apikey }

response = requests.request("GET", url, headers=headers, params=querystring)
#print(response.text)

response.raise_for_status()  # raises exception when not a 2xx response
#if response.status_code != 204:
stock_json = response.json()

data =(stock_json['quoteResponse']['result'][0]["symbol"] +', '+ time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(stock_json['quoteResponse']['result'][0]["regularMarketTime"])) +', '+ str(stock_json['quoteResponse']['result'][0]["regularMarketPrice"]))

f = open('DSquiz2.csv', 'a',newline='')
f.write(data)
f.close()
