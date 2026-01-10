from fastapi import FastAPI

app = FastAPI()


# 路径参数
# 默认 str类型
@app.get("/get_number/{number}")
async def get_number_function(number):
    num_type = type(number)
    return {"number": str(num_type)}


# 可以手动注明类型
@app.get("/get_number_2/{number_2}")
async def get_number_2_function(number_2: int):
    num2_type = type(number_2)
    return {"number_2": str(num2_type)}


# 查询参数：附加形式
datas = dict()

datas[(10086, "jom")] = "H市"
datas[(10087, "kom")] = "A市"
datas[(10088, "lom")] = "L市"


# print(datas)
@app.get("/stu")
async def stu_function(stu_id: int = 10088, stu_name: str = "lom"):
    print(datas)
    print(f"We Find Student Details is {datas[(stu_id,stu_name)]}")
    return datas[(stu_id, stu_name)]
