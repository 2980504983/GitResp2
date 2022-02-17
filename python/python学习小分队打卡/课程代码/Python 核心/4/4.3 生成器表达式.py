"""
    生成器表达式
"""

list01 = [5, "kdsjf", False]


def find01():
    for item in list01:
        if type(item) == int:
            yield item


re = find01()
for item in re:
    print(item)

# 改成生成器表达式版本(注意没有yield)
re1 = (item for item in list01 if type(item) == int)
for item in re:
    print(item)


# 列表推导式版本(与上面的不同，并不是取一次算一次返回一次而是全部都先算好)
re1 = [item for item in list01 if type(item) == int]
for item in re:
    print(item)


# 变量 = [item for item in 可迭代对象 if 条件]  列表推导式
# 变量 = {k,v for k,v in 可迭代对象 if 条件}  字典推导式
# 变量 = {item for item in 可迭代对象 if 条件}  集合推导式
# 变量 = (item for item in 可迭代对象 if 条件)  生成器表达式
