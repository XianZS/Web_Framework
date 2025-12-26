from flask import Flask, request

app = Flask(__name__)

# GET请求获取数据


@app.route("/get_data", methods=["GET"])
def get_data_function():
    data = request.args.get("data")
    for cho in data:
        print(cho)
    return "True", 200


if __name__ == "__main__":
    app.run(debug=True)
