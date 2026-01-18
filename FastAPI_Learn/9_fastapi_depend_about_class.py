from fastapi import Depends, FastAPI

app = FastAPI()


# 以类的形式定义依赖项
class StuDepends:
    def __init__(
        self,
        name: str = "姓名",
        age: int = 18,
        address: str = "地址",
        else_details: str = "其它详细信息",
    ):
        self.stu_name = name
        self.stu_age = age
        self.stu_address = address
        self.stu_else_details = else_details

    def __str__(self):
        return f"""
        self.stu_name:{self.stu_name},
        self.stu_age:{self.stu_age},
        self.stu_address:{self.stu_address},
        self.stu_else_details:{self.stu_else_details}
        """


@app.post("/class_test")
async def class_test_function(stu: StuDepends = Depends(StuDepends)):
    print(stu)
    return stu
