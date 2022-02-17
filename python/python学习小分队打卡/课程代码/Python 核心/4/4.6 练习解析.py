list01 = [43, 4, 5, 5, 6, 7, 87]


def condition01(item):
    return item % 2 == 0


def condition02(item):
    return 10 < item < 50


def find(func_condition):
    for item in list01:
        if func_condition(item):
            yield item


for item1 in find(condition01):
    print(item1)
find(condition02)

