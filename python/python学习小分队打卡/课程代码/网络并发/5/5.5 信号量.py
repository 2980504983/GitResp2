"""
    信号量(信号灯集):
        1 通信原理:
            给定一个数量对多个进程可见，多个进程都可以操作概数量增减，并根据数值决定自己行为

        2 实现方法:
            from multiprocessing import Semaphore
            sem = Semaphore(num)
            功能: 创建信号量对象
            参数: 信号量初始值
            返回值: 信号量对象

            sem.acquire()  将信号量减一，当信号量为零时阻塞
            sem.release()  将信号量加一
            sem.get_value()  获取信号量数量
"""

# 让信号量数量相当于资源，执行任务必须消耗资源
from multiprocessing import Process, Semaphore
from time import sleep
import os


# 创建信号量(最多允许三个任务同时执行)
sem = Semaphore(3)


# 任务函数
def handle():
    sem.acquire()  # 想执行任务必须消耗一个信号量
    print(f"{os.getpid()} 执行任务")
    sleep(2)
    print(f"{os.getpid()} 执行任务完毕")
    sem.release()  # 归还信号量


# 十个任务需要执行
for i in range(10):
    p = Process(target=handle)
    p.start()
