# 导入FastAPI核心模块
from fastapi import FastAPI
# 导入uvicorn用于启动服务（也可通过终端命令启动）
import uvicorn

app = FastAPI(
    title="简单的FastAPI示例",  # API文档标题
    description="这是一个基础的FastAPI启动代码",  # API文档描述
    version="1.0.0"  # 版本号
)


@app.get("/")
def read_root():
    """根路径接口：返回简单的问候信息"""
    return {"message": "Hello FastAPI!"}


if __name__ == "__main__":
    # 配置服务地址、端口和启动文件
    uvicorn.run(
        "main:app",  # 格式：文件名:应用对象名（这里文件是main.py，对象是app）
        host="0.0.0.0",  # 允许外部访问（仅本地访问可设为127.0.0.1）
        # host="127.0.0.1",
        port=8000,  # 服务端口
        reload=True  # 开发模式：代码修改后自动重启服务（生产环境需关闭）
    )
