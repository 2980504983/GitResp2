# 题目7：（变量作用域）学习使用auto定义变量的用法。

# 方法一
# 局部变量：
# 定义：在函数内部定义的变量，作用域仅仅限于函数内部
# 1不同函数可以定义同名或同值的局部变量，并且各用各自的，互不影响
#
# 全局变量：
# 与局部变量的区别就是作用域不同
# 1当局部变量和全局变量重复时，优先采用局部变量
# 2如果在函数内部要想对全局变量进行修改的话，必须用global关键字进行声明，也就是用global将局部
# 变量升级为全局变量

i = 0
n = 0


def dummy():
    i = 0
    print(i)
    i += 1


def dummy2():
    global n
    print(n)
    n += 1


print('函数内部的同名变量')
for j in range(20):
    print(i)
    dummy()
    i += 1
print('global声明同名变量')
for k in range(20):
    print(n)
    dummy2()
    n += 10
