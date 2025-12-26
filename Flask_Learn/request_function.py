"""
get：不加密，request.args.get("key") ===> value
post：加密，request.form.get("key") ===> value
"""

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/login", methods=["GET"])
def login_function():
    # 获取前端传入的账号和密码
    name = request.args.get("name")
    password = request.args.get("password")
    print(f"账号是:{name},密码是:{password}")
    return f"已经成功接受账号:{name},密码:{password}"


@app.route("/set_config", methods=["POST"])
def set_config_function():
    myself_detail = request.form.get("myconfig")
    print(f"== ={myself_detail}= ==")
    return f"我的个人信息是:{myself_detail}"


if __name__ == "__main__":
    app.run()
