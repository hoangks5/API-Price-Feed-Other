import matplotlib.pyplot as plt
import save_price
import time
import requests
import  threading

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
    return avg

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
    return avg

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
        'price_median' : price_median,
        'price_vwa' : price_vwa,

    }
    return avg

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
    return avg


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
    return avg
global data
data = []
def t1():
    


def show(token):
    th = []
        th.append(threading.Thread(target=get_price_min,args={token,}))
        th.append(threading.Thread(target=get_price_max,args={token,}))
        th.append(threading.Thread(target=get_price_noise,args={token,}))
        th.append(threading.Thread(target=get_price_coinbase,args={token,}))
        th.append(threading.Thread(target=get_price_chainlink,args={token,}))
    for ths in th:
        ths.start()
    time.sleep(delay)
    plt.bar('hi',10)
    plt.show()