from socket import *

# 练习: 将一个文件从客户端发送到服务端保存,文件可能是文本类型也可能是二进制类型

filename = "D:/python/python学习小分队打卡/课程代码/网络并发/2/2.3 项目改进.py"

with open(filename, 'rb') as f:
    sockfd = socket()

    sockfd.connect(('192.168.213.1', 12358))

    while True:
        data = f.read(1024)
        if not data:
            break
        sockfd.send(data)

    sockfd.close()
