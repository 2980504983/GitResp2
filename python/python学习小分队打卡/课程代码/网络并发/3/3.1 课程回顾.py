"""
    前情回顾:
        1 tcp 客户端:
            socket --> connect --> send/recv --> close()

        2 收发缓冲区:
            协调收发速度

        3 粘包:
            tcp没有消息边界，多次发送内容被一次接收

        4 udp:
            服务端:
                socket --> bind --> recvfrom/sendto --> close
            客户端:
                socket --> sendto/recvfrom --> close
        5 udp应用:
            广播:一段发送多端接收

        6 http协议:
            一个应用层协议，传输层只能是tcp，只能用流式套接字
            格式: 请求格式 响应格式
            请求格式:
                请求行 (GET / HTTP/1.1)
                请求头 (key:value\r\n ...)
                空行
                请求体

            响应格式:

        注: 自己写的tcp服务端，也可以通过浏览器来访问，网址输入 ip:端口号


"""