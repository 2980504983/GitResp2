"""
    io多路复用之epoll:
        只使用与linux
        1 epoll 和 poll使用方法几乎一样，但是原理不同
        2 生成对象改为epoll(),将所有事件类型改为EPOLL类型

    select, poll, epoll总结:
        1 select:
            支持linux，windows，unix, 只能监控1024个io，效率和poll一样
        2 poll:
            支持linux，unix，能支持更多的io，效率和select一样
        3 epoll:
            支持linux， 能支持更多的io，效率最高，epoll的触发方式比poll多(也就是事件类型)
            例如epoll有 (EPOLLET边缘触发)，而poll只有水平触发(就是当某个io就绪了，系统会一直
            提醒你处理) 边缘触发就是提醒你，如果你没处理，就不在提醒你了，下一次再有io就绪了就一起
            提醒
"""


from socket import *
from select import *

# 创建监听套接字， 作为关注的io
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)

# 创建epoll对象
ep = epoll()

# 建立查找字典，通过一个io的fileno找到io对象
fdmap = {s.fileno(): s}

# 关注s
ep.register(s, EPOLLIN | EPOLLERR)


# 循环监控io发生
while True:
    events = ep.poll()
    # 循环遍历列表，查看哪个io就绪，就进行处理
    for fd, event in events:
        # 区分哪个io就绪
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print('Connect from', addr)
            # 关注客户端连接套接字
            ep.register(c, EPOLLIN | EPOLLERR)
            fdmap[c.fileno()] = c  # 维护字典
        elif event & EPOLLIN:  # 判断是否为epollin就绪，
            data = fdmap[fd].recv(1024).decode()
            if not data:
                ep.unregister(fd)  # 取消关注
                del fdmap[fd]
                continue
            print(data)
            fdmap[fd].send(b'OK')
