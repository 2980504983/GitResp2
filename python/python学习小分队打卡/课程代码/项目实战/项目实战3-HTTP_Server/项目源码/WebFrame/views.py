"""
    数据处理模块，
        这不是mvc模型，是其他模型，这里的views更像是mvc中的c，也就是逻辑控制
"""

import time


def show_time():
    return time.ctime()


def hello():
    return "Hello World"


def bye():
    return "Good Bye"