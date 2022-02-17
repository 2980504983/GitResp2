"""
    创建两个进程
    分别复制文件的上半部分和下半部分到一个新的文件中

    注意: 每执行一次io操作(例如open),系统就记录open生成对象 fd的文件偏移量什么的。
         此时要注意，在父进程中open，创建fd对象，子进程中如果直接调用fd不重新open的话，那么这两
         个进程属于同一个open操作，也就是共享文件偏移量等信息，系统不会额外记录，如果用了open，那么
         系统就会另外记录子进程的fd信息，两个open虽然是对同一个文件的操作，但是互不影响
"""

from multiprocessing import Process
import os

filename = ''
size = os.path.getsize(filename)  # 获取图片大小


# 父进程创建fr，两个子进程使用这个fr会互相影响
fr = open(filename, 'rb')


# 复制上半部分
def top():
    fw = open('top.jpg', 'wb')
    n = size//2
    fw.write(fr.read(n))
    fr.close()
    fw.close()


def bot():
    fw = open('top.jpg', 'wb')
    fr.seek(size//2)  # 移动文件偏移量，移动size//2个字节
    fw.write(fr.read())
    fr.close()
    fw.close()


p1 = Process(target=top)
p2 = Process(target=bot)
p1.start()
p2.start()
p1.join()
p2.join()
