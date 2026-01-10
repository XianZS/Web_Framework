# python3
# 1.fastapi的简单使用
from fastapi import FastAPI
# 创建app对象
app = FastAPI()


# 创建视图函数和路由之间的映射
@app.get("/")
async def index_function():
    return "index page"
