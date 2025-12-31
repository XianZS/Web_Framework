"""
    flask 表单提交
"""

from flask import Flask, render_template, request

app = Flask(__name__)

# get 请求数据捕捉


@app.route("/get_method", methods=["GET"])
def get_method_function():
    nums = request.args.get("nums")
    if nums:
        for num in nums:
            print(num)
        return "True", 200
    else:
        return "False", 200

# post 请求数据捕捉


@app.route("/post_method", methods=["POST"])
def post_method_function():
    data = request.form.get("data")
    if data:
        print(data)
        return "True", 200
    else:
        return "False", 200


# file 文件捕捉
@app.route("/")
def index():
    return render_template("file.html")


@app.route("/upload", methods=["POST"])
def upload_function():
    file = request.files.get("file")
    if file:
        file_name = file.filename
        file.save(f"./{file_name}")
        return "True", 200
    else:
        return "False", 200


if __name__ == "__main__":
    app.debug = True
    app.run()
