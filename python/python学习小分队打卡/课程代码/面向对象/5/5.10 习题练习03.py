class PictureController:
    """
    图形管理器类
    管理所有图形
    """
    def calculate_area(self):
        raise NotImplementedError("没有提供面积计算的方法")


class Round(PictureController):
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        return 3.14 * (self.r**2)


class Rectangle(PictureController):
    def __init__(self, long, width):
        self.long = long
        self.width = width

    def calculate_area(self):
        return self.long * self.width


def text_area(picture):
    return picture.calculate_area()


r1 = Round(10)
rect = Rectangle(10, 20)


print(text_area(r1))
print(text_area(rect))


# -------------------------------------------------


class GraphicManager:
    def __init__(self):
        self.__graphics = []

    def add_graphic(self, graphic):
        if isinstance(graphic, Graphic):
            self.__graphics.append(graphic)
        else:
            raise ValueError("值填错了")

    def get_total_area(self):
        total_area = 0
        # 累加每个图形的面积
        for item in self.__graphics:
            total_area += item.calculate_area()
        return total_area


class Graphic:
    def calculate_area(self):
        pass


class Circle(Graphic):
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        return 3.14 * self.r ** 2


class Rectangle(Graphic):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


c01 = Circle(5)
r01 = Rectangle(10, 20)
manager = GraphicManager()
manager.add_graphic(c01)
manager.add_graphic(r01)

res = manager.get_total_area()
print(res)
