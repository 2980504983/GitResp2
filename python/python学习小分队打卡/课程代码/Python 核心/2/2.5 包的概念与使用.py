"""
    包

python程序结构:
    文件夹(项目根目录)
        包
            模块
                类
                    函数
                        语句

"""

# from 包.模块 import 成员
from pcakage01.module_a import *
fun01()

# from 包.包.模块 import 成员
from pcakage01.package02.module_b import *
fun02()
