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
    datas = mycol.find({'token':token.split('-')[0]},'source':'Min')
    min_price = []
    max_price = []
    noise_price = []
    coinbase_price = []
    chainlink_price = []
    min_ts = []
    max_ts = []
    noise_ts = []
    coinbase_ts = []
    chainlink_ts = []

    for data in datas:
        min_price.append(data['Min'],data['timestamp'])
        max_price.append(data['Max'])
        noise_price.append(data['Noise'])
        coinbase_price.append(data['Coinbase'])
        chainlink_price.append(data['CHAINLINK'])

    print(min_price)

show('BTC-USD')
