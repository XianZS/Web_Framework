"""
pip install flask
"""

# 第一步：导入
from flask import Flask

# 第二步：创建APP对象
app = Flask(__name__)


# 第三步：创建路由和视图函数之间的映射关系
@app.route("/")
def index():
    return "这里是HOME!"


# 第四步：运行Flask
if __name__ == "__main__":
    app.run()
