# 类
class Friend:
    # 数据成员
    def __init__(self, name, sex):
        # self 是调用当前方法的对象地址
        self.name = name
        self.sex = sex

    # 行为成员
    def play(self):
        """
            一起玩耍
        """
        print(self.name + '玩耍')


# 创建对象, 同时在调用__init__方法
hh = Friend('hh', 22)
# 调用对象的行为
hh.play()
