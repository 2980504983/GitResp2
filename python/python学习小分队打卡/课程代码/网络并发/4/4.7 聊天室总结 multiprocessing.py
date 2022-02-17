"""
    multiprocessing 模块创建进程
        multi多的意思，processing进程的意思，multiprocessing就是os.fork()的在封装，两者原理相同
        fork更偏向系统层，而multiprocessing则更符合python

        流程特点:
            1 将需要子进程执行的事件封装为函数
            2 通过模块的Process类创建进程对象，关联函数
            3 可以通过进程对象设置进程信息及属性 （可做可不做）
            4 通过进程对象调用start启动进程
            5 通过进程对象调用join回收进程

        基本接口使用:
            Process()
                功能:
                    创建进程对象
                参数:
                    target 要绑定函数的函数名
                    args ，target的位置参数
                    kwargs， target的关键字参数

            p.start()
                功能:
                    启动进程
                注意: 启动进程时，子进程才被创建，与子进程绑定的函数才会被执行

            p.join([timeout])
                功能:
                    阻塞等待回收进程
                参数:
                    超时时间

"""

import multiprocessing as mp
from time import sleep


# 进程函数
def fun():
    print("开始一个进程")
    sleep(5)
    print("子进程结束")


# windows中用multiprocessing创建进程必须用if__name__...这样的结构
if __name__ == '__main__':
    mp.freeze_support()  # 只有windows下才要加
    p = mp.Process(target=fun)
    p.start()
    p.join()

"""
上面的代码等同于
pid = os.fork()
if pid == 0:
    fun()
    os.exit()
else:
    os.wait()
"""
