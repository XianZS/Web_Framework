from flask import Flask,jsonify
import mysql.connector
app = Flask(__name__)


def connection_to_mysql():
    conn = mysql.connector.connect(
            # where is my database?
            host="localhost",
            # how connection to my mysql?
            port=3306,
            # what connection?
            user="root",
            password="123456789",
            # which connection?
            database="graduation"
            )
    return conn

# delete update insert
@app.route("/first_make",methods=["GET"])
def first_make_function():
    # 第一步：得到连接对象
    conn=connection_to_mysql()
    # 第二步：创建游标对象
    cursor=conn.cursor()
    # 第三步：执行语句
    cursor.execute("insert into user (username,email) values ('jom','jom@qq.com')")
    # 第四步：提交事务
    conn.commit()
    # 第五步：关闭连接对象
    cursor.close()
    conn.close()
    return "True"

@app.route("/select_make",methods=["GET"])
def select_make_function():
    # 第一步：得到conn对象
    conn=connection_to_mysql()
    # 第二步：创建游标 将查询到的结果，以字典形式输出
    cursor=conn.cursor(dictionary=True)
    # 第三步：执行语句
    cursor.execute("select * from user")
    # 第四步：得到查询结果
    data=cursor.fetchall()
    # 第五步：关闭连接对象
    cursor.close()
    conn.close()
    print(data)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")
