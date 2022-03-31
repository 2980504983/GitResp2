"""
    练习1：
    在list_helper中增加通用的求和方法
"""


class Enemy:
    def __init__(self, name, atk, defence, hp):
        self.name = name
        self.atk = atk
        self.defence = defence
        self.hp = hp

    def __str__(self):
        return f"{self.name}"


list_enemy = [Enemy("灭霸", 15, 15, 100), Enemy("leo", 11, 11, 500)]


def summation(list_target, func_condition):
    result = 0
    for item in list_target:
        result += func_condition(item)
    return result


print(summation(list_enemy, lambda item: item.atk))


def filter1(list_target, *args):
    list_result = []
    for item in range(len(args)):
        temp = []
        for item1 in list_target:
            temp.append(args[item](item1))
        list_result.append(temp)
    return list_result


def condition(item):
    return item.atk


def condition1(item):
    return item.name


print(filter1(list_enemy, condition, condition1))


def select(list_target, func_handle):
    for item in list_target:
        yield func_handle(item)


def max1(list_target, func_handle):
    temp = 0
    result = None
    for item in list_target:
        if func_handle(item) > temp:
            temp = func_handle(item)
            result = item
    return result


def get_max(list_target, func_handle):
    max_value = list_target[0]
    for i in range(1, len(list_target)):
        if func_handle(max_value) < func_handle(list_target[i]):
            max_value = list_target[i]
    return max_value


print(max1(list_enemy, lambda item: item.hp))
