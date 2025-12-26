"""
路由
视图函数
"""

from flask import Flask

app = Flask(__name__)


""" 路由的简单使用 """


# 个人主页路由 /myself
@app.route("/myself")
def myself_function():
    return "<h1>这是个人主页路由</h1>"


# 网站详情路由 /about
@app.route("/about")
def about_function():
    return "<h1>这是网站详情路由</h1>"


""" 视图函数的简单使用 """


@app.route("/view")
def view_function():
    name = "view_function"
    return f"<h1>这是/view路由对应的视图函数的处理结果:{name}</h1>"


if __name__ == "__main__":
    app.debug = True
    app.run()
