# 题目5：（逆序列表）将一个数组逆序列表输出。

# 方法一
# 用第二题的思路解题
a5 = [1, 3, 0, 9, 9, 0]
for a in range(len(a5)):
    for b in range(len(a5)):
        if a5[a] < a5[b]:
            a5[a], a5[b] = a5[b], a5[a]
print(a5)


# 方法二
# sort()方法, 可以给一个reverse参数False或Ture来决定是正序还是倒序
b5 = [1, 0, 3, 5, 4, 2]
b5.sort(reverse=False)
print(b5)


# 方法三
# 这种方法只能将正序的列表改为倒序
lis = [1, 10, 100, 0, 10000, 100000]
for i in range(int(len(lis)/2)):
    lis[i], lis[len(lis)-1-i] = lis[len(lis)-1-i], lis[i]
print('第一种实现：')
print(lis)


# 方法四
# .reverse()反转列表，和方法三有同样的缺陷
lis = [1, 10, 100, 1000, 10000, 100000]
print('第二种实现：')
lis.reverse()
print(lis)
