"""
    继承 -- 变量
"""


class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    # 子类若没有构造函数， 使用父类的
    # 子类若具有构造函数， 则必须先调用父类的构造函数
    def __init__(self, name, score):
        super().__init__(name)
        self.score = score

    pass


p01 = Person('李四')
print(p01.name)

s01 = Student('张三', 100)
print(s01.score)
print(s01.name)


"""
    定义父类：
        车（数据：速度， 品牌）
        
    定义子类：
        电动车（数据：电池容量， 充电功率）
        
    创建两个对象
    画出内存图
"""


class Car:
    def __init__(self, speed, brand):
        self.speed = speed
        self.brand = brand


class ElectricCar(Car):
    def __init__(self, speed, brand, battery_capacity, charging_power):
        super().__init__(speed, brand)
        self.battery_capacity = battery_capacity
        self.charging_power = charging_power


c01 = Car(10, 'gtr')
e01 = ElectricCar(5, '艾玛', 100, 0.8)

