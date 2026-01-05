from flask import Flask
from bps.home_route.home_bp import home_bp
from bps.type_route.type_bp import type_bp
app = Flask(__name__)

app.register_blueprint(
    home_bp,
    url_prefix="/home"
)
app.register_blueprint(
    type_bp,
    url_prefix="/type"
)


if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")
