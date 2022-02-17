"""
    二叉树的存储结构:  二叉树bitree

        二叉树的顺序存储:
            1 空节点用None表示

            2 非空二叉树用包含三个元素的列表[d,l,r]表示，其中d表示根节点(用于存储数据)，l,r
              表示左子树和右子树

            3 如果二叉树的结构比较稀疏的话，很浪费空间，因此一般只有满二叉树的情况，才会考虑
              用二叉树的顺序存储

        二叉树的链式存储:
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


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BiTree:
    def __init__(self, root):
        self.root = root

    # 先序遍历
    def pre_order(self, node):
        if node is None:  # 中止条件
            return
        print(node.val)
        self.pre_order(node.left)
        self.pre_order(node.right)

    # 中序遍历
    def in_order(self, node):
        if node is None:  # 中止条件
            return
        self.in_order(node.left)
        print(node.val)
        self.in_order(node.right)

    # 后序遍历
    def post_order(self, node):
        if node is None:  # 中止条件
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.val)

    # 层次遍历，就是一层一层向下遍历，顺序是先左后右
    def level_order(self, node):
        sq = SQueue()
        sq.enqueue(node)  # 初始节点入队
        while not sq.is_empty():
            node = sq.dequeue()
            # 打印出队元素
            print(node.val)
            if node.left:
                sq.enqueue(node.left)
            if node.right:
                sq.enqueue(node.right)


if __name__ == "__main__":
    # B F G D I H E C A
    # 根据后续遍历构建二叉树
    b = Node('B')
    f = Node('F')
    g = Node('G')
    d = Node('D', f, g)
    i = Node('I')
    h = Node('H')
    e = Node('E', i, h)
    c = Node('C', d, e)
    a = Node('A', b, c)

    # 将a作为起始位置
    bt = BiTree(a)

    bt.pre_order(bt.root)
