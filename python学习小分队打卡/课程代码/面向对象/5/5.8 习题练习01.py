"""
    手雷炸了: 可能伤害敌人/玩家的生命。
            还可能伤害未知事物（鸭子，房子...）
    要求: 增加了新事物，不影响手雷
    体会: 继承的作用
         多态的体现
         设计原则
            开闭原则
            单一职责
            依赖倒置(客户端代码调用抽象的父类)
    画出设计图

    继承：隔离子类的变化，同一概念，约束子类行为
    多态：调用父，执行子
        重写：父类可以通过将方法抛出异常来，约束子类重写方法
    依赖倒置：不调用具体的子类，而是调用抽象的父类


"""


class Grenada:
    """
        手雷类
    """
    def explode(self, biology):
        # 如果不加以判断，即使不是生物的子类也依然可以执行
        # 所以可以用isinstance判断传进来的对象是不是Biology子类的对象
        # 如果对象是生物则执行爆炸逻辑，不是则抛出异常
        if not isinstance(biology, Biology):
            raise ValueError('不是生物的子类')
        biology.get_hurt()


class Biology:
    def get_hurt(self):
        # 如果子类不重写则异常
        # 未实现异常
        raise NotImplementedError()


class Player(Biology):
    def get_hurt(self):
        print('玩家扣血')


class Enemy(Biology):
    def get_hurt(self):
        print('敌人扣血')


# 手雷爆炸，炸到了玩家和敌人
g01 = Grenada()
p01 = Player()
e01 = Enemy()
g01.explode(p01)
g01.explode(e01)
