import matplotlib.pyplot as plt
import save_price
import time
import requests

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
    return avg

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
data = []
plt.bar('hi',10)
plt.show()