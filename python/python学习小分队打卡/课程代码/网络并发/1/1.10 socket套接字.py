"""
    套接字:
        介绍:
            实现网络编程进行数据传输的一种技术手段
            python实现 import socket (模块里名字全大写的是常量)

        套接字分类:
            流式套接字(SOCK_STREAM):
                以字节流方式传输数据，时间tcp网络传输方案(面向连接，tcp协议，可靠的，流式套接字)

            数据报套接字(SOCK_DGRAM):
                以数据报形式传输数据，实现udp网络传输方案(无连接，udp协议，不可靠，数据报套接字)

        tcp套接字编程(流式套接字):
            服务端流程:
                socket - bind - listen - accept - send/recv - close
                (那打电话比喻，socket得有一个电话，bind有一个电话号码，listen充话费，
                accept开机，send/recv沟通， close销毁对象，把电话砸了)

        1 创建套接字:
            import socket
            sockfd = socket.socket(socket_family=AF_INET,socket_type=SOCK_STREAM,proto=0)
                参数：socket_family 网络地址类型， AF_INET表示ipv4
                     socket_type 套接字类型 SOCK_STREAM表示流式
                     proto 通常为0 选择子协议
                返回值: 套接字对象

        2 绑定地址:
            本地地址: 'localhost', '127.0.0.1'
                (就是说在自己主机上创建客户端和服务端时，服务端的地址) (只在自己的主机上数据传输，
                当你觉得自己的服务端没什么问题了，就可以改成网络地址让其它主机的客户端来访问)
            网络地址:'你计算机的网络地址' 获取命令 ipconfig
            自动获取地址：'0.0.0.0'或者直接写''
            (有图片，绑定地址。jpg)

            sockfd.bind(addr)
                功能：绑定本机网络地址
                参数: addr是一个二元元组(ip, port) ('0.0.0.0', 8888)
                ip是网络地址，前面创建对象网络地址选的什么类型就怎么填，例如默认选的 IPV4就填
                '0.0.0.0'这样的，port是端口号(最好用一万以上的，太小了可能已经被系统或是其它软件占用)

        3 设置监听:
            sockfd.listen(n)
                功能: 将套接字设置为监听套接字，提供更多的功能，确定监听队列的大小
                参数: 监听队列大小

        4 等待处理客户端连接请求:
            connfd, addr = sockfd.accept()
                功能：阻塞等待处理客户端请求 (阻塞等待: 程序还行到这暂停，什么时候客户端发起连接在执行)
                返回值: connfd 客户端连接套接字（相当于为每一个连接的客户端创建一个专属的套接字）
                       addr 连接的客户端地址

        5 消息收发:
            data = connfd.recv(buffersize) (现在不在用最开始的套接字了，而是用专属于每个客户端的套接字)
                功能: 接收客户端消息
                参数: 每次最多接收消息的大小
                返回值： 接收到的内容

            n = connfd.send(data)
                功能: 发送消息
                参数: 要发送的内容， bytes格式
                返回值：发送的字节数

        6 关闭套接字:
            sockfd.close() 关闭套接字，销毁该套接字对象

"""
