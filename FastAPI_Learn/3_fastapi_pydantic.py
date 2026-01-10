from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


# 创建数据模型:student
class student(BaseModel):
    stu_name: str
    stu_id: Union[str, None]
    stu_details: Union[str, None]


app = FastAPI()


@app.post("/student")
async def student_function(stu: student):
    print(stu)
    print("学生id:", stu.stu_id)
    print("学生name:", stu.stu_name)
    print("学生details:", stu.stu_details)
    return stu
