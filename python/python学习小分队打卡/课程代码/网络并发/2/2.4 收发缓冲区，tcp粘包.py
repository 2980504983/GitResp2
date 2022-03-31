"""
    tcp 套接字数据传输特点:
        1 tcp连接中当一端退出，另一端如果阻塞在recv, 此时recv会立即返回一个空
        2 tcp连接中如果一端已经不存在，仍然视图通过send发送则会产生BrokenPipError
        3 一个监听套接字可以同时连接多个客户端，也能重复被连接

    每个操作系统都会为我们设置网络缓冲区, 接收，发送

    网络收发缓冲区:
        1 网络缓冲区有效的协调了消息的收发速度
        2 send 和 recv 实际是向缓冲区发送和接收消息，当缓冲区不为空recv就不会阻塞


    tcp粘包:
        原因:
            接收和发送的速度取决于网速，是不确定的。而且，tcp以字节流方式传输，没有消息边界，就
            会存在多次发送的消息被一次接收，此时就会形成粘包

            (由于发送的速度不比接收速度快，所以消息发送过来的消息不一定
            会立马被接收，而是会被存到网络缓冲区中，而此时有来了一条消息，又被存到消息缓冲区中，在接收
            就会形成粘包)

        影响:
            如果每次发送内容是一个独立的含义，需要接收端独立解析此时粘包会有影响

        处理方法:
            1 人为的添加消息边界(例如没发送一次消息，就在消息后面加上一个#号，其它符号也行)
            2 控制发送速度(让发送速度小于接收速度)

"""

from socket import *

sockfd = socket()

f = open("D:/python/python学习小分队打卡/课程代码/网络并发/2/2.4 接收的文件.py", "wb")

sockfd.bind(('192.168.213.1', 12358))
sockfd.listen(3)
while True:
    print("等待连接")
    connfd, addr = sockfd.accept()
    print(f"{addr}连接成功")

    while True:
            data = connfd.recv(1024)
            if not data:
                break
            f.write(data)
    connfd.close()
sockfd.close()
f.close()
