class Student:
    def __init__(self, name, age, score, sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def display_info(self):
        print(self.name, self.age)
        pass


list01 = [
    Student('苏大强', 68, 62, '男'),
    Student('赵敏', 23, 62, "女"),
    Student('明玉', 30, 95, '女')
]


def find_su():
    for i in list01:
        if i.name == '苏大强':
            i.display_info()


def find_nv():
    for i in list01:
        if i.sex == '女':
            i.display_info()


def find_shu():
    a = 0
    for i in list01:
        if i.age >= 30:
            a += 1
    return a


def zero():
    for i in list01:
        i.score = 0


def find_name():
    b = []
    for i in list01:
        b.append(i.name)
    return b


def find_max():
    max_stu = list01[0]
    for i in range(1, len(list01)):
        if max_stu.age < list01[i].age:
            max_stu = list01[i]
    return max_stu.name


print(find_max())
