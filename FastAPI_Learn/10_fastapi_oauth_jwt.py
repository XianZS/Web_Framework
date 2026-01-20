from fastapi import FastAPI, HTTPException, Depends
from typing import Union
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from datetime import datetime, timedelta
import copy
from pwdlib import PasswordHash


# jwt参数设置
KEY = "23a6881d4ad6d43395cbd52967b50f718fd42aff32564f547eb19e0ccb9715be"
ALGORITHM = "HS256"
live_time = timedelta(seconds=40)


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwdlib_obj = PasswordHash.recommended()


def create_pwdlib_function(my_password):
    return pwdlib_obj.hash(my_password)


def check(user_input, sql_localhost):
    return pwdlib_obj.verify(user_input, sql_localhost)


# 用字典模拟数据库存储用户信息
users = {"username": "root", "password": create_pwdlib_function("123")}


def create_jwt(data):
    to_encode = copy.deepcopy(data)
    to_encode["past_time"] = str(datetime.now() + live_time)[:-7]
    print(f"to_encode:{to_encode}")
    to_encode_jwt = jwt.encode(to_encode, KEY, ALGORITHM)
    return to_encode_jwt


class Token:
    def __init__(self, username: str, token_type: Union[str, None] = "bearer"):
        self.access_token = username
        if token_type:
            self.token_type = token_type
        else:
            self.token_type = "bearer"


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == users["username"] and check(
        form_data.password, users["password"]
    ):
        print(form_data)
        print(users)
        # 将明文username设置为jwt编码之后的结果
        return Token(username=create_jwt({"username": form_data.username}))
    else:
        raise HTTPException(status_code=401, detail="账号或密码错误")


class UserModel:
    def __init__(self, username: str, email: Union[None, str] = "example@email.com"):
        self.username = username
        self.email = email


async def get_me(token: str = Depends(oauth2_scheme)):
    print(f"username:{token}")
    return UserModel(username=token)


@app.post("/me")
async def me_function(user_obj: UserModel = Depends(get_me)):
    print("=" * 40)
    print(user_obj)
    # 判断token是否过期
    # 如果过期：需要重新登录，重新获取token
    # 如果没有过期：允许通过
    username = user_obj.username
    to_decode_jwt = jwt.decode(username, KEY, algorithms=[ALGORITHM])
    print(to_decode_jwt)
    past_time = to_decode_jwt["past_time"]
    # past_time type str ===>>> datetime
    format_str = "%Y-%m-%d %H:%M:%S"
    if datetime.strptime(past_time, format_str) > datetime.now():
        return user_obj
    else:
        raise HTTPException(status_code=401, detail="过期了")
