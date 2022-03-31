"""
    select tcp服务
    通过io的多路复用（select）实现网络的并发

    思路分析:
        1 将关注的io放入到监听列表
        2 当io就绪时select会返回
        3 遍历返回值列表，得知哪个io就绪进行处理
"""

from socket import *
from select import select


# 创建监听套接字， 作为关注的io
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)

# 设置关注列表
rlist = [s]
wlist = []
xlist = []

# 循环监控io
while True:
    rs, ws, xs = select(rlist, wlist, xlist)

    # 遍历返回值列表，处理就绪的io
    for r in rs:
        if r is s:
            c, addr = r.accept()
            print("Connect from", addr)
            rlist.append(c)  # 增加新的IO关注

        else:
            # 有客户端发消息,这个不需要循环，因为每次客户端发消息，rs就会被返回,else内容就会被执行
            data = r.recv(1024).decode()
            # 客户端退出
            if not data:
                rlist.remove(r)  # 取消对客户端关注
                r.close()  # 关闭监听套接字
                continue
            print(data)
            # r.send(b'OK')
            wlist.append(r)  # 哪个客户端发来了消息，就把对应的监听套接字放到wlist中

    for w in ws:
        w.send(b'OK')
        wlist.remove(w)  # 发完消息就移除
        pass

    for x in xs:
        pass
