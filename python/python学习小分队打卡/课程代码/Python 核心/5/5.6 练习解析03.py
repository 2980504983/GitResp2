"""
    在list_helper中增加通用的升序排序方法
"""


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


def num(list_target, func_obj):
    for item in range(len(list_target)-1):
        for item1 in range(item+1, len(list_target)):
            if func_obj(list_target[item]) > func_obj(list_target[item1]):
                list_target[item], list_target[item1] = list_target[item1],\
                                                        list_target[item]
    return True


num(list_enemy, lambda item: item.atk)
for item in list_enemy:
    print(item)
