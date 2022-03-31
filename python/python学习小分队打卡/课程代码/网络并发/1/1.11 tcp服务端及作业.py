"""
    创建一个 tcp_server(tcp协议的服务端)
"""

import socket

# 1 创建tcp套接字
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 2 绑定地址
sockfd.bind(('192.168.213.1', 10325))


# 3 设置监听
sockfd.listen(5)

# 这两个循环的作用是，当一个客户端断开连接后，服务器销毁该客户端对应的套接字，并回到等待连接的状态
while True:
    # 4 阻塞等待处理连接
    print("Waiting for connect...")  # 用于看出阻塞的现象
    connfd, addr = sockfd.accept()
    print("Connect from", addr)

    while True:
        # 5 收发消息
        data = connfd.recv(1024)
        if not data:  # 当客户端断开连接时，recv()会返回空
            break
        print("收到", data.decode())

        n = connfd.send(b'Thanks')  # 发送的要是字节串
        print(f"发送了{n}个字节")
    connfd.close()

# 6 关闭套接字
sockfd.close()


# 没有创建客户端时，可以用linux来测试
# 输入 telnet 192.168.1.7 8888
