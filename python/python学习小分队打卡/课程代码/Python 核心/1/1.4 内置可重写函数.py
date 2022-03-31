"""
    内置可重写函数：
        Python中, 以双下划线开头，以双下划线结尾的是系统定义的成员，我们可以再自定义
        的类中进行重写，从而改变其行为。

        __str__函数：将对象转换为字符串 (对人友好)
        __repr__函数：将对象装换为字符串 (解释器可识别)

"""


class StudentModel:
    def __init__(self, name="", age=0, score=0, id=0):
        self.name = name
        self.age = age
        self.score = score
        self.id = id

    # 对象变成字符串 (随意格式)
    def __str__(self):
        return "qtx"

    # 对象变成字符串 (解释器可识别, 有格式要满足python的语法)
    def __repr__(self):
        return "StudentModel('%s', %d, %d, %d)" % (self.name, self.age,
                                                   self.score, self.id)


s01 = StudentModel("无忌", 27, 100, 101)
str01 = str(s01)
print(str01)
print(s01)

str02 = repr(s01)
print(str02)

# 根据字符串执行python代码,执行少量代码
re = eval("1+2*5")
# 执行大量代码
# exec
print(re)

# 下面操作是克隆了一个对象，上面已经创建过无忌对象了，而这里又创建了一个对象，并且填入的信息是
# 完全相同的。所以此时有两个无忌对象
# 这个操作不同于 s02 = s01，s02 = s01只是又创建一个新的内存地址并指向之前创建的对象，只有一个
# 无忌对象
s02 = eval(repr(s01))
print(type(s02))


"""
    练习:
        创建Enemy类对象，将对象打印在控制台中(格式自定)
        克隆Enemy类对象，体会克隆对象变量的改变不影响原变量
    
"""


class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def __str__(self):
        return "%s, %d, %d, %d" % (self.name, self.hp, self.atk, self.defense)

    def __repr__(self):
        return "Enemy('%s', %d, %d, %d)" % (self.name, self.hp, self.atk,
                                            self.defense)


e01 = Enemy('reo', 100, 10, 50)
print(e01)
print(str(e01))  # 效果一样

e02 = eval(repr(e01))  # 克隆e01
e02.name = "weiss"
print(e01)
print(e02)
