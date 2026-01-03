# 一、Flask的安装和简单应用

## 1、flask的安装

```shell
pip install flask
```

## 2、flask的简单应用

```python
from flask import Flask

app=Flask(__name__)

    @app.route("/")
    def index():
        return "<h1>This is index page!</h1>"

        if __name__=="__main__":
app.run()
    ```

# 二、Flask的基础组成

![image-20251226150843636](C:\Users\XianZS\AppData\Roaming\Typora\typora-user-images\image-20251226150843636.png)

## 1、路由和视图函数

    ```python
route() && def function()
    ```

## 2、请求对象

    ​  请求方法、URL、请求头、表单数据

![image-20251226161043137](C:\Users\XianZS\AppData\Roaming\Typora\typora-user-images\image-20251226161043137.png)

## 3、响应对象和模板

### （1）响应对象

    ​  响应对象包含了发送给客户端的响应信息，包括状态码、响应头和响应体。Flask 默认会将字符串、HTML 直接作为响应体。

    ```python
    from flask import make_response

    @app.route('/custom_response')
    def custom_response():
        response = make_response('This is a custom response!')
        response.headers['X-Custom-Header'] = 'Value'
        return response
        ```

### （2）模板

        ​  Flask 使用 Jinja2 模板引擎来渲染 HTML 模板。模板允许你将 Python 代码嵌入到 HTML 中，从而动态生成网页内容。

        ```python
        from flask import render_template

        @app.route('/hello/<name>')
        def hello(name):
            return render_template('hello.html', name=name)
            ```

            ```html
            <!DOCTYPE html>
            <html>
            <head>
            <title>Hello</title>
            </head>
            <body>
            <h1>Hello, {{ name }}!</h1>
            </body>
            </html>
            ```

