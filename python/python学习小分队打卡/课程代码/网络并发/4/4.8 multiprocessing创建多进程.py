"""
    multiprocessing 创建多个子进程
        特点:
            1 使用multiprocessing创建进程同样是子进程复制父进程空间代码段，父子进城运行互不影响
            2 子进程只运行target绑定的函数部分，其余内容由父进程执行
            3 multiprocessing中父进程往往只用来创建子进程并回收子进程，具体时间由子进程完成
            4 multiprocessing创建的子进程中无法使用标准输入 (就是无法使用input)

        Process的各种属性:
            p.name  进程名称
            p.pid  对应子进程的pid
            p.is_alive()  查看子进程是否在生命周期
            p.daemon  设置父子进程的退出关系
                (在start前设置，如果设置True，子进程会随着父进程的退出而退出，一般不会和join一起用)
"""

from multiprocessing import Process, freeze_support
from time import sleep
import os


def th1():
    sleep(3)
    print("weiss")
    print(os.getppid(), '--', os.getpid())


def th2():
    sleep(2)
    print("ruby")
    print(os.getppid(), '--', os.getpid())


def th3():
    sleep(4)
    print("neo")
    print(os.getppid(), '--', os.getpid())


things = [th1, th2, th3]
jobs = []
for th in things:
    p = Process(target=th)
    jobs.append(p)  # 将进程对象保存
    p.start()


# 一起回收
for i in jobs:
    i.join()


# 参数的传递 ------------------------------------------------------------

# 带参数的进程函数
def worker(sec, name):
    for i1 in range(3):
        sleep(sec)
        print(f"I'm {name}")
        print(f"I'm working {sec}")


p = Process(target=worker, args=(2, ), kwargs={'name': 'Baron'})

if __name__ == "__main__":
    freeze_support()
    p.start()
    p.join()
