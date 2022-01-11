# 定义当前模块那些模块可以被from 模块 import * 导入
__all__ = ["MyClass"]


class MyClass:
    @staticmethod
    def fun03():
        print("MyClass --> fun03")
