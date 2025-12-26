"""
安装flask : pip install flask
"""

# 导入flask
from flask import Flask

# 创建flask的app应用
app = Flask(__name__)


# @flask应用.route(路径,请求方式,传入参数)
@app.route("/")
def index():
    return "<h1>This is index page!</h1>"


if __name__ == "__main__":
    app.run()
