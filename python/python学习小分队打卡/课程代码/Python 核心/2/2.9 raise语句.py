"""
    raise
        作用: 抛出一个错误，让程序进入异常状态
        目的: 在层级调用太深时，快速直接的传递错误信息

    自定义异常:
        封装错误信息类(将多个错误信息集成到一个类中,封装错误的数据)


"""


class AgeError(Exception):
    """
        封装错误信息类(将多个错误信息集成到一个类中,封装错误的数据)
    """
    def __init__(self, message, age_value, code_line, error_number):
        super().__init__("错误的显示值")
        self.message = message
        self.age_value = age_value
        self.code_line = code_line
        self.error_number = error_number


class Wife:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 21 <= value <= 31:
            self.__age = value
        else:
            # 1个传递一个信息
            # raise ValueError("我不要")
            # 自定义异常类
            raise AgeError("超过我想要的范围了", value, 26, 1001)


try:
    w01 = Wife(81)
# as获取错误信息
except AgeError as e:
    print("请重新输入:")
    print(e.message)
    print(e.age_value)

