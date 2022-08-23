import matplotlib.pyplot as plt
import save_price
import time
import requests
import  threading
import pymongo

client = pymongo.MongoClient("mongodb+srv://hoangks5:YrfvDz4Mt8xrrHxi@cluster0.tcbxc.mongodb.net/",tlsCAFile=certifi.where())
mydb = client['compare']
mycol = mydb['data']
TOKENS = ['BTC-USD', 'ETH-USD', 'DOGE-USD', 'LINK-USD',  'SOL-USD', 'MATIC-USD',  'DOT-USD', 'ATOM-USD']

