"""
    继承 -- 设计

        开闭原则：
            对拓展开放， 对修改关闭（允许增加新功能，不允许改变原有代码）

        类的单一职责：
            一个类有且只有一个改变它的原因

        依赖倒置：
            客户端代码（调用其它类的类）尽量依赖（使用）抽象的组件
            抽象的是稳定的，现实的是多变的（父类更抽象，子类更具体）

    多态
        父类的同一种行为，在不同的子类上有不同的表现


"""

# 需求: 老张开车去东北
# 变化:    坐飞机
#         坐火车
#         骑车
#         ...

# 违反开闭原则:
#  如果增加火车，需要增加‘火车类’，在修改人类中的go_to方法


class Person:
    def __init__(self, name):
        self.name = name

    def go_to(self, vehicle, str_position):
        if type(vehicle) == Car:
            vehicle.run(str_position)
        elif type(vehicle) == Airplane:
            vehicle.flay(str_position)


class Airplane:
    def flay(self, str_position):
        print('飞机飞到', str_position)


class Car:
    def run(self, str_position):
        print('汽车开到', str_position)


p01 = Person('老张')
c01 = Car()
a01 = Airplane()
p01.go_to(a01, '东北')
p01.go_to(c01, '东北')


# 正确的写法-----------------------


class Vehicle:
    """
        交通工具, 代表所有具体的交通工具
        继承：隔离子类变化，将子类的共性提取到父类中
    """
    def transport(self, str_position):
        # 父类的作用在于调用者能调用它的子类，隔离做与用
        # 父类太过抽象写不出方法体

        pass

# 客户端代码，用交通工具
class Person:
    def __init__(self, name):
        self.name = name

    def go_to(self, vehicle, str_position):
        # 多态：调用父，执行子
        # 看起来是调用父类，实际是执行子类
        vehicle.transport(str_position)


# -------------------以上是架构师完成的，以下是程序员干的---------------------------


class Airplane(Vehicle):
    def transport(self, str_position):
        print('飞机飞到', str_position)


class Car(Vehicle):
    def transport(self, str_position):
        print('汽车开到', str_position)


p01 = Person('老张')
c01 = Car()
a01 = Airplane()
p01.go_to(a01, '东北')
p01.go_to(c01, '东北')
