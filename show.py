import matplotlib.pyplot as plt
import save_price
import time
import requests
import  threading
import pymongo
import certifi



client = pymongo.MongoClient("mongodb+srv://hoangks5:YrfvDz4Mt8xrrHxi@cluster0.tcbxc.mongodb.net/",tlsCAFile=certifi.where())
mydb = client['compare']
mycol = mydb['data']
TOKENS = ['BTC-USD', 'ETH-USD', 'DOGE-USD', 'LINK-USD',  'SOL-USD', 'MATIC-USD',  'DOT-USD', 'ATOM-USD']

def show(token):
    token1 = token.split('-')[0]
    datas = mycol.find({})
    print(datas)
show('BTC-USD')