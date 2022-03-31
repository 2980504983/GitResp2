"""
    群聊聊天室:
        功能:
            类似qq群功能
        1 有人进入聊天室，需要输入姓名，不能重复
        2 人进入聊天室，其他人会收到通知
        3 一个人发消息，其他人会收到
        4 有人退出聊天室，其他人也会收到通知
        5 拓展功能，服务器可以向所有用户发送公告

        聊天室思路分析:
            1 需求分析:
                干什么达到什么效果?
            2 技术点的确定:
                1 数据如何流动:
                    转发: 客户端 --> 服务端 --> 其它客户端

                2 网络模型如何构建:
                    采用udp数据传输

                3 用户信息在哪维护怎么维护:
                    服务端: {name:address}  字典也是散列结构
                           [(name, address), ]

                4 随意收发消息如何避免阻塞:
                    收和发使用不同的进程执行

            3 结构设置注意事项:
                1 采用什么封装结构: 函数
                2 编写一个功能测试一个功能
                3 注释和结构的设计

            4 分析功能模块:
                1 网络搭建
                2 进入聊天室
                    客户端:
                        * 输入姓名
                        * 将请求发送给服务器
                        * 接收结果
                        * 允许则可以聊天，不允许则重新输入姓名
                    服务端:
                        * 接收请求
                        * 判断是否存在用户名
                        * 如果允许进入则将用户存储，并通知其它客户端
                        * 不允许则结束
                        * 将结果通知客户端
                3 聊天
                    客户端:
                        * 创建新的进程
                        * 一个进程循环发送消息
                        * 一个进程循环接收消息

                    服务端:
                        * 接收请求
                        * 判断请求类型
                        * 将消息转发
                4 退出聊天室
                    客户端:
                        * 输入quit或者ctrl -c退出
                        * 将请求发送给服务端
                        * 结束进程

                    服务端:
                        * 接收请求
                        * 将退出信息告知其他人
                        * 给该用户发送EXIT
                        * 删除用户
                5 管理员消息

            5 通信协议设置
                * 进入聊天室: L
                * 聊天: C
                * 退出: Q
                * 服务器反馈: OK 表示成功 其它表示失败
                * 客户端收到 EXIT 结束进程
            详细见 群聊聊天室设计图.jpg

"""

from socket import *
import os
import sys

# 什么时候定义全局变量: 如果很多封装模块都要用或者有固定的含义
# 有固定含义定义为全局变量，并且字母都大写，江湖规矩

# 服务器地址
ADDR = ('192.168.213.1', 8888)

# 存储用户
user = {}


# 登录
def do_login(s, name, addr):
    if name in user or '管理员' in name:
        s.sendto("该用户已经存在".encode(), addr)
        return
    s.sendto(b'OK', addr)  # 可以进入聊天室

    # 通知其他人
    msg = "\n欢迎'%s'进入聊天室" % name
    for i in user:
        s.sendto(msg.encode(), user[i])
    user[name] = addr  # 插入字典


# 聊天
def do_chat(s, name, text):
    msg = f"\n{name}: {text}"
    for item in user:
        if item != name:
            s.sendto(msg.encode(), user[item])


# 退出
def do_quit(s, name):
    msg = f'\n{name}退出聊天室'
    for item in user:
        if item != name:
            s.sendto(msg.encode(), user[item])
        else:
            s.sendto(b'EXIT', user[item])
    del user[name]  # 删除用户


# 处理请求
def do_request(s):
    while True:
        data, addr = s.recvfrom(1024)
        tmp = data.decode().split(' ')  # 拆分请求
        # 根据不同的请求类型具体执行不同的事情
        # L 进入  C 聊天  Q 退出
        if tmp[0] == "L":
            do_login(s, tmp[1], addr)  # 执行具体工作
        elif tmp[0] == 'C':
            text = ' '.join(tmp[2:])
            do_chat(s, tmp[1], text)
        elif tmp[0] == 'Q':
            do_quit(s, tmp[1])


# 搭建网络:
def main():
    # udp服务端
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)

    # 创建一个进程给服务器的父进程发消息，再让父进程转发给各个客户端
    pid = os.fork()
    if pid == 0:  # 子进程处理管理员消息
        while True:
            msg = input("管理员消息:")
            msg = "C 管理员 " + msg
            s.sendto(msg.encode(), ADDR)

    # 请求处理函数
    do_request(s)


main()
