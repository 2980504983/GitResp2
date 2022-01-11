"""
    界面模块
"""
import bll
import model


class StudentManagerView:
    """
        学生管理器视图
    """

    def __init__(self):
        self.__manager = bll.StudentManagerController()

    def __display_menu(self):
        print('1)添加学生')
        print('2)显示学生')
        print('3)删除学生')
        print('4)修改学生')
        print('5)按照成绩升序显示学生')

    def __select_menu(self):
        item = input('请输入：')
        if item == '1':
            self.__input_student()
        elif item == '2':
            self.__putout_student(self.__manager.stu_list)
        elif item == '3':
            self.__remove_student()
        elif item == '4':
            self.__modify_student()
        elif item == '5':
            self.__output_student_score()
        else:
            print("瞎填是吧")
            pass

    def __input_number(self, message):
        while True:
            try:
                age = int(input(message))
                return age
            except:
                print("输入有误")

    def __input_student(self):
        name = input('请输入姓名：')
        age = self.__input_number("请输入年龄:")
        score = self.__input_number("请输入分数:")
        stu = model.StudentModel(name, age, score)
        self.__manager.add__student(stu)
        pass

    def __putout_student(self, list_output):
        for item in list_output:
            print(item.id, item.name, item.age, item.score)

    def __remove_student(self):
        id = self.__input_number("请输入id:")
        if self.__manager.remove_student(id):
            print('移除成功')
        else:
            print('删除失败')

    def __modify_student(self):
        stu = model.StudentModel()
        stu.id = self.__input_number("请输入新id:")
        stu.name = input('请输入学生的新姓名：')
        stu.age = self.__input_number("请输入新年龄:")
        stu.score = self.__input_number("请输入新成绩:")
        if self.__manager.update_student(stu):
            print('--修改成功--')
        else:
            print('--修改失败--')

    def __output_student_score(self):
        self.__manager.order_by_score()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

