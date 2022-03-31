"""
    实现协程的第三方库greenlet模块
    安装: sudo pip3 install greenlet
    函数:

    实现协程的gevent模块

"""

# greenlet协程行为示例
from greenlet import greenlet
import gevent
from gevent import monkey
monkey.patch_time()  # 将time中的阻塞变为gevent类型的阻塞，要在time模块导入之前使用
from time import sleep



def fun1():
    print('执行fun1')
    gr2.switch()  # 执行fun2
    print('结束fun1')
    gr2.switch()


def fun2():
    print('执行fun2')
    gr1.switch()  # 执行fun1
    print('结束fun2')


# 将函数变为协程
gr1 = greenlet(fun1)
gr2 = greenlet(fun2)
gr1.switch()  # 选择执行哪一个协程


# -------------------------------------------------------------------


# gevent 协程模块示例
# 协程函数
# gevent与标准库asyncio的不同在于，gevent提供了一个monkey插件，可以修改底层解释io阻塞的行为
# 将很多普通阻塞转换为gevent阻塞

def foo(a, b):
    print('Running foo...', a, b)
    sleep(2)
    print('Foo again..')


def bar():
    print('Running bar...')
    sleep(3)
    print('Foo again..')


# 生成协程对象
f = gevent.spawn(foo, 1, 2)
b = gevent.spawn(bar)

# 阻塞等待f，b两个协程执行完毕
gevent.joinall([f, b])


# 只有gevent只有在遇到gevent指定的阻塞行为是，才会自动的在协程之间跳转，例如gevent.joinall()
# 例如 gevent.sleep()
