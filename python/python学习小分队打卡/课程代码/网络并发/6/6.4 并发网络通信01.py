"""
    并发网络通信模型:
        常见模型分类:
            1 循环服务器模型:
                循环接收客户端请求，处理请求，同一时刻只能处理一个请求，处理完毕后在处理下一个
                优点: (实现简单，占用资源少)
                缺点: (无法同时处理多个客户端请求)
                适用情况: 处理的任务可以很快完成，客户端无需长期占用服务端程序，udp比tcp更适合
                        循环。

            2 io并发模型:
                利用io多路复用，异步io等技术，同时处理多个客户端io请求
                优点: (资源消耗少，能同时高效处理多个io行为)
                缺点: (只能处理并发产生的io事件，无法处理cpu计算)
                适用情况: HTTP请求，网络传输等都是io行为

            3 多进程/线程网络并发模型:
                每当一个客户端连接服务器，就创建一个新的进程/线程为该客户端服务，客户端退出时
                在销毁该进程/线程
                优点: (能同时满足多个客户端长期占有服务端需求，可以处理各种请求)
                缺点: (资源消耗大)
                适用情况: 客户端同时连接量较少，需要处理行为较复杂的情况

    基于fork的多进程网络并发模型:
        实现步骤:
            1 创建监听套接字
            2 等待接收客户端请求
            3 客户端连接创建新的进程处理客户端请求
            4 原进程继续等待其它客户端连接
            5 如果客户端退出，则销毁对应的进程
"""

# fork_server.py 基于fork的多进程并发
# 服务端不退出，不断产生子进程，这是典型的产生僵尸进程的条件，因此到如signal模块

from socket import *
import os
import signal


# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)


# 具体处理客户端请求:
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()


# 创建tcp套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 设置端口可以立即被重用
s.bind(ADDR)
s.listen(5)

# 处理僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
print("listen the port 8888...")

while True:
    # 循环处理客户端连接
    try:
        c, addr = s.accept()
        print("Connect from", addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    # 创建子进程处理客户端请求
    pid = os.fork()
    if pid == 0:
        s.close()  # 子进程不需要用到总套接字，只要有一个监听套接字就行了，注意这里关闭总套接字不会影响父进程，父子进程中都有各自的主套接字，因为复制
        handle(c)  # 处理具体事物
        os.exit(0)  # 执行完handle就让子进程消耗
    # 无论是执行父进程，还是fork出错，都要回去继续处理连接
    else:
        c.close()  # 父进程不需要监听套接字
