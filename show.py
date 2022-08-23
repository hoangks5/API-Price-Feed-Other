import matplotlib.pyplot as plt
import time
import requests
import  threading
import pymongo
import certifi

TOKENS = ['BTC-USD', 'ETH-USD', 'BNB-USD', 'DOGE-USD', 'LINK-USD', 'UNI-USD', 'SOL-USD', 'MATIC-USD', 'LUNA-USD', 'DOT-USD', 'ATOM-USD']

myclient = pymongo.MongoClient("mongodb+srv://hoangks5:YrfvDz4Mt8xrrHxi@cluster0.tcbxc.mongodb.net/",tlsCAFile=certifi.where())
mydb = myclient['compare']
mycol = mydb['data']


def show(token):
    datas = mycol.find({'token':token.split('-')[0],'source':'Min'})
    min_price = []

    for data in datas:
        print(data)

show('BTC-USD')
