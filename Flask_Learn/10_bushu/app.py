from flask import Flask, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return "index"


@app.route("/index")
def index_function():
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=8080, host="127.0.0.1")
