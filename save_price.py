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
    