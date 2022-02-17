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


l1 = LinkList()
l2 = LinkList()

l1.init_list([1, 2, 3, 4, 5])
l2.init_list([6, 7, 8, 9, 10])

l1.show()
l2.show()


def merge(l1, l2):
    # 将l2合并到l1中
    p = l1.head
    q = l2.head.next
    while p.next is not None:
        if p.next.val < q.val:
            p = p.next
        else:
            tmp = p.next
            p.next = q
            p = p.next
            q = tmp
    p.next = q

