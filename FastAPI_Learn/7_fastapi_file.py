from fastapi import FastAPI
from fastapi import File, UploadFile

app = FastAPI()


# File 方法 上传文件
@app.post("/file_method")
async def file_method_function(file: bytes = File()):
    # 调用File方法
    with open("文件.md", "wb") as f:
        f.write(file)
    print(len(file))
    return {"file len": str(len(file))}


# UploadFile 类对象 上传文件
@app.post("/uploadfile_method")
async def uploadfile_method_function(file: UploadFile):
    # 创建了file对象
    with open(str(file.filename), "wb") as f:
        f.write(await file.read())
    return {"filename": file.filename}
