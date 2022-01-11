"""
    高阶函数：
        将函数作为参数或返回值的函数
    内置高阶函数:

"""
from code_tools.list_helper import *


class Enemy:
    def __init__(self, name, atk, defence, hp):
        self.name = name
        self.atk = atk
        self.defence = defence
        self.hp = hp

    def __str__(self):
        return f"{self.name}"


list_enemy = [Enemy("灭霸", 30, 15, 100), Enemy("leo", 11, 11, 500),
              Enemy("dkjfk", 0, 100, 20)]
# 1.
# 需求：获取所有死人
for item in ListHelper.find_all(list_enemy, lambda item: item.hp == 0):
    print(item)

re = filter(lambda item: item.hp == 0, list_enemy)
for item1 in re:
    print(item1)


# 2.map:将可迭代对象中的每个元素，执行函数，并返回，类型是可迭代对象类型
for item in ListHelper.select(list_enemy, lambda item: item.name):
    print(item)

re = map(lambda item: item.name, list_enemy)
for item in re:
    print(item)

# 3.max ...



