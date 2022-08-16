from fastapi import FastAPI #import class FastAPI() từ thư viện fastapi
import requests
app = FastAPI() # gọi constructor và gán vào biến app
@app.get("/min/{token}") # giống flask, khai báo phương thức get và url
async def price_min(token): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    return {"message": "Xin chào đây là đội Xanh nước biển"}