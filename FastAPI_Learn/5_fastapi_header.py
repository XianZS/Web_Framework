from fastapi import FastAPI
from fastapi import Header

app = FastAPI()


@app.get("/get_header")
async def get_header_function(
    x_value: str = Header("x_key"), y_value: int = Header("y_key")
):
    print(f"{x_value} type is {type(x_value)}")
    print(f"{y_value} type is {type(y_value)}")
    return {"x": str(type(x_value)), "y": str(type(y_value))}
