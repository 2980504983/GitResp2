"""
    tcp客户端:
        socket --> bind(可选，不写操作系统自动分配) --> connect(并不属于三次握手和四次挥手，
        那是属于传输层的操作，是由操作系统来完成的，connect是应用层的操作) --> send/recv()
        --> close()

        sockfd.connect(server_addr)
        功能: 连接服务器
        参数: 元组，服务器的地址

        注： 只有相同类型的套接字才能进行通信
"""
from socket import *

# 创建tcp客户端(tcp_client) (注意客户端一般不用自己绑定地址，让系统随机分配)

# 1 创建套接字
sockfd = socket()  # 使用默认参数就是，tcp套接字

# 2 连接服务器
server_addr = ('192.168.213.1', 10325)  # 服务端地址
sockfd.connect(server_addr)

while True:
    # 3 发送消息,消息必须是字节串，只有常量前面才可以加b变成字节串，变量用encode()
    data = input("msg>>")
    if not data:
        break
    sockfd.send(data.encode())
    data = sockfd.recv(1024)
    print("Server:", data.decode())  # 打印接收内容

# 4 关闭套接字
sockfd.close()






