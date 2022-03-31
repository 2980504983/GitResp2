"""
    进程池实现:
        1 必要性:
            1 进程创建和销毁的过程，消耗的资源较多
            2 当任务量众多，每个任务在很短时间内完成时，需要频繁的创建和销毁进程。此时对计算机
              压力较大
            3 进程池技术很好的解决了以上问题

        2 原理:
            创建一定数量的进程来处理事件，事件处理完，进程不销毁，而是继续处理其它事件，直到
            所有事件全都处理完毕统一销毁，增加进程的复用，降低资源消耗，详细见  进程池.jpg

        3 进程池实现:
            1 创建进程池对象， 放入适当的进程:
                from multiprocessing import Pool
                Pool(processes)
                功能: 创建进程池对象
                参数: 指定进程数量，默认根据系统自动判定(系统根据cpu核数来判定)

            2 将事件加入进程池要执行的事件队列:
                pool.apply_async(func, args, kwds)
                功能: 使用进程池执行func事件
                参数: func事件函数  args func的位置参数  kwds func的关键字参数
                返回值: 返回函数事件对象

            3 关闭进程池:
                pool.close()
                关闭之后，就不能添加新的事件了，但是已经在事件队列中的事件，仍然会执行完的

            4 回收进程池中的进程:
                pool.join()
"""


# 进程池使用实例
from multiprocessing import Pool, freeze_support
from time import sleep, ctime


# 进程池事件
def worker(msg):
    sleep(2)
    print(ctime(), '--', msg)


if __name__ == '__main__':
    # 创建进程池
    pool = Pool()  # 事件函数要写在创建进程池之前

    freeze_support()

    # 向进程池队列添加事件
    for i in range(10):
        msg = "Tedu%d"%i
        pool.apply_async(func=worker, args=(msg,))

    # 关闭进程池
    pool.close()

    # 回收进程池
    pool.join()
