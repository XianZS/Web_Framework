from typing import Union
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token")
async def login_function(form_data: OAuth2PasswordRequestForm = Depends()):
    print(f"form_data:{form_data}")
    print(f"username:{form_data.username};password:{form_data.password}")
    if form_data.username == "root" and form_data.password == "123":
        return {"access_token": form_data.username, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="账号或密码错误")


"""
    访问其它资源
"""


# 访问我的个人信息界面
class UserBaseModel(BaseModel):
    username: str = "default"
    email: Union[None, str] = "example@email.com"
    details: Union[None, str] = "详细信息"


async def get_details(token: str = Depends(oauth2_scheme)):
    """
    OAuth2PasswordBearer() ===>>> token ，token其实是当前的用户名username
    """
    print(token)
    return UserBaseModel(username=token, email="xxx@xxx.com")


@app.get("/details/me")
async def details_me_function(user_obj: UserBaseModel = Depends(get_details)):
    print(user_obj)
    return user_obj


if __name__ == "__main__":
    pass
