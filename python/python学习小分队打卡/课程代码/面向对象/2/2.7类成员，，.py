class ICBC:
    """
        工商银行
    """
    # 表示总行的钱
    total_money = 1000000

    def __init__(self, name, money):
        self.name = name
        self.money = money
        # 表示从总行中扣除当前支行使用的金额
        ICBC.total_money -= money


i01 = ICBC('广渠门支行', 100000)
i02 = ICBC('陶然亭支行', 100000)
print('总行还剩%d' % ICBC.total_money)


"""
类变量存储在类中，在方法区中
类变量和实例变量并不存在一起，类变量只有一个，被所有对象所共享
"""


"""
类方法，用于操作类变量的方法， 用@classmethod修饰
def 方法名称 （cls， 参数）
    方法体

用@classmethod会自动将类的内存地址传给cls
而不用则是自动将对象的内存地址传给self

类方法中不能访问实例成员，因为类方法没有对象地址self，所以不能访问实例成员
"""