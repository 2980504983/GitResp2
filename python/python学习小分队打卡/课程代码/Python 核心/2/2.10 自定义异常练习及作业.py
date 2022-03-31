"""
    练习:敌人类(攻击力0-100)
        抛出异常的信息:消息/错误行/攻击力/错误编号
"""


class AtkError(Exception):
    def __init__(self, message, code_line, atk, error_number):
        super().__init__("出错啦")
        self.message = message
        self.code_line = code_line
        self.atk = atk
        self.error_number = error_number


class Enemy:
    def __init__(self, atk):
        self.atk = atk

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 0 <= value <= 100:
            self.__atk = value
        else:
            raise AtkError("出错啦", 29, value, 1001)


try:
    e01 = Enemy(100)
except AtkError as e:
    print(e.message)
    print(e.code_line)
    print(e.atk)
else:
    print("执行成功")
