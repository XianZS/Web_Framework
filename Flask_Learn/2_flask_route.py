"""
flask路由的简单使用
/login 路由 处理函数
/Home 路由 主页网站介绍信息
/email 路由 联系开发者
不同路由对应着不同的处理函数
"""

from flask import Flask, jsonify, render_template, make_response

app = Flask(__name__)


# 1、简单应用
# app.route(url路径,请求方式GET、POST等)
@app.route("/home")
def home_function():
    return "Home Page"


# 2、路由传参
# jom进入个人主页时，会显示Hello JOM
# kom进入个人主页时，会显示Hello KOM
@app.route("/details/<name>")
def details_function(name):
    return f"Hello {name}"


# 3、路由规则
@app.route("/user/<int:user_id>")
def user_function(user_id):
    return f"User id is {user_id}!"


@app.route("/user/<float:number>")
def user_function2(number):
    return f"number is {number}"


# （重要）4、请求方法 GET | POST | PUT | DELETE
# GET: 输入的内容，会在URL中显示出来
# POST：输入的内容，不会在URL中显示出来
@app.route("/login", methods=["POST"])
def login_function():
    return "POST请求，登录/login"


@app.route("/data", methods=["GET"])
def data_function():
    return "GET请求，数据/data"


# 5、路由转换
# flask里面提供了一些内置的转换器，可以对URL的内容进行转换
@app.route("/shift/<int:user_id>/details")
def shift_function(user_id):
    # /shift/123/details
    print(type(user_id))
    return "True"


# （重点）6、视图函数返回
# 字符串 | HTML页面 | JSON格式文件 | Response对象
@app.route("/return_string")
def return_string_function():
    return "This is return_string route!"


@app.route("/return_html")
def return_html_function():
    # render_template(html页面文件，传入参数)
    # 特别注意：html页面，默认会去当前根路径下的templates文件夹下寻找你所传入的html页面
    return render_template("hello.html", name="jom")


@app.route("/return_json")
def return_json_function():
    data = {"name": "jom", "age": "17"}
    return jsonify(data)


@app.route("/return_response")
def return_response_function():
    response = make_response("This is response project!")
    response.headers["response_version"] = "1.1.1"
    return response


# 7、静态文件和模板的返回
# css、html、图片都可以通过特定路由设置来返回查看
@app.route("/templates_html_make")
def templates_html_make_function():
    return render_template("xxx.html")


# 8、路由的优先级
@app.route("/make")
def make_function():
    return "make function"


@app.route("/make/123")
def make_123_function():
    return "make 123 function"


if __name__ == "__main__":
    app.run()
