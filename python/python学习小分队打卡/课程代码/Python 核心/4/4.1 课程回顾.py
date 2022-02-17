"""
    迭代：
        可迭代对象：具有__iter__方法(iter一般创建一个迭代器对象并返回)
        迭代器：
    生成器

    class 可迭代对象:
        def __iter__():
            创建迭代器对象并返回

    class 迭代器:
        def __next__():
            返回一个元素
            如果没有元素，则抛出一个StopIteration异常

    for 变量 in 可迭代对象:
        变量得到的就是__next__方法的返回值

    原理:
    iterator = 可迭代对象.__iter__()
    while True:
        try:
            变量 = iterator.next()
        except StopIteration:
            break

    启发:
        调用next执行一次，计算一次，返回一次

    生成器函数:
        def 函数名():
            ...
            yield 数据
            ...
        调用方法不执行
        生成器 = 函数名()
        for 生成器 才执行函数体
        for item in 生成器:
            ...
        # 延迟/惰性操作

    生成器源码:
        class 生成器：
            def __iter__():
                return self

            def __next__():
                定义着yield以前的代码
                return yield后面的数据
"""

# 练习: 定义生成器函数my_enumerate,实现下列现象
# list01 = [3, 4, 55, 6, 7]
# for item in enumerate(list01):
#     # (索引，元素)
#     print(item)
#
# for index, element in enumerate(list01):
#     print(index, element)


def my_enumerate(list_target):
    index = 0
    while index <= len(list_target)-1:
        temp = index
        index += 1
        value = (temp, list_target[temp])
        yield value


list01 = [3, 4, 55, 6, 7]
my_enumerate = my_enumerate(list01)

for item in my_enumerate:
    print(item)
