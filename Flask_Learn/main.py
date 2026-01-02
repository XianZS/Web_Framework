# 导入Flask框架和相关模块
from flask import Flask, request, jsonify
# 导入mysql-connector用于连接MySQL数据库
import mysql.connector

# 创建Flask应用实例
app = Flask(__name__)


# 定义一个函数，用于获取数据库连接
def get_db_connection():
    """
    创建并返回一个数据库连接。
    """
    connection = mysql.connector.connect(
        host='localhost',       # 数据库主机地址
        user='root',            # 数据库用户名
        password='YangHaiTao3135',# 数据库密码
        database='graduation'   # 要连接的数据库名称
    )
    return connection


# 定义一个路由，用于添加新用户，只接受POST请求
@app.route('/add_user', methods=['POST'])
def add_user():
    """
    从请求中获取用户信息，并将其添加到数据库中。
    """
    # 从POST请求的JSON数据中获取用户信息
    data = request.json
    name = data['name']
    email = data['email']

    # 获取数据库连接
    connection = get_db_connection()
    # 创建一个游标对象
    cursor = connection.cursor()
    # 执行SQL插入语句
    cursor.execute('INSERT INTO user (username, email) VALUES (%s, %s)', (name, email))
    # 提交事务
    connection.commit()
    # 关闭游标和连接
    cursor.close()
    connection.close()

    # 返回成功信息
    return 'User added!'


# 定义一个路由，用于获取所有用户信息
@app.route('/get_users')
def get_users():
    """
    从数据库中查询所有用户信息，并以JSON格式返回。
    """
    # 获取数据库连接
    connection = get_db_connection()
    # 创建一个字典类型的游标，这样查询结果会是字典列表
    cursor = connection.cursor(dictionary=True)
    # 执行SQL查询语句
    cursor.execute('SELECT * FROM user')
    # 获取所有查询结果
    users = cursor.fetchall()
    # 关闭游标和连接
    cursor.close()
    connection.close()
    # 将用户列表转换为JSON格式并返回
    return jsonify(users)


# 当该脚本作为主程序运行时，启动Flask应用
if __name__ == '__main__':
    # 启动web服务器，开启调试模式，监听所有网络接口，端口为5000
    app.run(debug=True,host="0.0.0.0",port=5000)