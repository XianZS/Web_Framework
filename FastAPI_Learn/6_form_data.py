from fastapi import FastAPI
from fastapi import Form
from pydantic import BaseModel

app = FastAPI()


class FileMode(BaseModel):
    file_name: str = "文件名"
    file_password: str = "文件密码"
    file_details: str = "文件详细信息"
    file_author: str = "文件创作者"
    file_time: str = "文件创建时间"


"""
    当有多个数据需要通过表单form提交时，我们可以通过创建数据模型，在书写视图函数时，
    指明所使用的数据模型
    from pydantic import BaseModel
    Class 我的数据模型(BaseModel):
        属性1:属性1的类型=默认值-1
        属性2:属性2的类型=默认值-2
"""


@app.post("/file_make")
async def file_make_function(data: FileMode = Form()):
    print(data)
    return "True"


@app.post("/make_form_data")
async def make_form_data_function(
    username: str = Form(),
    password: str = Form(),
):
    print(f"username is {username}, and password is {password}")
    return "True"
