"""
    模快
"""


# 导入方式1
# 本质：使用变量名module01关联模块地址
# import module01
# module01.fun01()
# my02 = module01.MyClass02()
# my02.fun02()


# 导入方式2
# 出现同名方法本函数中的方法优先级跟高
# 本质：将指定的成员导入到当前模块作用域中
from module01 import fun01
from module01 import MyClass02

def fun01():
    print("我和另一个模快中一个方法的重名，我在调用者前被创建所以会先执行我")

fun01()
my02 = MyClass02()
my02.fun02()


# 导入方式3
# 将模块中的所有成员导入到当前模块作用域中
# 小心导入进来的成员和其他模块的成员冲突
# from module01 import *
# fun01()
# my02 = MyClass02()
# my02.fun02()
