from flask import Blueprint

type_bp = Blueprint("type_bp", __name__,
                    template_folder="templates", static_folder="static")


@type_bp.route("/type_1")
def type_1_function():
    return "type-1"
