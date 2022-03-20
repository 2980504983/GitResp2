# 题目5：将一个列表的数据复制到另一个列表中。

# 方法一 copy()方法
listA = ['up', 1, [1, 2, 3], 'i']
a = listA.copy()
print(listA)
print(a)

# 方法二 利用索引
listB = [1, [1, 2, 3], 'i', 'up']
b = listB[:]
print(b)

# 方法三 直接赋值(简单粗暴)
listC = [[1, 2, 3], 'i', 'up', 1]
c = listC
print(c)

# 方法四 通过逻辑实现
listD = ['i', 'up', 1, [1, 2, 3]]
d = []
m = 0
# 当listD的长度大于d的长度时重复执行代码
while len(listD) > len(d):
    # 向d中追加listD里,索引m对应的值
    d.append(listD[m])
    # 每追加一次，索引加一
    m += 1
print(d)
