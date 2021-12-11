from fastapi import FastAPI #import class FastAPI() từ thư viện fastapi
from utils import test

app = FastAPI() # gọi constructor và gán vào biến app


@app.get("/") # giống flask, khai báo phương thức get và url
async def root(): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    cache_data = test.get('user')
    if cache_data:
        return cache_data

    cache_data = test.set("user", ["1", "2", "3", "4"])
    return {"message": "Hello World"}