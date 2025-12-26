"""
1；（上节课）请求对象：request：前端向后端，从客户端向服务器发起请求
响应对象：response：后端向前端响应。
2；模板：flask使用的jinja2模板引擎来渲染html模板，生成动态的网页请求。
    jom进入个人界面时，出现“hello jom”
    kom进入个人界面时，出现“hello kom”
"""

from flask import Flask, make_response, render_template


app = Flask(__name__)


# flask的响应对象
@app.route("/my_make_response")
def my_make_response_function():
    response = make_response("This is a response project!")
    response.headers["response_version"] = "1.1.1"
    return response


# flask的模板渲染
@app.route("/make_templates/<name>")
def make_templates_function(name):
    # render_template(html文件,传参)
    # html文件 /templates
    # 传参：传给html页面
    return render_template("hello.html", name=name)


if __name__ == "__main__":
    app.run()
