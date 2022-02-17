"""
    UDP套接字编程:
        udp协议: 面向无连接，消息收发不需要提前连接，不可靠
        与TCP套接字略有不同，不需要设置监听(listen)了，收发改为recvfrom和sendto，并且
        创建的不是流式套接字，而是数据报套接字

        数据报套接字不会产生粘包，它是有消息边界的，数据会丢失

"""

# UDP_server
from socket import *

# 创建数据报套接字
sockfd = socket(AF_INET, SOCK_DGRAM)


# 绑定地址
server_addr = ('192.168.213.1', 12358)
sockfd.bind(server_addr)

# 循环收发消息
while True:
    data, addr = sockfd.recvfrom(1024)
    print(f"收到消息:", data.decode())
    sockfd.sendto(b"thanks", addr)

# 关闭套接字
sockfd.close()
