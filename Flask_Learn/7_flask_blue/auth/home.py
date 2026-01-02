from flask import Blueprint, render_template

auth_home_bp = Blueprint('auth_home', __name__)


@auth_home_bp.route("/index")
def index_function():
    return render_template("index.html")


@auth_home_bp.route("/login")
def login_function():
    return "<h1>LOGIN PAGE</h1>"


@auth_home_bp.route("/logout")
def logout_function():
    return "<h1>LOGOUT PAGE</h1>"


@auth_home_bp.route("/type")
def type_function():
    return "<h1>TYPE PAGE</h1>"

