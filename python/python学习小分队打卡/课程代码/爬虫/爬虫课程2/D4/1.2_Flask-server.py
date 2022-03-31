import time
from wsgiref.simple_server import make_server

from flask import Flask, render_template
from time import sleep

# 实例化一个app
app = Flask(__name__, template_folder='templates')


# 创建视图函数和路由地址
@app.route('/yang')
def index_1():
    time.sleep(2)
    return 'hello yang'


# 第二个页面(返回一个静态页面)
@app.route("/yan")
def index_2():
    time.sleep(2)
    return render_template('flask_page.html')


# 第三个页面(返回一个静态页面)
@app.route("/lily")
def index_3():
    time.sleep(2)
    return render_template('flask_page.html')


if __name__ == "__main__":
    server = make_server('127.0.0.1', 5000, app)
    server.serve_forever()

    # debug=True表示开启调试模式,服务器端代码被修改后按下保存键会自动重启服务
    app.run(debug=True)

# 这么简单有点牛啊,
# 记得在浏览器访问的时候要加上自己的路由地址，也就是http://127.0.0.1:5000/yang
