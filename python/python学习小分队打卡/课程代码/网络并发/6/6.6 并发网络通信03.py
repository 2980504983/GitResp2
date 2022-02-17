"""
    练习:
        模仿fork完成基于process的多进程并发网络模型:
            fork多进程并发网络模型思路
            实现步骤:
            1 创建监听套接字
            2 等待接收客户端请求
            3 客户端连接创建新的进程处理客户端请求
            4 原进程继续等待其它客户端连接
            5 如果客户端退出，则销毁对应的进程

"""

from multiprocessing import Process
import signal
from socket import *
import os

HOSt = '0.0.0.0'
PORT = 8888
ADDR = (HOSt, PORT)

# 创建tcp套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 设置端口可以立即被重用
s.bind(ADDR)
s.listen(5)

# 处理僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
print("listen the port 8888...")

# 处理客户端请求
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()


while True:
    try:
        c, addr = s.accept()
        print(f"Connect from {addr}")
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    p = Process(target=handle, args=(c,))

    # 父进程退出，子进程也退出
    p.daemon = True

    p.start()
