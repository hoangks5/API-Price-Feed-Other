import requests
import time
import pymongo
import threading
import certifi
from datetime import datetime
import numpy as np
from flask import Flask
import json
from flask_cors import CORS
import random
# BTC-USD, ETH-USD, BNB-USD, DOGE-USD, LINK-USD, UNI-USD, SOL-USD, MATIC-USD, LUNA-USD, DOT-USD, ATOM-USD
# Connection MongoDB


client = pymongo.MongoClient("mongodb+srv://hoangks5:YrfvDz4Mt8xrrHxi@cluster0.tcbxc.mongodb.net/",tlsCAFile=certifi.where())
mydb = client['compare']
mycol = mydb['data']
TOKENS = ['BTC-USD', 'ETH-USD', 'DOGE-USD', 'LINK-USD',  'SOL-USD', 'MATIC-USD',  'DOT-USD', 'ATOM-USD']

def get_price_min(token):
    token = token.split('-')[0]
    url = "https://pricefeedfastapi.herokuapp.com/min/"+token
    response = requests.get(url).json()['price']
    timest = time.time()
    avg = {
        'source' : 'Min',
        'token' : token,
        'timestamp' : timest,
        'price' : response,
    }
    mycol.insert_one(avg)
def get_price_max(token):
    token = token.split('-')[0]
    url = "https://pricefeedfastapi.herokuapp.com/max/"+token
    response = requests.get(url).json()['price']
    timest = time.time()
    avg = {
        'source' : 'Max',
        'token' : token,
        'timestamp' : timest,
        'price' : response,
    }
    mycol.insert_one(avg)


def get_price_noise(token):
    token = token.split('-')[0]
    url = "https://pricefeedfastapi.herokuapp.com/noise/"+token
    response = requests.get(url).json()['price']
    timest = time.time()
    avg = {
        'source' : 'Noise',
        'token' : token,
        'timestamp' : timest,
        'price' : response,
    }
    mycol.insert_one(avg)


def get_price_main():
    token = token.split('-')[0]
    url = "https://pricefeedfastapi.herokuapp.com/"+token
    response = requests.get(url).json()
    price_median = response['price_median']
    price_vwa = response['price_volume_weighted_average']
    timest = time.time()
    avg = {
        'source' : 'Median',
        'token' : token,
        'timestamp' : timest,
        'price' : price_median,
    }
    mycol.insert_one(avg)
    avg = {
        'source' : 'Vwa',
        'token' : token,
        'timestamp' : timest,
        'price' : price_vwa,
    }
    mycol.insert_one(avg)

def get_price_coinbase(token):
    url = "https://api.exchange.coinbase.com/products/"+token+"T/stats"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    time_start = time.time()
    response = requests.request("GET", url, headers=headers)
    avg = {
        'source': 'Coinbase',
        'token': token.split('-')[0],
        'timestamp': time_start,
        'price': float(response.json()['last']),
    }
    mycol.insert_one(avg)


def get_price_chainlink(token):
    url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms='+token.split('-')[0]+'&tsyms='+token.split('-')[1]+'t'
    time_start = time.time()
    response = requests.get(url)

    avg = {
        'source': 'CHAINLINK',
        'token': token.split('-')[0],
        'timestamp': time_start,
        'price': response.json()['RAW'][token.split('-')[0]]['USDT']['PRICE'],
    }
    mycol.insert_one(avg)

def get_price(times,delay):
    for i in range(times):
        th = []
        for token in TOKENS:
            th.append(threading.Thread(target=get_price_min,args={token,}))
            th.append(threading.Thread(target=get_price_max,args={token,}))
            th.append(threading.Thread(target=get_price_noise,args={token,}))
            th.append(threading.Thread(target=get_price_coinbase,args={token,}))
            th.append(threading.Thread(target=get_price_chainlink,args={token,}))
        for ths in th:
            ths.start()
        time.sleep(delay)

get_price(5,120)
