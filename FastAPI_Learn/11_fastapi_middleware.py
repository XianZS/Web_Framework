import time
from fastapi import FastAPI
from fastapi import Request

app = FastAPI()


@app.middleware("http")
async def middleware_1_function(request: Request, call_next):
    begin_time = time.time()
    print("=== 第一个中间件 ===")
    print(f"request type :{type(request)}")
    print(f"请求路径:{request.url}")
    print(f"请求方法:{request.method}")
    print(f"请求头:{request.headers}")
    res = await call_next(request)
    spent_time = str(time.time() - begin_time)
    res.headers["X-Spent-Time"] = spent_time
    return res


@app.middleware("http")
async def middleware_2_function(request: Request, call_next):
    print("=== 第二个中间件 ===")
    res = await call_next(request)
    return res


@app.get("/me")
async def me_function():
    return "test"


if __name__ == "__main__":
    pass
