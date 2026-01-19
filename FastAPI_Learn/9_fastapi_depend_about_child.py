from fastapi import Depends, FastAPI
from fastapi import Form


app = FastAPI()


# 父依赖项
def animal(name: str = Form()):
    print(name)
    return name


# 子依赖项
def cat(name: str = Depends(animal), foot: int = 4):
    return f"{name} has {foot} foot"


def people(name: str = Depends(animal), foot: int = 2):
    return f"{name} has {foot} foot"


@app.post("/test_cat")
async def test_cat_function(cat_obj: str = Depends(cat)):
    print(cat_obj)
    return cat_obj


@app.post("/test_people")
async def test_people_function(people_obj: str = Depends(people)):
    print(people_obj)
    return people_obj
