import matplotlib.pyplot as plt
import save_price
import time
import requests
import  threading
import pymongo
import certifi


myclient = pymongo.MongoClient("mongodb+srv://hoangks5:YrfvDz4Mt8xrrHxi@cluster0.tcbxc.mongodb.net/",tlsCAFile=certifi.where())
mydb = myclient['price']
mycol = mydb['datanew']
