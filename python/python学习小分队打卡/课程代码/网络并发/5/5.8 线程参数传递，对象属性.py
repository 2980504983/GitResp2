"""
    创建多线程:

    线程对象属性:
        t.name 线程名称
        t.setName()  设置线程名称
        t.setDaemon(True)  主线程退出分支线程也退出(在start之前设置，一般不喝join一起使用)
        ...
"""

from threading import Thread
from time import sleep


# 带有参数的线程函数
def fun(sec, name):
    print("线程函数参数")
    sleep(sec)
    print(f"{name}执行完毕")


# 创建多个线程,抢占式关系，执行顺序不一定
jobs = []
for i in range(5):
    t = Thread(target=fun, args=(2, ), kwargs={"name": f'{i}'})
    jobs.append(t)  # 存储线程对象
    t.start()

for i in jobs:
    i.join()
