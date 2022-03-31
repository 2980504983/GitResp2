class GraphicManager:
    def __init__(self):
        self.__graphics = []

    def add_graphic(self, graphic):
        self.__graphics.append(graphic)

    def __iter__(self):
        # 执行过程:
        #    1 调用当前方法不执行。(会在内部创建迭代器对象)
        #    2 调用到__next__方法，才执行
        #    3 执行到yield语句，暂时离开
        #    4 再次调用__next__方法，继续执行(就是从离开代码的下一行开始执行)
        #    5 重复 3，4步骤，直至方法__iter__方法执行完毕

        # return GraphicIterator(self.__graphics)
        number = -1
        while number < len(self.__graphics)-1:
            number += 1
            yield self.__graphics[number]


# class GraphicIterator:
#     def __init__(self, target):
#         self.__target = target
#         self.__index = -1
#
#     def __next__(self):
#         if self.__index >= len(self.__target)-1:
#             raise StopIteration
#         self.__index += 1
#         return self.__target[self.__index]


class Graphic:
    def __str__(self):
        return "hello"


manager = GraphicManager()
manager.add_graphic(Graphic())
manager.add_graphic(Graphic())
manager.add_graphic(Graphic())
manager.add_graphic(Graphic())
manager.add_graphic(Graphic())

iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break


"""
    yield --> 生成器
"""


class MyGenerator:
    """
        这是生成器原理
        生成器 = 可迭代对象 + 迭代器
        
        写了yield就会自动生成这些代码
    """
    def __init__(self, stop_value):
        self.begin = 0
        self.stop_value = stop_value

    def __iter__(self):
        return self

    def __next__(self):
        if self.begin >= self.stop_value:
            raise StopIteration
        temp = self.begin
        self.begin += 1
        return temp
        pass


def my_range(stop_value):  # 生成器版本
    number = 0
    while number < stop_value:
        yield number
        number += 1


my01 = my_range(10)
for item in my01:
    print(item)
