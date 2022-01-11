"""
    在list_helper中增加通用的获取最大值的方法
"""


def max1(list_target, func_handle):
    temp = 0
    result = None
    for item in list_target:
        if func_handle(item) > temp:
            temp = func_handle(item)
            result = item
    return result
