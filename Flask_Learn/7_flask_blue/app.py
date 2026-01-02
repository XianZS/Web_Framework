from flask import Flask, render_template

app = Flask(__name__)
from auth.home import auth_home_bp

app.register_blueprint(
    auth_home_bp,
    url_prefix="/auth",
    static_folder="static",
    template_folder="templates"
)



if __name__ == '__main__':
    app.debug = True
    app.run()
