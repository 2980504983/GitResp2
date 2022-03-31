"""
    复习
    View    Controller    Model
    界面      业务逻辑      数据

"""


class XXController:
    def add_xx(self, a):
        print('Controller 添加了数据', a)

    @staticmethod
    def fun01():
        pass


class XXView:
    def __init__(self):
        self.manager = XXController()

    def input_xx(self, a):
        # 需求：调用XXController类中的实例方法add_xx
        self.manager.add_xx(a)

    def input_fun01(self):
        # 需求：调用XXController类中的静态方法fun01
        XXController.fun01()


