"""
    其实顺序存储的栈已经可以满足大部分需求，因为顺序存储的栈只能从后面插入数据，就不存在
    移动一个其他都要动的情况，但是，顺序存储还有一个缺点，就是需要连续的空间，所以当数据非常大
    时，使用顺序存储就不合适了，这时候就要用到链式存储的栈

    顺序栈的栈顶是列表的尾部
    链式栈的栈顶是链表的头部 (如果在尾部的话，每一次操作数据都要遍历到最后一个节点)

    思路分析:
        1. 源于列表的结构
        2. 封装栈的操作方法 (入栈，出栈，栈空，栈顶元素)
        3. 链表的开头作为栈顶 (不用每次遍历)
        4. 不用写头节点了，用一个变量top标记栈顶元素，top指向的元素就是栈顶元素

    把大象关进冰箱:
        面向过程:
            打开冰箱门，把大象放进去，关上冰箱门
        面向对象:
            我有一个大象，找一个人帮我把大象关进冰箱

"""


class Node:
    """
        用于生成节点的类
    """
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkList:
    """
    单链表(线性结构链式存储)
    """
    def __init__(self):
        """
            初始化链表，标记链表的开端，便于获取后续的节点
        """
        self.head = Node(None)

    def init_list(self, list_):
        p = self.head  # 创建指针
        for item in list_:
            p.next = Node(item)  # 在指针后面创建新节点
            p = p.next  # 移动指针

    def show(self):
        p = self.head.next
        while p is not None:
            print(p.val)
            p = p.next

    def is_empty(self):
        if self.head.next is None:
            return True
        else:
            return False

    def clear(self):
        self.head.next = None  # 清空链表，虽然后面的节点依然存在，但是python后面会自动进行 垃圾回收

    # 尾部插入 效率不如列表，链表要遍历到最后，而列表直接加就好了，并不需要移动元素
    def append(self, val):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(val)

    # 头部插入 效率比列表好
    def head_insert(self, val):
        new = Node(val)  # 生成节点
        new.next = self.head.next  # 先让新节点连接head后面的节点
        self.head.next = new  # 在让head指向该节点

    # 指定位置插入()
    def insert(self, index, val):
        p = self.head
        for i in range(index):
            if p.next is None:
                break  # 超出最大范围，就在最后插入
            p = p.next

        node = Node(val)
        node.next = p.next
        p.next = node.next

    # 删除节点
    def delete(self, val):
        p = self.head
        while p.next and p.next.val != val:  # 短路原则
            p = p.next

        if p.next is None:
            raise ValueError("我不要")
        else:
            p.next = p.next.next

    # 获取节点值
    def index(self, index):
        p = self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError("我不要")
            p = p.next
        return p.val


class LStack:  # lstack 表示链式栈
    def __init__(self):
        # 标记栈顶位置
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self, val):
        # node = Node(val)
        # node.next = self._top
        # self._top = node
        # 重构版本
        self._top = Node(val, self._top)

    def pop(self):
        if self._top is None:
            raise Exception("我不要")
        value = self._top.val
        self._top = self._top.next
        return value

    def top(self):
        if self._top is None:
            raise Exception("我不要")
        return self._top.val

