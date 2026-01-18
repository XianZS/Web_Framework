from fastapi import FastAPI
from fastapi import Depends
from fastapi import Header, Cookie
from pydantic import BaseModel


app = FastAPI()


class Req(BaseModel):
    user_name: str = "user_name"
    user_password: str = "user_password"


req = Req()


# 定义依赖函数
async def depend_function(
    # 路径参数
    number_child: int = 0,
    # 查询参数
    find_child: int = 0,
    # header参数
    header_child: str = Header(),
    # cookie参数
    cookie_child: str = Cookie(None),
    # 请求体参数
    req_child: Req = req,
):
    return {
        "number_child": number_child,
        "find_child": find_child,
        "header_child": header_child,
        "cookie_child": cookie_child,
        "req_child": req_child,
    }


"""
    依赖注入：归根结底是给路由增加限制，将多种复杂限制合并起来
"""


@app.post("/depend_method")
async def depend_method_function(data: dict = Depends(depend_function)):
    print(data)
    return data

