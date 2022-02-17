"""
    ftp 文件服务器，服务端
"""

from socket import *
from threading import Thread
import sys, os
import time


# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)
FTP = "D:/python/python学习小分队打卡/课程代码/网络并发/6/ftp/"  # 文件库位置,最后加一个斜杆，方便后面拼接


# 创建类实现服务器文件处理功能
class FTPServer(Thread):
    """
        查看列表，下载，上传，退出处理
    """
    def __init__(self, connfd):
        self.connfd = connfd
        super().__init__()

    def do_list(self):
        files = os.listdir(FTP)
        if not files:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)  # 避免ok与后面的文件信息粘包

        # 拼接文件名(文件不包括隐藏文件和文件夹)
        filelist = ""
        for file in files:
            if file[0] != '.' and os.path.isfile(FTP+file):
                filelist += file + '\n'  # 人为设置消息边界防止粘包(边界是\n)
        self.connfd.send(filelist.encode())

    # 下载文件
    def do_get(self, filename):
        try:
            f = open(FTP+filename, 'rb')
        except Exception:
            # 打开失败文件不存在
            self.connfd.send('文件不存在'.encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)  # 防止ok粘包
        # 发送文件
        while True:
            data = f.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)
            # 这里不关闭文件是因为文件操作完函数就销毁了，函数一销毁里面的变量什么的也都会销毁

    # 上传文件
    def do_put(self, filename):
        if os.path.exists(FTP + filename):
            self.connfd.send("文件已存在".encode())
            return
        else:
            self.connfd.send(b'OK')
        # 接收文件
        f = open(FTP+filename, 'wb')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            f.write(data)
        f.close()

    # 循环接收请求，分情况调用功能函数
    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            if not data or data == 'Q':
                return  # run结束了对应客户端的线程就结束了
            elif data == 'L':
                self.do_list()
            elif data[0] == 'G':
                filename = data.split(' ')[-1]
                self.do_get(filename)
            elif data[0] == 'P':
                filename = data.split(' ')[-1]
                self.do_put(filename)


# 搭建网络服务端模型
def main():
    # 创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 设置端口立即被回收
    s.bind(ADDR)
    s.listen(5)

    # 循环等待客户端连接
    while True:
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            sys.exit('退出服务器')
        except Exception as e:
            print(e)
            continue

        # 创建线程处理请求
        client = FTPServer(c)
        client.setDaemon(True)
        client.start()  # 运行自定义线程类的run方法


if __name__ == "__main__":
    main()
