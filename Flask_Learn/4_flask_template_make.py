from flask import Flask, render_template

app = Flask(__name__)


@app.route("/template_make")
def template_make_function():
    # html文件存储在当前根路径下，templates文件夹下
    name = "kom"
    age = 19
    return render_template("xxx.html", name=name, age=age)


if __name__ == "__main__":
    app.run()
