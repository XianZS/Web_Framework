from flask import Flask
app = Flask(__name__)

print(1)

@app.route("/")
def index():
    return "index"


if __name__ == "__main__":
    app.run()
