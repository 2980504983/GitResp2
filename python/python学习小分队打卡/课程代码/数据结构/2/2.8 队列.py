"""
    队列
        定义:
            只能在尾部存入，头部删除的线性表
        特点:
            1 头出尾进
            2 先进先出，后进后出

        队列的的顺序存储  squeque
            列表的两端哪里作为队列的头，和尾，效率差不多，如果列表的头作为头，添加的时候不用移动数据，
            但是删除的时候要移动，列表的尾作为头则是添加的时候要移动，删除的时候不移动

        队列的链式存储  lqueue

        怎样让队列翻转过来呢？(题目)
            很简单，while 只要队列不为空就出队，并把它们装进一个栈中。
            在 while 只要栈不为空就出栈，并把它们在入队，这样就翻转过来了

"""


class QueueError(Exception):
    pass


class SQueue:
    # 初始化
    def __init__(self):
        self._squeue = []
        self._head = None

    # 判断队列是否为空
    def is_empty(self):
        return self._squeue == []

    # 入队
    def enqueue(self, val):
        self._squeue.append(val)
        self._head = val

    # 出队
    def dequeue(self):
        if not self.is_empty():
            raise QueueError("我不要")
        del self._squeue[0]

    def show(self):
        return self._squeue


queue01 = SQueue()
queue01.enqueue(20)
queue01.enqueue(10)
queue01.enqueue(100)
queue01.dequeue()
queue01.dequeue()
print(queue01.show())
