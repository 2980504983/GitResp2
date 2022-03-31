"""
    gevent_server 基于协程的tcp并发

    思路:
        1 将每个客户端的处理设置为协程函数
        2 让socket模块下的阻塞可以出发协程跳转
"""
import gevent
from gevent import monkey
monkey.patch_socket()  # 设置套接字阻塞为gevent阻塞
from socket import *


def handle(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print(data)
        c.send(b'OK')


# 创建tcp套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)

# 循环接收客户端连接
while True:
    c, addr = s.accept()
    print("Connect from", addr)
    handle(c)  # 处理具体的客户端请求
    gevent.spawn(handle, c)  # 协程方案，当recv不阻塞了，就会跳转到handle中，阻塞时就在这里等待客户端连接


