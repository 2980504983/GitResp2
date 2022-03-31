"""
    系统编程(依赖于操作系统的编程):
        1 linux操作系统:
            1 shell命令:
                shell命令是linux和unix的一种专有叫法，简单的来说，shell命令就是在命令行
                输入的命令，但是，输入命令后，会经过解释器shell(壳)进行解释，有效的就会交由
                内核执行，无效的就不执行，所以shell可以认为是一种对保护操作系统的保护
            2 文件系统结构:
                linux文件系统结构是一个典型的树形结构

        2 io网络编程:
            1 文件io:
                对文件的读写open() read() write() close(),文件缓冲区(减少与磁盘交互次数)，
                flush()，文件偏移量, seek()
            2 网络io:
                理论基础:
                    osi七层模型, tcp/ip模型(四层模型), 三次握手和四次挥手, http协议,
                    传输层协议(tcp,udp协议),tcp协议与udp协议之间的差异，各自提供怎样的服务
                TCP通信:
                    socket() bind() listen() accept() recv() send() connect()
                UDP通信:
                    socket() bind() recvfrom() sendto(),不需要建立连接

        3 并发编程:
            1 进程:
                1 进程理论:
                    什么是进程，进程的状态，僵尸进程
                2 fork进程:
                    os.fork() 基于fork网络并发
                3 Process进程:
                    Process() start() join() 进程池Pool, 进程间通信(管道，消息队列，
                    共享内存，信号量)
            2 线程:
                1 线程创建:
                    Thread() start() join() 基于线程的网络并发
                2 同步互斥:
                    Event() Lock() 死锁
                3 GIL:
                    全局解释器锁
            3 io模型:
                1 阻塞io:
                    默认形态，简单，效率低
                2 非阻塞io:
                    block timeout
                3 io多路复用:
                    select() poll() epoll()
                4 协程:
                    什么是协程，gevent

"""