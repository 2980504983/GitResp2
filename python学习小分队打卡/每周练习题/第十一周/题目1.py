# 第十一周
# 题目1：（输入和输出）
# 编写input()和output()函数输入，输出5个学生的数据记录。
# 题目2：（创建链表）创建一个链表
# 题目3：（反向输出链表）反向输出一个链表
# 题目4：（列表排序、连接）列表排序及连接
# 题目5：（不知所云）放松一下，算一道简单的题目。
# （注：不知道这个题目要干嘛~）
# 题目6：（做函数）
# 编写一个函数，输入n为偶数时，调用函数求1/2+1/4+…+1/n,当输入n为奇数时，调用函数1/1+1/3+…
# +1/n
# 题目7：（遍历列表）循环输出列表
# python基础学习
# 看完第四章并完成第四章的检查点
# 爬虫学习
# python3网络爬虫开发实战，第三章

# 题目1：（输入和输出）
# 编写input()和output()函数输入，输出5个学生的数据记录。
# 方法一
e = []


def output():
    a = int(input('请输入学生的数量：'))
    for i in range(1, a+1):
        b = input(f'请输入第{i}个学生的姓名：')
        c = input(f'请输入第{i}个学生的学号：')
        d = input(f'请输入第{i}个学生的成绩：')
        e.append([])
        e[i-1].append(b)
        e[i-1].append(c)
        e[i-1].append(d)


if __name__ == '__main__':
    output()
    print(e)


# 方法二
N = 3
# stu
# num : string
# name : string
# score[4]: list
student = []
for i in range(5):
    student.append(['', '', []])


def input_stu(stu):
    for i in range(N):
        stu[i][0] = input('input student num:\n')
        stu[i][1] = input('input student name:\n')
        for j in range(3):
            stu[i][2].append(int(input('score:\n')))


def output_stu(stu):
    for i in range(N):
        print('%-6s%-10s' % (stu[i][0], stu[i][1]))
        for j in range(3):
            print('%-8d' % stu[i][2][j])


if __name__ == '__main__':
    input_stu(student)
    print(student)
    output_stu(student)
