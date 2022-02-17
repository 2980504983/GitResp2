class Student:
    def __init__(self, name, age, score, sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def display_info(self):
        print(self.name, self.age)
        pass


list_student_info = []
while True:
    name = input('姓名')
    if name == "":
        break
    age = input('年龄')
    score = input('成绩')
    sex = input('性别')
    # 创建实例
    stu = Student(name, age, score, sex)
    list_student_info.append(stu)
pass

for stu in list_student_info:
    stu.display_info()


