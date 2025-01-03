from fastapi import FastAPI #import class FastAPI() từ thư viện fastapi
import requests
import numpy as np
import random
import API
app = FastAPI() # gọi constructor và gán vào biến app
@app.get("/{token}") # giống flask, khai báo phương thức get và url
async def price_main(token): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    return API.price_main(token)

@app.get("/min/{token}") # giống flask, khai báo phương thức get và url
async def price_1(token): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    return API.price_min(token)


@app.get("/max/{token}") # giống flask, khai báo phương thức get và url
async def price_2(token): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    return API.price_max(token)


@app.get("/noise/{token}")
async def price_3(token):
    token = (token + '-usd').upper()
    price = API.get_binance_price(token)['price'] 
    return {'price' : price + price*random.randint(1,100)*0.001}