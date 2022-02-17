class Enemy:
    def __init__(self, name, atk, defence, hp):
        self.name = name
        self.atk = atk
        self.defence = defence
        self.hp = hp


list_enemy = [Enemy("灭霸", 15, 15, 100), Enemy("leo", 11, 11, 0)]


def find_all(list_target, func_condition):
    for item in list_target:
        if func_condition(item):
            yield item


re1 = find_all(list_enemy, lambda item: item.name == "灭霸")
for item1 in re1:
    print(item1)

re2 = find_all(list_enemy, lambda item: item.atk > 10)
for item1 in re2:
    print(item1)

re3 = find_all(list_enemy, lambda item: item.hp > 0)
for item1 in re3:
    print(item1)


def find_target(list_target, func_condition):
    for item in list_target:
        if func_condition(item):
            return True
        else:
            return False


def condition(item):
    return item.atk < 5 or item.defence < 10


print(find_target(list_enemy, lambda item: item.name == "成昆"))
print(find_target(list_enemy, condition))
