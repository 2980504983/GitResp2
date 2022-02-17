"""
    在list_helper中添加通用的筛选方法
"""


def filter1(list_target, *args):
    list_result = []
    for item in range(len(args)-1):
        temp = []
        for item1 in list_target:
            temp.append(item1.args[item]())
        list_result.append(temp)

