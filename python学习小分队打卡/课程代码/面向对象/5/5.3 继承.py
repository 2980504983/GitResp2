"""
继承 -- 方法
    子类继承父类，可以用父类的方法
    多个类之间在概念上是统一的，就可以在多个子类中抽象出父类(一般先有子类)
    有很多类，类于类之间有很多共性，就可以从这些类中抽象出一个父类，提取共性到父类中
"""

# 多个子类，在概念上是一致的，所以就抽象出一个父类。
# 多个子类的共性，可以提取到父类中
# 在实际开发过程中:
# 从软件设计角度讲：先有子，再有父
# 从编码角度讲：现有父，再有子


class Person:
    def say(self):
        print('说话')
    pass


class Student(Person):
    def study(self):
        print('学习')


class Teacher(Person):
    def teach(self):
        print('讲课')


s01 = Student()
# 子类对象可以调用子类成员，也可以调用父类成员
s01.study()
s01.say()

p01 = Person()
# 父类对象只能调用父类成员，不能调用子类成员
p01.say()

t01 = Teacher()

# python 内置函数

# 1. 判断对象是否属于一个类型
# print(isinstance(t01, Teacher))  # ture
# print(isinstance(t01, Student))  # False
# print(isinstance(t01, Person))  # Ture
#
# # 2. 判断一个类型是否属于一另一个类型
# print(issubclass(Teacher, Student))  # False
# print(issubclass(Teacher, Person))  # Ture
# print(issubclass(Person, Teacher))  # False


"""
定义父类：
    动物（行为：叫）

定义子类：
    狗（行为：跑）
    鸟（行为：飞）
    
创建三个类型对象
体会：isinstance(对象，类型)
体会：issubclass(类型，类型)
"""


class Animal:
    def jiao(self):
        print('叫')


class Dog(Animal):
    def pao(self):
        print("跑")


class Bird(Animal):
    def fly(self):
        print('飞')


a01 = Animal()
d01 = Dog()
B01 = Bird()

# ao1 属于动物吗
print(isinstance(a01, Animal))  # Ture

# 动物属于狗吗
print(issubclass(Animal, Dog))  # False

# a01 属于鸟吗
print(isinstance(a01, Bird))  # False
