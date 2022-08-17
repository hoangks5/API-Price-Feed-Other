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
