"""
    httpserver2.0
        1 主要功能:
            1 接收客户端请求
            2 解析客户端发送的请求
            3 根据请求组织数据内容
            4 将数据内容形成http响应格式返回给浏览器

        2 升级点:
            1 采用io并发，可以满足多个客户端同时发起请求情况
            2 做基本的请求解析，根据具体请求返回具体内容，同时满足客户端简单的
              非网页请求情况
            3 通过类接口形式进行功能封装

        3 技术分析:
            1 使用tcp通信，基于http协议格式
            2 select io多路复用

        4 类的接口设计:
            1 在用户使用角度进行流程设计
                * 当需要完成的功能是一个比较大的概括的功能，可以提供继承方法，
                  让别人使用时继承你的类

                * 针对一个非常具体的功能，尽量帮用户实现更多的功能，让用户尽可
                  能少的修改代码或尽可能简单使用

                * 不能够替用户决定的属性，并且属性不多的时候，让用户传参

                * 不能替用户决定的复杂功能，让用户去重写

            2 确定功能，参数，使用方法
"""

# httpserver2.0
from socket import *
from select import *


# 具体功能实现
class HTTPSever:
    def __init__(self, host='0.0.0.0', port=8888, dir=None):
        self.host = host
        self.port = port
        self.dir = dir
        self.address = (self.host, self.port)

        # 多路复用列表
        self.rlist = []
        self.wlist = []
        self.xlist = []

        # 实例化对象时直接创建套接字
        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # 绑定地址
    def bind(self):
        self.sockfd.bind(self.address)

    # 启动服务
    def serve_forever(self):
        self.sockfd.listen(3)
        print("Listen the port %d" % self.port)
        # io多路复用的方法接收客户端请求
        self.rlist.append(self.sockfd)
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c, addr = self.sockfd.accept()
                    print("Connect from", addr)
                    self.rlist.append(c)  # 增加新的io关注

                else:
                    self.handle(r)

    def handle(self, connfd):
        # 接收HTTP请求
        request = connfd.recv(1024)
        # 客户端退出
        if not request:
            self.rlist.remove(connfd)  # 取消对客户端的关注
            connfd.close()  # 关闭监听套接字
            return
        # 提取请求内容(字节串按行切割)
        request_line = request.splitlines()[0]
        info = request_line.decode().split(' ')[1]
        # 获取连接的客户端的地址
        print(connfd.getpeername(), ':', info)

        # 根据请求内容进行数据整理
        # 简单点分为两类，请求网页，其它
        if info == '/' or info[-5:] == '.html':
            self.get_html(connfd, info)
        else:
            self.get_data(connfd, info)

    # 返回网页
    def get_html(self, connfd, info):
        if info == '/':
            filename = self.dir + "/index.html"
        else:
            filename = self.dir + info
        try:
            fd = open(filename)
        except Exception:
            # 网页不存在
            response = 'HTTP/1.1 404 Not Found\r\n'
            response += 'Content-Typy:tex/html\r\n'
            response += '\r\n'
            response += '<h1>Sorry...</h1>'
        else:
            # 网页存在
            response = 'HTTP/1.1 200 OK\r\n'
            response += 'Content-Typy:tex/html\r\n'
            response += '\r\n'
            response += fd.read()
        finally:
            # 将响应发送给浏览器
            connfd.send(response.encode())
        pass

    # 其它数据
    def get_data(self, connfd, info):
        response = 'HTTP/1.1 200 OK\r\n'
        response += 'Content-Typy:tex/html\r\n'
        response += '\r\n'
        response += "<h1>waiting for httpserver 3.0</h1>"
        connfd.send(response.encode())
        pass
    pass


# 用户使用HTTPServer
if __name__ == '__main__':
    """
        通过HTTPServer类快速搭建服务，展示自己的网页
    """
    # 用户决定的参数
    HOST = '0.0.0.0'
    PORT = 8888
    DIR = './static'  # 网页存储位置

    httpd = HTTPSever(HOST, PORT, DIR)  # 实例化对象
    httpd.serve_forever()  # 启动服务
