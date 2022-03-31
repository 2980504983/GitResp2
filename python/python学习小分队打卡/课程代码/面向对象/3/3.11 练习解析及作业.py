"""
请以面向对象的思想，描述下列场景
        小明在招商银行取钱
        取钱虽然是人的行为，但是取钱的逻辑应该由银行来决定，所以放在银行类中
"""


class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value


class Bank:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value

    def draw_money(self, person, value):
        """
        取钱虽然是人的行为，但是取钱的逻辑应该由银行来决定，所以放在银行类中
        :param person:
        :param value:
        :return:
        """
        self.money -= value
        person.money += value
        print(person.name, '取了%d' % value)


xm = Person('小明', 0)

zsyh = Bank('招商', 100000)
zsyh.draw_money(xm, 10000)
