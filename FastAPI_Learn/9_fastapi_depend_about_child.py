from fastapi import Depends, FastAPI
from typing import Union

app = FastAPI()


def animal(name: Union[str, None] = None):
    if name:
        return name
    else:
        return "default"


def cat(name: str = Depends(animal), foot: int = 4):
    return f"animal is {name},it has {foot} foot"


def people(name: str = Depends(animal), foot: int = 2):
    return f"animal is {name},it has {foot} foot"


@app.post("/test_cat")
async def test_function(cat: str = Depends(cat)):
    print(cat)
    return cat


@app.post("/test_people")
async def test_people_function(people: str = Depends(people)):
    print(people)
    return people
