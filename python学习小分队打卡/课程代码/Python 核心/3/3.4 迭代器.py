"""
    迭代器
"""


class Skill:
    def __str__(self):
        return "hello"
    pass


class SkillIterator:
    def __init__(self, target):
        self.__target = target
        self.__index = -1

    def __next__(self):
        if self.__index >= len(self.__target)-1:
            raise StopIteration
        self.__index += 1
        return self.__target[self.__index]


class SkillManager:
    def __init__(self):
        self.__skill = []

    def add_skill(self, item1):
        self.__skill.append(item1)

    def __iter__(self):
        return SkillIterator(self.__skill)


manager = SkillManager()
manager.add_skill(Skill())
manager.add_skill(Skill())
manager.add_skill(Skill())

iterator = manager.__iter__()

# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break


# --------------------------------------------------------------


class GraphicManager:
    def __init__(self):
        self.__graphics = []

    def add_graphic(self, graphic):
        self.__graphics.append(graphic)

    def __iter__(self):
        return GraphicIterator(self.__graphics)


class GraphicIterator:
    def __init__(self, target):
        self.__target = target
        self.__index = -1

    def __next__(self):
        if self.__index >= len(self.__target)-1:
            raise StopIteration

        self.__index += 1
        return self.__target[self.__index]


class Graphic:
    def calculate_area(self):
        raise NotImplementedError()

    def __str__(self):

        return "hello"


graphic_manager = GraphicManager()
graphic_manager.add_graphic(Graphic())
graphic_manager.add_graphic(Graphic())
graphic_manager.add_graphic(Graphic())
graphic_manager.add_graphic(Graphic())
graphic_manager.add_graphic(Graphic())
graphic_manager.add_graphic(Graphic())
graphic_manager.add_graphic(Graphic())
iterator_graphic = graphic_manager.__iter__()
while True:
    try:
        item = iterator_graphic.__next__()
        print(item)
    except StopIteration:
        break
