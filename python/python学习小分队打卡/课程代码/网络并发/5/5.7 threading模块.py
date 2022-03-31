"""
    threading 模块
        步骤:
            (基本同Process)
            1 封装线程函数
            2 创建线程对象
            3 启动线程
            4 回收线程
"""

import threading
from time import sleep
import os

a = 1


# 下面的过程中，产生了两个线程，创建线程对象哪里，属于主线程，后面music属于分支线程
# 线程函数
def music():
    for i in range(3):
        sleep(2)
        print(os.getpid(), "播放: 黄河大合唱")  # pid相同是因为两个线程都在同一个进程中
    global a
    print("a=", a)
    a = 10000


# 创建线程对象
t = threading.Thread(target=music)
t.start()  # 启动线程

for i in range(4):
    sleep(1)
    print(os.getpid(), '播放: 葫芦娃')

t.join()  # 回收线程

# 这里a=10000，虽然子进程会复制父进程的内存空间，但是这两个线程是在同一个进程内的，线程们用是进程
# 的内存空间。
print("main a:", a)

