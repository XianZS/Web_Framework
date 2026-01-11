from fastapi import FastAPI, Depends, Header, Cookie
from pydantic import BaseModel

app = FastAPI()


# 定义JSON请求体的Pydantic模型（前端传JSON时用）
class UserData(BaseModel):
    username: str = "username"
    age: int = 18


default_user_data = UserData()


# 定义依赖函数：同时捕捉多种前端参数
async def get_all_params(
    # 1. 路径参数（从URL路径 /test/{item_id} 捕捉）
    item_id: int,
    # 2. 查询参数（从URL ?page=10 捕捉）
    page: int = 1,
    # 3. 请求头参数（从请求头 X-Token 捕捉）
    x_token: str = Header(None),
    # 4. Cookie参数（从Cookie session_id 捕捉）
    session_id: str = Cookie(None),
    # 5. JSON请求体（从POST的JSON数据捕捉）
    user_data: UserData = default_user_data,
):
    # 把所有捕捉到的参数返回
    return {
        "item_id": item_id,  # 路径参数
        "page": page,  # 查询参数
        "x_token": x_token,  # 请求头
        "session_id": session_id,  # Cookie
        "user_data": user_data,  # JSON请求体
    }


# 路由注入依赖：获取所有参数
@app.post("/test/{item_id}")
async def test_dependency(all_params: dict = Depends(get_all_params)):
    return all_params

