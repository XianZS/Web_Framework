from flask import Flask

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    return "login"


@app.route("/")
def index():
    number = 1
    print(number)
    yyy = 100
    print(yyy)
    for x in range(1, 100):
        number += x
        number += 123
    return "iex"


if __name__ == "__main__":
    app.run()
