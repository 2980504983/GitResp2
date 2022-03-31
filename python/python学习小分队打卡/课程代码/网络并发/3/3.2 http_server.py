"""
    http_server v1.0
        基本要求:
            1 获取来自浏览器的请求
            2 判断，如果请求内容是 / (表示主页) 将index.html返回给客户端
            3 如果请求的是其它内容则返回404
"""

from socket import *


def request(connfd):
    data = connfd.recv(1024)
    # 防止浏览器异常退出，异常退出时，data为空，下面会报错
    if not data:
        return
    request_line = data.decode().split('\n')[0]
    info = request_line.split(' ')[1]
    if info == '/':
        with open("index.html") as f:
            response = "HTTP/1.1 200 OK\r\n"  # 字符串要写\r\n,三个双/单引号的注释不用,因为注释是固定格式
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += f.read()
    else:
        with open("index.html") as f:
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += "<h1>Sorry.....</h1>"
    connfd.send(response.encode())


# 搭建tcp网络
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 解决操作系统暂时保存端口的问题
s.bind(('192.168.213.1', 10325))
s.listen(3)

while True:
    connfd, addr = s.accept()
    print(f"Connect from {addr}")
    request(connfd)  # 处理客户端请求


