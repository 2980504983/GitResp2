"""
    udp套接字广播
        广播定义: 一端发送多点接收
        广播地址: 每个网络的最大地址为发送广播的地址，想该地址发送，则网段内所有主机都能接收

    广播发送:
        1 创建udp套接字
        2 设置可以发送广播
        3 循环向广播地址发送


"""
# broadcast_send
from socket import *
from time import sleep

# 广播地址
dest = ('192.168.213.1', 9999)

s = socket(AF_INET, SOCK_DGRAM)

s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

data = "*******************************************"

while True:
    sleep(2)
    s.sendto(data.encode(), dest)  # 目标地址=广播地址


