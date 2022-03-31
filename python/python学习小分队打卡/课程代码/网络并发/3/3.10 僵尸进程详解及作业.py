"""
    模拟僵尸进程产生
"""
from time import sleep
import os, sys

# 让子进程退出，但是父进程不退出，且父进程没有处理子进程的退出状态，此时的子进程变成僵尸进城
pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("child pid:", os.getpid())
    sys.exit("子进程退出")
else:
    while True:  # 父进程不退出
        pass


# 用wait处理僵尸进程
# 但是wait有一个缺陷，它是一个阻塞函数，这样写让子进程先执行完，在执行父进程，这样就失去了创建两个进程
# 的意义了，所以wait一般不这么使用
pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("child pid:", os.getpid())
    sys.exit("子进程退出")
else:
    """
    os.wait() 处理僵尸进程
    """
    pid, status = os.wait()
    print("pid:", pid)
    print("status:", status)  # 这个值是child退出状态 * 256
    while True:  # 父进程不退出
        pass


# 用二级子进程处理僵尸进程, 也要用到wait
pid = os.fork()
if pid == 0:  # 一级子进程
    p = os.fork()
    if p == 0:  # 二级子进程
        print("干活中")
        sleep(5)
    else:  # 一级子进程
        sys.exit()
else:  # 父进程
    os.wait()  # 等待一级子进程退出
    print('干活中')
    sleep(5)


# 最终版本，又不阻塞，而且一劳永逸
# 用信号处理僵尸

import signal

# 子进程退出时，父进程忽略退出行为，子进程由系统处理
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

pid = os.fork()
if pid == 0:  # 子进程
    print("干活中")
    sleep(5)
else:  # 父进程
    print('干活中')
    sleep(5)
