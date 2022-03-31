"""
    定义员工管理器
        1.管理所有员工
        2.计算所有员工工资

    员工：
        程序员：底薪 + 项目分红
        销售：底薪 + 销售额 * 0.05
        软件测试...
        ...

    要求：增加新岗位，员工管理器不变
"""


class WorkerManager:
    def __init__(self):
        self.__workers = []

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.__workers.append(worker)
        else:
            raise ValueError("值填错了")

    def get_total_salary(self):
        total_salary = 0
        for item in self.__workers:
            total_salary += item.get_salary()
        return total_salary


class Worker:
    def __init__(self, basic_salary):
        self.basic_salary = basic_salary

    def get_salary(self):
        return self.basic_salary


class Programmer(Worker):
    def __init__(self, basic_salary, project_dividend):
        # 爸爸有构造函数，儿子也有，要调用爸爸的构造函数
        super().__init__(basic_salary)
        self.project_dividend = project_dividend

    def get_salary(self):
        return self.basic_salary + self.project_dividend


class Sales(Worker):
    def __init__(self, basic_salary, sales):
        super().__init__(basic_salary)
        self.sales = sales

    def get_salary(self):
        return self.basic_salary + self.sales * 0.05


p01 = Programmer(1000, 500)
s01 = Sales(100, 1000)

manager = WorkerManager()

manager.add_worker(p01)
manager.add_worker(s01)

print(manager.get_total_salary())


# day12作业
# 1.三合一
# 2.根据需求，画出当前练习设计图
# 3.设计员工管理器框架
# 4.将面向过程的购物车，改为面向对象的购物车
# 5.画出天龙八部3D手游技能系统框架图，写出基本框架


# ----------------------------------------------------------
