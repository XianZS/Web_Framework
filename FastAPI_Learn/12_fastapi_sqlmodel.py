from os import stat
from typing import Union
from fastapi import Depends, FastAPI

# 模型
from sqlalchemy.orm.attributes import del_attribute
from sqlmodel import Field, SQLModel

# 引擎
from sqlmodel import create_engine

# 会话
from sqlmodel import Session
from sqlmodel import select

app = FastAPI()


# 创建模型 》 表 people数据库模型
class PeopleModel(SQLModel, table=True):
    people_id: str = Field(default="123", primary_key=True)
    people_name: Union[str, None] = Field(default="people_name")
    people_age: int = Field(default=18)


class note(SQLModel, table=True):
    note_id: str = Field(default="note_id", primary_key=True)


# 创建引擎 》 create_engine
sql_name = "test.db"
sql_url = f"sqlite:///{sql_name}"

engine_obj = create_engine(sql_url, connect_args={"check_same_thread": False})


def get_session():
    with Session(engine_obj) as session:
        yield session


@app.post("/read")
def read_function(session: Session = Depends(get_session)):
    # 表单的所有数据 select(表单对象)
    statement = select(PeopleModel)
    # 添加筛选条件 .where
    statement = statement.where(PeopleModel.people_age > 29)
    # 执行语句 session.exec(statement).all()
    data = session.exec(statement=statement).all()
    print(data)
    return data


@app.post("/add")
def add_function(people_obj: PeopleModel, session: Session = Depends(get_session)):
    print(f"people_obj:{people_obj}")
    # 插入缓存之中
    session.add(people_obj)
    # 提交事务 将其写入数据库
    session.commit()
    # 同步缓存和数据库
    session.refresh(people_obj)
    return "插入成功"


@app.post("/delete")
def delete_function(session: Session = Depends(get_session)):
    # 得到删除对象
    del_sql = select(PeopleModel).where(PeopleModel.people_age > 50)
    print(del_sql)
    del_data = session.exec(del_sql).all()
    # 执行删除操作
    for cho in del_data:
        print(f"将要删除:{cho}")
        session.delete(cho)
    session.commit()
    return del_data


@app.post("/update")
def update_function(session: Session = Depends(get_session)):
    # 得到修改对象
    update_sql = select(PeopleModel).where(PeopleModel.people_name == "fom")
    update_data = session.exec(update_sql).all()
    print(update_data)
    for cho in update_data:
        cho.people_age = 100
    session.commit()
    return update_data
