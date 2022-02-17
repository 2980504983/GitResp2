# 题目4：（反向输出II）按相反的顺序输出列表的值。

# 方法一
# reversed()方法，
# 不能像下下行代码那样直接打印，因为reversed()返回的是一个迭代器(我也不是很清楚啥是迭代器)
# 正确的做法是通过for in 来逐个获取里面的值
A4 = [1, 2, 3, 4]
# print(reversed(listA4))
a4 = reversed(A4)
b4 = []
for a in a4:
    b4.append(a)
print(b4)


# 方法二
# 通过下标来实现，这里是借助原有列表，创建一个逆序的列表
# 这种方法更简便一些
listC4 = [5, 6, 7, 8]
d4 = listC4[::-1]
print(d4)
