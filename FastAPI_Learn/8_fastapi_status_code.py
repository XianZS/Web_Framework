from fastapi import FastAPI

app = FastAPI()


"""
    status code:
        100~199: 数据
        200~299: 成功请求
        300~399: else
        400~: 失败
"""

"""
    不指定 status_code
"""


@app.post("/no_setting")
async def no_setting_function():
    return "no_setting_function"


"""
    指定 status_code ,setting 201
"""


@app.get("/setting_201", status_code=201)
async def setting_201_function():
    return "This status code is 201"


"""
    指明 status_code ,setting 222
"""


@app.put("/setting_222", status_code=222)
async def setting_222_function():
    return "This status code is 222"
