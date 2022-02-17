from socket import *

# UDP_client
# 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 服务器地址
addr = ('192.168.213.1', 12358)

# 循环收发
while True:
    data = input("Msg>>")
    if not data:
        break
    sockfd.sendto(data.encode(), addr)
    msg, addr = sockfd.recvfrom(1024)
    print('From server:', msg.decode())

sockfd.close()


# 注: 即使服务器地址是错误的，或是不存在的，也不会报错，因为无连接，但是这次的数据会丢失
