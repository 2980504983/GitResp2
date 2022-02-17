"""
    io并发:
        io是什么:
            在内存中存在数据交换的行为都是io行为

        io分类:  阻塞io，非阻塞io，io多路复用，异步io 等

            阻塞io:
                1 定义:
                    在执行io操作时如果执行条件不满足则阻塞。阻塞io是io的默认形态。
                2 效率:
                    阻塞io效率很低，但是逻辑简单
                3 阻塞情况:
                    1 因为某种执行条件没有满足造成的函数阻塞(accept, input, recv)
                    2 处理io的时间较长产生的阻塞(网络传输，大文件读写)

            非阻塞io:
                1 定义:
                    通过修改io属性行为，使原本阻塞的io变为非阻塞io的状态
                2 做法(举例子):
                    1 设置套接字为非阻塞io:
                        sockfd.setblocking(bool),默认True表示阻塞io
                    2 超时检测:
                        sockfd.settimeout(sec)
                    注: 超时检测是不会和非阻塞一起使用的，无意义

            io多路复用:
                1 定义:
                    同时监听多个io事件，当哪个io事件 准备就绪 就执行哪个io事件。以此形成可以同时
                    处理多个io的行为，避免一个io阻塞造成其它io均无法执行，提高了io执行效率

                    注: io的准备就绪，是系统内核感知到了它的发生，是一种不可逆的过程，例如，
                    执行一个input(),我在命令行输入字母并不算准备就绪，当我按下回车的那一刻才
                    算准备就绪

                2 具体方案:
                    就是把要多路复用的io扔给操作系统，让它来判定哪个io具备执行条件
                    select方法: windows linux unix
                    poll方法: linux unix
                    epoll方法: linux
                    注: 上面三种方法都封装在python标准库，select中
"""


# socket 套接字非阻塞示例
from socket import *
from time import ctime, sleep


# 日志文件
f = open('log.txt', 'a+')

# tcp套接字
sockfd = socket()
sockfd.bind(('0.0.0.0', 8888))
sockfd.listen(3)

# 设置套接字为非阻塞
# sockfd.setblocking(False)

# 设置超时检测
sockfd.settimeout(3)

while True:
    print("Waiting for connect...")
    # 没有客户端连接每隔三秒写一条日志,套接字设置为非阻塞，accept会报错
    try:
        connfd, addr = sockfd.accept()
    except (BlockingIOError, timeout) as e:
        sleep(3)
        f.write("%s : %s\n" % (ctime(), e))
        f.flush()  # 刷新缓冲区
    else:
        print('Connect from', addr)
        data = connfd.recv(1024).decode()  # 要想recv不阻塞要设置connfd为非阻塞
        print(data)
