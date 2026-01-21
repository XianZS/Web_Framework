from fastapi import FastAPI, Request


app = FastAPI()


@app.middleware("http")
async def add_process_time_header_1(request: Request, call_next):
    print("=== 中间件1 ===")
    response = await call_next(request)
    print(request.method)
    print(request.url)
    print(request.cookies)
    if request.client:
        print(request.client.host)
    print(request.state)
    return response


@app.get("/test")
async def test_function():
    return "test"
