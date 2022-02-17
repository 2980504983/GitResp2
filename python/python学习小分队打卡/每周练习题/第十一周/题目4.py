# 题目4：（列表排序、连接）列表排序及连接
a = [2, 6, 8, 0]
b = [7, 0, 4]
# 连接列表
a.extend(b)
a.sort()
print(a)

print(id(a[3]))
print(id(b[1]))
