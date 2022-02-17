"""
    进程间通信(IPC):
        消息队列:
            1 通信原理:
                在内存中建立队列模型， 进程通过队列将消息存入，或者从队列中取出完成进程间通信

            2 实现方法:
                from multiprocessing import Queue
                q = Queue(maxsize = 0),
                功能: 创建队列对象
                参数: 最多存放消息的个数

                q.put(data,[block, timeout])
                功能: 向队列存入消息
                参数: data 要存入的内容
                     block 设置是否阻塞
                     timeout 超时检测

                q.get([block, timeout])
                功能: 取出消息
                参数: 同上

                q.full()  判断队列是否未满
                q.empty()  判断队列是否为空
                q.qsize()  队列中的事件个数
                q.close()  关闭队列
"""
from multiprocessing import Queue, Process,freeze_support
from time import sleep
from random import randint

# 创建消息队列
q = Queue(5)


def handle():
    for i in range(6):
        x = randint(1, 33)
        q.put(x)
    q.put(randint(1, 16))


def request():
    while True:
        print("摇啊摇...")
        sleep(2)
        try:
            print(q.get(3))
        except:
            break


if __name__ == "__main__":  # windows下会阻塞在fd2.recv()哪里，linux下可以正常运行
    freeze_support()
    p1 = Process(target=handle)
    p2 = Process(target=request)
    p2.start()
    p1.start()
    p1.join()
    p2.join()