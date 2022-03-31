# 练习一: （使用迭代器原理，遍历元祖）
# ("铁扇公主"， "铁锤公主", "扳手王子")
# 练习二: 不使用for，获取字典所有数据
# {"铁扇公主":101， "铁锤公主":102, "扳手王子":103}


t01 = ("铁扇公主", "铁锤公主", "扳手王子")
iterator = t01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break


d01 = {"铁扇公主": 101, "铁锤公主": 102, "扳手王子": 103}
iterator1 = d01.keys().__iter__()
iterator2 = d01.values().__iter__()
while True:
    try:
        item = iterator1.__next__()
        print(item)
        item = iterator2.__next__()
        print(item)
    except StopIteration:
        break
