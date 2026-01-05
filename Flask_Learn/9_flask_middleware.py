from flask import Flask

app = Flask(__name__)


@app.before_request
def before_request_function():
    # 触发时间：请求处理之前
    print("before_request_function")


@app.after_request
def after_request_function(res):
    print("after_request_function")
    return res

@app.teardown_request
def teardown_request_function(res):
    print("teardown_request_function")
    print(f"res:{res}")

@app.route("/")
def index():
    # 时间
    print("===index===")
    return "index page"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
