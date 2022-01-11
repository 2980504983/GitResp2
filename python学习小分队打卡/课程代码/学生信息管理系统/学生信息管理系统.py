"""
需求：
    实现对学生信息的增加，删除，修改和查询

分析：
    界面可能使用控制台，也可能使用 Web 等

    1. 识别对象：
        界面视图类， 逻辑控制类， 数据模型类

    2. 分配职责：
        界面视图类：负责处理界面逻辑，比如显示菜单，获取输入
        逻辑控制类：负责存储学生信息，处理业务逻辑，比如添加
        数据模型类：定义需要处理的数据模型。比如学生信息(姓名，年龄...)

    3. 建立交互：
        界面视图对象 <----> 数据模型对象 <----> 逻辑控制对象

设计：
    数据模型类：StudentModel
        数据：编号 id， 姓名 name， 年龄 age， 成绩 score

    逻辑控制类：StudentManagerController
        数据：学生列表 __stu_list
        行为：获取列表 stu_list，添加学生 add__student, 删除学生 remove_student
             修改学生 update_student, 根据成绩排序 order_by_score

    界面视图类：StudentManagerView
        数据：逻辑控制对象 __manager
        行为：显示菜单 __display_menu, 选择菜单项__select_menu, 输入学生信息 __input_
             students, 输出学生 __output_students, 删除学生__delete_student，
              修改学生信息 __modify_student, 按成绩输出学生 __output_student

"""


class StudentModel:
    """
        学生信息模型
    """
    def __init__(self, name='', age=0, score=0, id=0):
        """
            创建学生对象
        :param name: 姓名， str
        :param age: 年龄， int
        :param score: 成绩， float
        :param id: 编号 (该学生对象的唯一标识)
        """
        self.name = name
        self.age = age
        self.score = score
        self.id = id


class StudentManagerController:
    """
        学生管理控制器，负责业务逻辑处理
    """
    # 类变量 表示初始编号
    __init_id = 1000

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        """
            学生列表
        :return: 存储学生对象的列表
        """
        return self.__stu_list

    def add__student(self, stu_info):
        """
            添加一个新学生
        :param stu_info: 没有编号的学生信息
        """
        stu_info.id = self.__generate_id()
        self.stu_list.append(stu_info)

    def __generate_id(self):
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

    def remove_student(self, id):
        """
            根据编号删除学生信息
        :param id: 学生编号
        """
        for item in self.stu_list:
            if item.id == id:
                self.stu_list.remove(item)
                return True  # 表示移除成功
            return False  # 表示删除失败

    def update_student(self, stu_info):
        """
            根据stu_info.id修改其他信息
        :param stu_info: 学生对象
        :return: 是否修改成功
        """
        for item in self.stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False

    def order_by_score(self):
        """
            根据学生成绩从低到高排序
        """
        for item0 in range(len(self.__stu_list)):
            for item in range(item0, len(self.__stu_list)):
                if self.__stu_list[item0].score > self.__stu_list[item].score:
                    self.__stu_list[item], self.__stu_list[item0] =\
                        self.__stu_list[item0], self.__stu_list[item]


class StudentManagerView:
    """
        学生管理器视图
    """

    def __init__(self):
        self.__manager = StudentManagerController()

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
            pass

    def __input_student(self):
        name = input('请输入姓名：')
        age = int(input('请输入年龄：'))
        score = int(input('请输入分数：'))
        stu = StudentModel(name, age, score)
        self.__manager.add__student(stu)
        pass

    def __putout_student(self, list_output):
        for item in list_output:
            print(item.id, item.name, item.age, item.score)

    def __remove_student(self):
        id = int(input('请输入学生id：'))
        if self.__manager.remove_student(id):
            print('移除成功')
        else:
            print('删除失败')

    def __modify_student(self):
        stu = StudentModel()
        stu.id = int(input('请输入学生原来的id：'))
        stu.name = input('请输入学生的新姓名：')
        stu.age = int(input('请输入学生的新年龄：'))
        stu.score = int(input('请输入学生的新成绩：'))
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


view = StudentManagerView()
view.main()
