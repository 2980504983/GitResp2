# 用 property(读方法名， 写方法名)，封装变量
class Enemy:
    def __init__(self, name, atk, hp):
        self.name = name
        # 这个变量其实是下面的类变量atk，而atk被property拦截，执行其中的逻辑判断，真正的实例
        # 变量还是方法体中的双下划线变量，可以通过__dict__查看一个实例的所有实例变量
        self.atk = atk
        self.hp = hp

    def get(self):
        return self.name, self.__atk, self.__hp

    def set_atk(self, atk):
        if 10 <= atk <= 50:
            self.__atk = atk
        else:
            raise ValueError('我不要')

    # 创建一个类变量,property拦截对atk变量的读写操作
    atk = property(get, set_atk)

    def set_hp(self, hp):
        if 100 <= hp <= 200:
            self.__hp = hp
        else:
            raise ValueError('我不要')
    # 只能写不能读
    hp = property(None, set_hp)


w01 = Enemy('灭霸', 30, 120)

w01.atk = 45

# 通过__dict__查看该实例的所有实例变量
print(w01.__dict__)

# print(w01.hp)
