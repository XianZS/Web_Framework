from flask import Blueprint, render_template

home_bp = Blueprint("home_bp", __name__,
                    template_folder="templates", static_folder="static")


@home_bp.route("/home_1")
def home_1_function():
    return "home-1"


@home_bp.route("/home_2")
def home_2_function():
    return "home-2"


@home_bp.route("/home_templates")
def home_templates_function():
    return render_template("home.html")
