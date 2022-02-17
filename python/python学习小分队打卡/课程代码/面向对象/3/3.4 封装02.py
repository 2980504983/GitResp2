class Wife:
    def __init__(self, name, age, weight):
        # 加双下划线隐藏数据
        # 本质：障眼法(实际将变量名改为：_类名__age,但是你看到的是__age)
        self.__name = name

        # 此时这里的数据仍然在限制外，没用通过set_age方法进行限制
        # self.__age = age

        # 这样就可以将数据通过set_age筛查一遍后，在传给构造函数了
        self.set_age(age)
        self.__weight = weight

    # 提供公开的读写方法
    # 用方法操作数据，而不是直接操作数据
    def get_age(self):
        # 类中可以直接访问私有变量
        return self.__age

    def set_age(self, value):
        if 21 < value < 81:
            self.__age = value
        else:
            raise ValueError('我不要')


# w01 = Wife('铁锤公主', 87, 87)

# 此时这里的age相当于创建了一个新的实例变量，并没有访问init中哪个隐藏的age
# w01.__age = 107

# 隐藏了name，所以访问不了name,会显示没有name属性并报错
# print(w01.name)

# 识破障眼法，改变了私有变量(尽量不要改，改了是耍流氓)
# w01._Wife__age = 107

# python内置变量， 存储所有对象的实例变量
# print(w01.__dict__)

w01 = Wife('铁锤公主', 31, 87)

w01.set_age(25)
print(w01.get_age())


# 练习：定义敌人类(姓名，攻击力10-50， 血量100-200)
# 创建一个敌人对象，可以修改和读取数据
# 通过方法封装变量

class Enemy:
    def __init__(self, name, atk, hp):
        self.name = name
        self.set_atk(atk)
        self.set_hp(hp)

    def get(self):
        return self.name, self.__atk, self.__hp

    def set_atk(self, atk):
        if 10 <= atk <= 50:
            self.__atk = atk
        else:
            raise ValueError('我不要')

    def set_hp(self, hp):
        if 100 <= hp <= 200:
            self.__hp = hp
        else:
            raise ValueError('我不要')


Neo = Enemy('Neo', 10, 200)

# 可以绕开限制
Neo._Enemy__hp = 10000

print(Neo.get())
