"""
    io多路复用之poll方法:
        支持linux和unix
        p = select.poll()
        创建poll对象 返回值poll对象，比select能监控跟多的io，select只能监控1024个

        p.register(fd, event)
        功能: 注册关注的io事件
        参数: fd 要关注的io ，
             event 要关注的io事件类型，常用类型:
                POLLIN  读io事件  （rlist）
                POLLOUT  写io事件  （wlist）
                POLLERR  异常io  （xlist）
                POLLHUP  断开连接

                将一个io放在多个事件中:
                p.register(sockfd, POLLIN|POLLERR)
                (这里的属性是用数据表示，也就是有一个数字代表了POLLIN，有一个数字代表了POLLERR
                ，我们将这两个数字按位或，表示这两个属性的相加，此时得到一个新的数字，这个数字就用有了
                POLLIN和POLLERR两者的属性了，还可以用位运算来删减功能，或者判断是否具备某功能)

        p.unregister(fd)
        功能: 取消对io的关注
        参数: IO对象或者IO对象的fileno(文件描述符)

        events = p.poll()
        功能: 阻塞等待监控的io事件发生
        返回值: [(filene, event),()...]  fileno: 文件描述符，event: io发生的事件类型

    poll_server:
        步骤:
            1 创建套接字
            2 将套接字传给register
            3 创建查找字典，并维护
            4 循环监控io发生
            5 处理发生的io
"""
from socket import *
from select import *


# 创建监听套接字， 作为关注的io
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)

# 创建poll对象
p = poll()

# 建立查找字典，通过一个io的fileno找到io对象
fdmap = {s.fileno():s}

# 关注s
p.register(s, POLLIN | POLLERR)


# 循环监控io发生
while True:
    events = p.poll()
    # 循环遍历列表，查看哪个io就绪，就进行处理
    for fd, event in events:
        # 区分哪个io就绪
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print('Connect from', addr)
            # 关注客户端连接套接字
            p.register(c, POLLIN | POLLERR)
            fdmap[c.fileno()] = c  # 维护字典
        elif event & POLLIN:  # 判断是否为pollin就绪，
            data = fdmap[fd].recv(1024).decode()
            if not data:
                p.unregister(fd)  # 取消关注
                del fdmap[fd]
                continue
            print(data)
            fdmap[fd].send(b'OK')
