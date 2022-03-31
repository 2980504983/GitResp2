"""
    运算符重载：
        让自定义的类生成的对象能够使用运算符进行操作
"""


class Vector1:
    def __init__(self, x):
        self.x = x

    # 算数运算符重载
    def __add__(self, other):
        return Vector1(self.x + other)

    def __sub__(self, other):
        return Vector1(self.x - other)

    def __mul__(self, other):
        return Vector1(self.x * other)

    # 反向算数运算符重载
    def __radd__(self, other):
        return Vector1(self.x + other)

    def __rsub__(self, other):
        return Vector1(self.x - other)

    def __rmul__(self, other):
        return Vector1(self.x * other)

    # 复合算数运算符重载
    # (复合算数运算符不写也可以实现 += ，但是会生成新对象，写了之后，是直接在原有对象的基础上进行累加)
    # 用复合算数运算符是为了实现在原对象基础上发生变化
    # 如果不重写__iadd__,默认使用__add__，一般会产生新对象
    def __iadd__(self, other):
        self.x += other
        return self

    # 对象转字符串
    def __str__(self):
        return str(self.x)


v01 = Vector1(10)
print(v01 + 2)  # v01.__add__(2)
print(v01 - 4)  # v01.__sub__(4)
print(v01 * 3)  # v01.__mul__(3)


print(2 + v01)
print(4 - v01)
print(3 * v01)

# 以下操作是修改v01的数据，上面的代码并不修改数据，而是返回一个新的变量
v01 += 3
print(v01)

# 练习：实现自定义类的对象与数值的减法，乘法运算

