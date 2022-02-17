"""
    队列的链式结构

    思路分析:
        1 基于链表构建队列模型
        2 链表的开端作为队头，结尾作为队尾
        3 单独定义队尾标记，避免每次插入数据遍历
        4 队头和队尾重叠认为队列为空
"""


class QueueError(Exception):
    pass


class Node:
    """
        用于生成节点的类
    """
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LQueue:
    def __init__(self):
        # 定义队头和队尾的属性变量
        self._front = self._rear = Node(None)

    def is_empty(self):
        return self._front == self._rear

    # 入队
    def enqueue(self, val):
        self._rear.next = Node(val)
        self._rear = self._rear.next

    # 出队
    def dequeue(self):
        if self._front == self._rear:
            raise QueueError("wobuy")
        self._front = self._front.next
        return self._front.val
