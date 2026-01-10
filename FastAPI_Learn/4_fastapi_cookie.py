from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

begin_user_id = 10000
datas = dict()

# 设置cookie


@app.get("/set_cookie")
async def set_cookie_function():
    global begin_user_id
    res = JSONResponse(content="会话")
    res.set_cookie("user_id", str(begin_user_id))
    if begin_user_id % 2 == 0:
        res.set_cookie("h", "1")
        datas[str(begin_user_id)] = "1"
    else:
        res.set_cookie("h", "0")
        datas[str(begin_user_id)] = "0"
    begin_user_id += 1
    return res


# 查看所有的cookie
@app.get("/select_all_cookie")
async def select_all_cookie_function():
    return datas


# (正常)校验某个用户对h资源的访问权限
@app.get("/check")
async def check_function(req: Request):
    user_id = req.cookies.get("user_id")
    h_right = req.cookies.get("h")
    print(user_id, h_right)
    if h_right == "1" and datas[user_id] == "1":
        return "True"
    else:
        return "False"
