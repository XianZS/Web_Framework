from flask import Flask

# 返回字符串 json html 自定义response对象

app = Flask(__name__)


# 路由请求
@app.route("/route")
def route_function():
    print("== route ==")
    return "1"


# 需要在每次进行路由请求之前，完成某些操作
@app.before_request
def before_request_function():
    print("before_request_function")


# 需要在每次进行路由请求之后，完成某些操作
@app.after_request
def after_request_function(response):
    print("after_request_function")
    return response


# 返回状态码
@app.route("/status")
def status_function():
    return "Everything is ok!", 200


if __name__ == "__main__":
    app.run()
