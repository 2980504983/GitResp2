"""
    io多路复用，select方法:
        rs, ws, xs = select(rlist, wlist, xlist[, timeout])
        功能:
            监控io事件，阻塞等待io发生
        参数:
            rlist 列表  存放关注的等待发生的io事件(读事件，不知道什么时候发送，需要等待某一条件达成时才发生)
            wlist 列表  存放关注的要主动处理的io事件(写事件，可以主动处理的事件)
            xlist 列表  存放关注的出现异常要处理的io事件
            timeout 超时时间

        返回值:
            rs 列表  rlist中准备就绪的io
            ws 列表  wlist中准备就绪的io
            xs 列表  xlist中准备就绪的io
        注意: wlist中如果存在io事件，则select立即返回给ws处理io过程中不要出现死循环占有服务器
             的情况io多路复用消耗资源较少，效率较高
"""

from select import select
from socket import *

s = socket()
s.bind(('0.0.0.0', 8888))
s.listen(3)

print('监控io')
rs, ws, xs = select([s], [], [], 3)
print("rlist", rs)
print("wlist", ws)
print("xlist", xs)
