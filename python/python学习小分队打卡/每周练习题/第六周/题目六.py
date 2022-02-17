# 题目6：（类的方法与变量）模仿静态变量的用法。

# 方法一
# 静态变量的定义：静态变量初始化只会被执行一次
# 这个方法里第一个i之所以会一直显示0是因为，每次在打印i之前，i都会被重置，也就是每次遍历虽然
# 加等于一了，但是打印前i都被赋了一个0的值
# def dummy():
#     i = 0
#     print(i)
#     i += 1
#
#
# class Cls:
#     i = 0
#
#     def dummy(self):
#         print(self.i)
#         self.i += 1
#
#
# a = Cls()
# for i in range(50):
#     dummy()
#     a.dummy()


# 方法二
# 静态变量的定义：静态变量初始化只会被执行一次
# 每个实例对象都能调用静态变量，但是并不能通过实例对象改变静态变量，如果通过实例对象改变静态变量
# 会创造一个新的仅属于该实例的变量，而原来的那个静态变量没变
class Static:
    """定义一个静态变量"""
    a6 = 0


b6 = Static()
c6 = Static()
for i in range(5):
    b6.a6 += 1
    c6.a6 += 2

print(b6.a6)
print(c6.a6)
print(Static.a6)
