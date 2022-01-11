"""
    迭代器 --> yield
    练习: 将迭代器版本的图形管理器改为yield实现
"""

"""
class DigitalIterator:
    def __init__(self, target):
        self.target = target
        self.number = self.target

    def __next__(self):
        if self.number <= 0:
            raise StopIteration
        temp = self.target - self.number
        self.number -= 1
        return temp
"""


class DigitalGeneration:
    def __init__(self, number):
        self.number = number

    def __iter__(self):
        # return DigitalIterator(self.number)
        # 0 --> self.number
        # yield 作用: 将下列代码改为迭代器模式的代码
        # 生成迭代器代码的大致规则:
        # 1 将yield以前的语句定义在next方法中
        # 2 将yield后面的数据作为next方法返回值
        digital = 0
        while digital < self.number:
            yield digital
            digital += 1


# for item in DigitalGeneration(10):
#     print(item)

digital = DigitalGeneration(5)
iterator = digital.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

