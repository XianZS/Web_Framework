from typing import Union
from fastapi import FastAPI

# 模型
from sqlmodel import Field, PrimaryKeyConstraint, SQLModel

# 引擎
from sqlmodel import create_engine


app = FastAPI()


# 创建模型 》 表 people数据库模型
class PeopleModel(SQLModel, table=True):
    people_id: str = Field(default="people_id", primary_key=True)
    people_name: Union[str, None] = Field(default="people_name")
    people_age: int = Field(default=18)


class note(SQLModel, table=True):
    note_id: str = Field(default="note_id", primary_key=True)


# 创建引擎 》 create_engine
sql_name = "test.db"
sql_url = f"sqlite:///{sql_name}"

engine_obj = create_engine(sql_url, connect_args={"check_same_thread": False})


def migrate_sql_function():
    # 使用 SQLModel.metadata.create_all(传入参数=引擎)
    SQLModel.metadata.create_all(engine_obj)


# 应该在什么时候进行数据库迁移？
# 答案：在启动项目时


@app.on_event("startup")
async def start_up_function():
    print("项目开始启动，正在创建所有数据库")
    try:
        migrate_sql_function()
        print("创建成功")
    except Exception as e:
        print(f"创建失败,报错信息:{e}")


@app.get("/test")
async def test_function():
    return "test"
