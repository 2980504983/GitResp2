"""
    闭包：
        三要素：
        定义：
            在一个函数内部的函数，同时内部函数又引用了外部函数的变量
        本质：
            闭包是将内部函数和外部函数的执行环境绑在了一起(也就是说，当执行外面函数后，
            会开辟一块栈帧，里面存着变量等数据，但是执行完后并不会立即销毁，因为，在调用该函数
            里的函数时需要外面函数的变量)


"""


def fun01():
    a = 1

    def fun02():
        print(a)
    return fun02


# 调用内嵌函数，返回值是内嵌函数
result = fun01()  # 闭包后，函数
# 调用内嵌函数
result()  # 可以访问外部变量a


# 闭包应用，不支持这样写，更推荐用类来进行逻辑的延续，但是要记住闭包也能进行逻辑的延续，但是不能
# 像类那样对数据进行封装
# 压岁钱
def give_gift_money(money):
    """
        得到压岁钱
    :param money:
    """
    print(f"得到了{money}压岁钱")

    def child_buy(target, price):
        """
            孩子买东西
        :param target: 需要买的东西
        :param price: 商品单价
        """
        nonlocal money
        if money >= price:
            money -= price
            print(f"孩子花了{price}钱，买了{target}")
        else:
            print("钱不够")
    return child_buy


# 下面代码是一个连续的逻辑
action = give_gift_money(10000)
action("唐僧肉", 0.5)
action("手机", 10000)
