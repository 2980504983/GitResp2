"""
    测试比较单进程，多进程，和多线程在 计算密集型程序和io密集型程序中的效率

    cpu 密集型程序:
        单进程:
            8.159267663955688秒
        多进程:
            2.1177752017974854秒
        多线程:
            8.499015092849731秒


    io 密集型程序:
        单进程:
            5.077086687088013秒
        多进程:
            1.6040825843811035秒
        多线程:
            5.604798793792725秒

    结果令人震惊:
        多线程比单进程慢，按理来说多线程也能提高程序的执行效率，同样是并发和并行，为什么会慢呢?
        这是因为python线程GIL的问题，其它后端编程语言,应该没有这样的问题

    python线程GIL:
        有图 python的线程.jpg
        1 python线程GIL问题(全局解释器锁)
            python解释器设计中加入了解释器锁，导致python解释器同一时刻只能解释执行一个线程，
            大大降低了线程的执行效率(虽然你有多线程了，但是解释器不支持多线程)

        2 后果:
            虽然python解释器因为有锁，不支持多线程，但是因为，线程遇到阻塞后，会让出解释器，所以，
            python多线程在执行多阻塞高延迟io时可以提升程序效率，其它情况并不能对效率有所提升

        3 GIL问题建议:
            1 使用多进程(但是进程消耗的资源比线程多)
            2 不使用c作为解释器(java C#)

    结论:
        在无阻塞状态下，多线程和单进程效率差不多，甚至不如单进程，但是多进程可以明显提升效率

"""
import time
from multiprocessing import Process
from threading import Thread


# 计算
def count(x, y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1


def write():
    with open('text', "w") as f:
        for i in range(1800000):
            f.write("Hello World")


def read():
    with open('text') as f:
        lines = f.readlines()


# IO
def io():
    write()
    read()


# -------------------------------------------------------------------

# 单进程测试
# tm = time.time()
# for i in range(10):
#     io()
# print(f"消耗时间{time.time()-tm}秒")


# 多进程测试
# if __name__ == "__main__":
#     jobs = []
#     tm = time.time()
#     for i in range(10):
#         p = Process(target=io)
#         jobs.append(p)
#         p.start()
#     for i in jobs:
#         i.join()
#     print(f"消耗时间{time.time()-tm}秒")


# 多线程测试
# jobs = []
# tm = time.time()
# for i in range(10):
#     t = Thread(target=io)
#     jobs.append(t)
#     t.start()
# for i in jobs:
#     i.join()
# print(f"消耗时间{time.time()-tm}秒")
