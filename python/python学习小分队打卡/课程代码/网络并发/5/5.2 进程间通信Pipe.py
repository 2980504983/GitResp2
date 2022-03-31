"""
    进程间通信(IPC)
        1 必要性:
            进程间空间独立，资源不共享，此时在进程间的数据传输，就需要特定的手段进行数据通信

        2 常用进程间通信方法:
            管道 消息队列 共享内存 信号 信号量 套接字

            管道通信(Pipe):
                1 通信原理:
                    在内存中开辟管道空间，生成管道操作对象，多个进程使用同一个管道对象进行
                    读写即可实现通信

                2 实现方法:
                    from multiprocessing import Pipe
                    fd1, fd2 = Pipe(duplex = True)
                        功能: 创建管道
                        参数: 默认表示双向管道，False表示单向管道
                        返回值: 表示管道两端的读写对象，如果是双向管道均可读写，单向管道
                               fd1只读，fd2只写
                    fd.recv()
                        功能: 从管道获取内容
                        返回值: 获取到的数据
                    fd.send(data)
                        功能: 向管道写入内容
                        参数: 要写入的数据
                    注: multiprocessing 中管道通信只能用于有亲缘关系的进程中(父子，兄弟)
                       管道对象在父进程中创建，子进程可以自己copy，不需要在创建管道对象了
"""

from multiprocessing import Process, Pipe, freeze_support

# 创建管道
fd1, fd2 = Pipe()


def app1():
    print("启动APP1， 请登录")
    print("请求APP2 授权")
    fd1.send("app1 请求登录")  # 写入管道
    data = fd1.recv()
    if data:
        print("登录成功:", data)


def app2():
    data = fd2.recv()  # 阻塞等待读取管道内容
    print(data)
    fd2.send(("Weiss", '123'))


if __name__ == "__main__":  # windows下会阻塞在fd2.recv()哪里，linux下可以正常运行
    p1 = Process(target=app1)
    p2 = Process(target=app2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
