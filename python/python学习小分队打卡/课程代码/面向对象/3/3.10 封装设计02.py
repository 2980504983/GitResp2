"""
    封装设计思想
        需求：老张开车去东北
        (因为人和车都有各自的行为，人开东西，车要行驶，因此要做两个类，而东北没有行为，可以那
        字符串表示)
"""


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def go_to(self, str_position, type):
        type.run(str_position)


class Car:
    """
    行驶
    """
    def run(self, str_position):
        print(f'行驶到{str_position}')


lz = Person('老张')
car = Car()
# 老张开车去东北
lz.go_to('东北', car)
