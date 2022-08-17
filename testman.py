import matplotlib.pyplot as plt
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

def get_price_main(token):
    token = token.split('-')[0]
    url = "https://pricefeedfastapi.herokuapp.com/"+token
    response = requests.get(url).json()
    price_median = response['price_median']
    price_vwa = response['price_volume_weighted_average']
    timest = time.time()
    avg = {
        'source' : 'Main',
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
def t1(token):
    data.append(get_price_min(token))
def t2(token):
    data.append(get_price_max(token))
def t3(token):
    data.append(get_price_noise(token))
def t4(token):
    data.append(get_price_coinbase(token))
def t5(token):
    data.append(get_price_chainlink(token))
def t6(token):
    data.append(get_price_main(token))


def show(token):
    th = []
    th.append(threading.Thread(target=t1,args={token,}))
    th.append(threading.Thread(target=t2,args={token,}))
    th.append(threading.Thread(target=t3,args={token,}))
    th.append(threading.Thread(target=t4,args={token,}))
    th.append(threading.Thread(target=t5,args={token,}))
    th.append(threading.Thread(target=t6,args={token,}))
    for ths in th:
        ths.start()
    for ths in th:
        ths.join()
    print(data)

def rint1(token):
    print(get_price_min(token))
    print(get_price_max(token))
    print(get_price_noise(token))
    print(get_price_coinbase(token))
    print(get_price_chainlink(token))
    print(get_price_main(token))
rint1('DOGE-USD')