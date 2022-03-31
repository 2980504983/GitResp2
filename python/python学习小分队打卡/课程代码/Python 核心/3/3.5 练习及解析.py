"""
    练习: 员工管理器记录多个员工
         迭代员工管理器对象
"""


class Employee:
    pass


class EmployeeIterator:
    def __init__(self, target):
        self.__target = target
        self.__index = -1

    def __next__(self):
        if self.__index >= len(self.__target)-1:
            raise StopIteration
        self.__index += 1
        return self.__target[self.__index]


class EmployeeManager:
    def __init__(self):
        self.__employees = []

    def add_employee(self, emp):
        self.__employees.append(emp)

    def __iter__(self):
        return EmployeeIterator(self.__employees)


manager = EmployeeManager()
manager.add_employee(Employee())
manager.add_employee(Employee())
manager.add_employee(Employee())

# 多态，调用的是九十年前的迭代器协议，实际执行的是EmployeeManager里的__iter__方法
iterator = manager.__iter__()
while True:
    try:
        # 和上面一样，多态
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

