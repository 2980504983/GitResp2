"""
请用面向对象思想，描述下列场景：

    张无忌 教 赵敏 九阳神功
    赵敏 教 张无忌 化妆
    张无忌 上班 挣了 10000
    赵敏 上班 挣了 6000
    对象区分数据的不同

    思考：变化点事数据的不同还是行为的不同

请用面向对象思想，描述下列场景：

    玩家攻击敌人，敌人受伤掉血，还可能死亡(掉装备， 加分)
    敌人攻击玩家，玩家受伤后掉血并且碎屏，还可能死亡(游戏结束)
    类区分行为的不同
"""


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def teach(self, obj, skill):
        print(f'{self.__name} 教 {obj} {skill}')

    def work(self, money):
        print(f'{self.__name} 挣了 {money}')


zwj = Person('张无忌')
zm = Person('赵敏')

zwj.teach(zm.name, '九阳神功')
zm.teach(zwj.name, '化妆')

zwj.work(10000)
zm.work(6000)


# ----------------------------------------------------------------------


class Enemy:
    def __init__(self, name, atk, hp):
        self.name = name
        self.atk = atk
        self.hp = hp

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    def damage(self, value):
        self.hp -= value
        print(f'{self.name}扣了{value}滴血')
        if self.hp <= 0:
            self.__death()

    def attack(self, obj):
        print('敌人攻击玩家')
        obj.damage(self.atk)

    # 私有的死亡方法
    def __death(self):
        print('我挂了')
        print('掉装备啦')


class Player:
    def __init__(self, name, atk, hp, point):
        self.name = name
        self.atk = atk
        self.hp = hp
        self.point = point

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    @property
    def point(self):
        return self.__point

    @point.setter
    def point(self, value):
        self.__point = value

    def attack(self, obj):
        print('玩家攻击了敌人')
        # 通过敌人对象地址，调用实例方法
        obj.damage(self.atk)

    def damage(self, value):
        print('玩家受伤')
        self.hp -= value
        if self.hp <= 0:
            self.__death()

    def __death(self):
        print('游戏结束')


p01 = Player('Neo', 10, 100, 0)
e01 = Enemy('ruby', 10, 100)
p01.attack(e01)
