# 题目5：函数交换变量，两个变量值用函数互换。

# 方法一
# 这里函数内部的变量值互换并不能影响函数外的x，y的值，还是需要在函数外进行变量值互换
def a5(a, b):
    a, b = b, a


x = 1
y = 0
a5(x, y)
x, y = y, x
print(f'x = {x}')
print(f'y = {y}')


# 方法二
# 这种方法，也是在函数外完成变量的值得交换的
def exc(a9, b9):
    return (b9, a9)


a8 = 0
b8 = 10
a8, b8 = exc(a8, b8)
print(a8, b8)
