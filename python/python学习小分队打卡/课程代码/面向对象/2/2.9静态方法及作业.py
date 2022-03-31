"""
    静态方法
"""
# 面向过程转面向对象，将函数放到类中，这种函数就是静态方法，静态方法不需要访问类中的数据成员，
# 自成一体用@statimethod装饰

# 总结

# 实例方法：操作对象的数据
# 类方法：操作类的数据(类变量)
# 静态方法：不操作任何类中的数据，自成一体


list01 = [
    ['00', '01', '02', '03'],
    ['10', '11', '12', '13'],
    ['20', '21', '22', '23']
]


class Vector2:
    """
    二维向量表示位置/方向
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def left():
        return Vector2(0, -1)

    @staticmethod
    def right():
        return Vector2(0, 1)

    @staticmethod
    def up():
        return Vector2(-1, 0)

    @staticmethod
    def down():
        return Vector2(1, 0)


class DoubleListHelper:
    # 在二维列表中，获取指定位置的，指定方向，指定数量的元素
    @staticmethod
    def get_elements(target, vect_pos, vect_dir, count):
        list_result = []
        for i in range(count):
            vect_pos.x += vect_dir.x
            vect_pos.y += vect_dir.y
            element = target[vect_pos.x][vect_pos.y]
            list_result.append(element)
        return list_result
        pass


re = DoubleListHelper().get_elements(list01, Vector2(1, 0), Vector2.left(),
                                     2)
print(re)


# 作业部分

# 在二维列表中，获取13位置, 向左三个元素
res01 = DoubleListHelper().get_elements(list01, Vector2(1, 3), Vector2.left(),
                                        3)
print(res01)


# 在二维列表中，获取22位置, 向上两个元素
res02 = DoubleListHelper().get_elements(list01, Vector2(2, 2), Vector2.up(),
                                        2)
print(res02)


# 在二维列表中，获取03位置, 向下两个元素
res03 = DoubleListHelper().get_elements(list01, Vector2(0, 3), Vector2.down(),
                                        2)
print(res03)


# 定义敌人类
    # -- 数据：姓名，血量，基础攻击力，防御力
    # -- 行为：打印个人信息

    # 创建敌人列表(至少四个元素)，并画出内存图
    # 查找姓名是灭霸的敌人对象
    # 查找所有死亡的敌人
    # 计算所有敌人的平均攻击力
    # 删除防御力小于10的敌人
    # 将所有敌人攻击力都增加50


class Enemy:
    def __init__(self, name, hp, ap, df):
        self.name = name
        self.hp = hp
        self.ap = ap
        self.df = df

    def print_info(self):
        print('name: %s, hp: %d, ap: %d, df: %d' %
              (self.name, self.hp, self.ap, self.df))


Enemy_list = [Enemy('Roman', 100, 10, 5),
              Enemy('Cinder', 200, 20, 20),
              Enemy('Neo', 100, 50, 50),
              Enemy('灭霸', 0, 1, 1)
              ]

atk = 0
num = 0
for item in Enemy_list:
    item.ap += 50
    if item.name == '灭霸' and item:
        item.print_info()
    if item.hp == 0 and item:
        print(item.name)
    atk += item.ap
    num += 1

for i in range(len(Enemy_list) - 1, -1, -1):
    if Enemy_list[i].df < 10:
        del Enemy_list[i]


print(atk/num)


