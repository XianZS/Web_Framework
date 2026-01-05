from flask import Flask, render_template, abort
app = Flask(__name__)


@app.errorhandler(404)
def errorhandler_function(error):
    print(error)
    return render_template("404.html")


@app.route("/abort_404")
def abort_404_function():
    abort(404)


if __name__ == '__main__':
    app.run(debug=True)
