import matplotlib.pyplot as plt
import time
import requests
import  threading
import pymongo
import certifi


myclient = pymongo.MongoClient("mongodb+srv://hoangks5:YrfvDz4Mt8xrrHxi@cluster0.tcbxc.mongodb.net/",tlsCAFile=certifi.where())
mydb = myclient['compare']
mycol = mydb['data']


def show(token):
    datas = mycol.find({'token':token.split('-')[0]})
    for data in datas:
        print(data)

