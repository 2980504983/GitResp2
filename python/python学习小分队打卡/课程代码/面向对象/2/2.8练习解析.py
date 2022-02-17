class Student:
    num = 0

    def __init__(self):
        Student.num += 1
        pass

    def yyy(self):
        print(1)
        pass

    @classmethod
    def print_nums(cls):
        print(cls.num)


a = Student()

b = Student()

Student.print_nums()


# 不建议的操作，在__init__()外，创建实例变量
a.name = 'hhh'

# 不建议的操作, 通过类名访问访问实例变量, 需要手动传递self对象地址
Student.yyy(a)

# 不建议的操作， 也可以通过对象地址访问访问类成员
print(a.num)



