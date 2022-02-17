# 题目5：旋转数列
# （有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数）

# 方法一
# 直接饮用collections库中的旋转函数
from collections import *
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
deq = deque(li, maxlen=len(li))
print(li)
""" 向右旋转 deque n 步（默认 n=1）。如果 n 为负，则向左旋转。"""
deq.rotate(int(input('rotate:')))
print(list(deq))

