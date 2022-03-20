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


# --------------------------------------------------------------------------


# 题目2：（创建链表）创建一个链表

# 作者的方法有点没看懂，啥意思，找了找，链表的介绍，链表是一种数据结构，是一种方便修改的线性数据

'''
单链表的基本操作：
 1、验证链表里面有没有值！
 2、从头部插入数值！
 3、从尾部插入数值！
 4、按指定位置插入数值！
 5、删除操作！
 6、查找一个节点是否在链表中！
 7、按下标查找节点处的数值！
 8、给链表排序！
 9、修改！
'''


# 创建节点
class Node(object):
    def __init__(self, item):
        self.element = item
        self.next = None


# 创建单链表类
class SingleLinkList(object):
    def __init__(self):
        self.header = None
        self.length = 0

    # 1、判断是否为空
    def is_empty(self):
        if self.header == None:
            return True
        else:
            return False

    # 2、头部插入
    def add(self, node):
        if self.is_empty():
            self.header = node
        else:
            node.next = self.header
            self.header = node
            # currentNode = self.header
        self.length += 1

    # 3、尾部插入
    def append(self, node):
        current_Node = self.header
        if self.is_empty():
            self.add(node)
        else:
            while (current_Node.next != None):
                current_Node = current_Node.next
            current_Node.next = node
            self.length += 1

    # 4、指定位置插入
    def insert(self, node, index):
        current_Node = self.header

        if index > self.length + 1 or index <= 0:
            while (index > self.length + 1 or index <= 0):
                print("你要插入的位置不对，请重选位置:")
                index = eval(input())

        if index == 1:
            self.add(node)
        elif index == 2:
            node.next = self.header.next
            self.header.next = node
            self.length += 1
        else:
            for i in range(1, index - 1):
                current_Node = current_Node.next
            node.next = current_Node.next
            current_Node.next = node
            self.length += 1

    # 5、遍历
    def travel(self):
        current_Node = self.header
        if self.length == 0:
            print("目前链表没有数据！")
        else:
            print("目前链表里面的元素有:", end=" ")
            for i in range(self.length):
                print("%s " % current_Node.element, end=" ")
                current_Node = current_Node.next
            print("\n")

    # 6、排序不用交换节点的位置，只需要交换节点上的数据值
    def list_sort(self):
        for i in range(0, self.length - 1):
            current_Node = self.header
            for j in range(0, self.length - i - 1):
                if current_Node.element > current_Node.next.element:
                    temp = current_Node.element
                    current_Node.element = current_Node.next.element
                    current_Node.next.element = temp

                current_Node = current_Node.next

    # 7、按索引删除
    def delete(self, index):
        if index <= 0 or index > self.length:
            while (index <= 0 or index > self.length):
                print("你输入的下标不对，请重新输入需要删除的值的下标：")
                index = eval(input())
            #   return
        else:
            if index == 1:
                self.header = self.header.next
                currentNode = self.header
            elif index == 2:
                current_Node = self.header
                current_Node.next = current_Node.next.next
            else:
                current_Node = self.header
                for i in range(1, index - 1):
                    current_Node = current_Node.next
                current_Node.next = current_Node.next.next
        self.length -= 1

    # 8、查找是否包含,并返回下标
    def isContain(self, num):
        contain = 0
        current_Node = self.header
        for i in range(self.length):
            if current_Node.element == num:
                print(
                    "%d在链表中%d处\n" % (num, i + 1))  # i+1是在正常人认为的位置处，程序员一般是从0开始算起
                contain = 1
            current_Node = current_Node.next
        if contain == 0:
            print("%d不在链表中\n" % num)

    # 9、根据下标找节点
    def searchNodeByIndex(self, index):
        current_Node = self.header
        if index <= 0 or index > self.length:
            while (index <= 0 or index > self.length):
                print("你输入的下标不对，请重新输入:")
                index = eval(input())
            #   return 0
        if index > 0 or index <= self.length:
            for i in range(index - 1):
                current_Node = current_Node.next
            return current_Node

    # 10、根据下标修改节点的值
    def Alert(self, index, num):  # index定义为下标
        current_Node = self.header
        if index <= 0 or index > self.length:
            print("你输入的下标不对，请重新输入!\n")
        else:
            for i in range(index - 1):
                current_Node = current_Node.next
            current_Node.element = num


def main():
    # 创建一个节点对象
    node1 = Node(1)
    # 创建一个单链表对象
    single_link_list = SingleLinkList()  # 实例化

    print('''
          *******************************************************************
          *****************请选择相应的序号完成相应的操作*************************
          *******************************************************************
          **         0、结束所有操作！！！！！！                              ***
          **         1、验证链表里面有没有值！                                ***
          **         2、从头部插入数值！                                     ***
          **         3、从尾部插入数值！                                     ***
          **         4、按指定位置插入数值！                                  ***
          **         5、删除操作！                                          ***
          **         6、查找一个节点是否在链表中！                             ***
          **         7、按下标查找节点处的数值！                               ***
          **         8、给链表排序！                                         ***
          **         9、修改！                                              ***
          ********************************************************************
          ''')
    while True:
        number = eval(input("——————输入下一步要进行的相应操作序号——————："))
        if (number == 1):
            print("正在验证链表里面有没有值：")
            single_link_list.travel()
            print("\n")

        if (number == 2):
            print("目前的链表状态。")
            single_link_list.travel()
            print("正在从头部插入数值：")
            node1 = Node(eval(input("输入要插入的值:")))  # 从头部插入数值
            single_link_list.add(node1)
            print("操作后链表的状态。")
            single_link_list.travel()

        if (number == 3):
            print("目前的链表状态。")
            single_link_list.travel()
            print("正在尾部插入数值：")
            node2 = Node(eval(input("输入要插入的值:")))
            single_link_list.append(node2)
            print("操作后链表的状态。")
            single_link_list.travel()

        if (number == 4):
            print("目前的链表状态。")
            single_link_list.travel()
            print("正在按指定位置插入数值：")
            node3 = Node(eval(input("输入插入的数：")))
            position = eval(input("输入要插入到的位置为："))
            single_link_list.insert(node3, position)
            print("操作后链表的状态。")
            single_link_list.travel()

        if (number == 5):
            print("目前的链表状态。")
            single_link_list.travel()
            print("正在删除：")
            single_link_list.delete(eval(input("输入要删除哪个位置的数：")))
            print("操作后链表的状态。")
            single_link_list.travel()

        if (number == 6):
            print("目前的链表状态。")
            single_link_list.travel()
            print("正在查找一个节点是否在链表中：")
            single_link_list.isContain(eval(input("输入要验证的数：")))

        if (number == 7):
            print("正在按下标查找节点处的数值：")
            node = single_link_list.searchNodeByIndex(
                eval(input("输入下标值：")))  # 查找某节点处的值
            print("这个位置的值为：%s" % node.element)

        if (number == 8):
            print("目前的链表状态。")
            single_link_list.travel()
            print("正在排序：")
            single_link_list.list_sort()
            print("操作后链表的状态。")
            single_link_list.travel()

        if (number == 9):
            print("目前的链表状态。")
            single_link_list.travel()
            print("正在修改（这是在上面排序后的前提下修改。）：")
            index = eval(input("输入要修改的得位置："))  # 修改的下角标
            num = eval(input("输入要修改为的数："))  # 要修改成的那个数
            single_link_list.Alert(index, num)
            print("操作后链表的状态。")
            single_link_list.travel()  # 遍历一遍

        if number == 0:
            break


if __name__ == '__main__':
    main()


# -----------------------------------------------------------------------


# 题目3：（反向输出链表）反向输出一个链表
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

class List:

    def __init__(self, head):
        self.head = head

    def is_empty(self):
        return self.get_len() == 0

    def get_len(self):
        length = 0
        temp = self.head
        while temp is not None:
            length += 1
            temp = temp.next
        return length

    def append(self, node):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = node

    def delete(self, index):
        if index < 1 or index > self.get_len():
            print("给定位置不合理")
            return
        if index == 1:
            self.head = self.head.next
            return
        temp = self.head
        cur_pos = 0
        while temp is not None:
            cur_pos += 1
            if cur_pos == index-1:
                temp.next = temp.next.next
            temp = temp.next

    def insert(self, pos, node):
        if pos < 1 or pos > self.get_len():
            print("插入结点位置不合理")
            return
        temp = self.head
        cur_pos = 0
        while temp is not Node:
            cur_pos += 1
            if cur_pos == pos-1:
                node.next = temp.next
                temp.next =node
                break
            temp = temp.next

    def reverse(self, head):
        if head is None and head.next is None:
            return head
        pre = head
        cur = head.next
        while cur is not None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        head.next = None
        return pre

    def print_list(self, head):
        init_data = []
        while head is not None:
            init_data.append(head.get_data())
            head = head.next
        return init_data

if __name__=='__main__':
    head=Node('head')
    link=List(head)
    for i in range(10):
        node=Node(i)
        link.append(node)
    print(link.print_list(head))
    print(link.print_list(link.reverse(head)))


# -----------------------------------------------------------------------


# 题目4：（列表排序、连接）列表排序及连接
a = [2, 6, 8, 0]
b = [7, 0, 4]
# 连接列表
a.extend(b)
a.sort()
print(a)

print(id(a[3]))
print(id(b[1]))


# -------------------------------------------------------------------


# 题目6：（做函数）
# 编写一个函数，输入n为偶数时，调用函数求1/2+1/4+…+1/n,当输入n为奇数时，调用函数1/1+1/3+…
# +1/n

# 方法一
def func6():
    a6 = int(input('请输入数字：'))
    s6 = 0
    d6 = 2
    if a6 % 2 == 0:
        for i6 in range(a6//2):
            s6 += 1/d6
            d6 += 2
        print(s6)
    else:
        for item in range(a6//2):
            s6 += 1/(d6-1)
            d6 += 2
        print(s6)


func6()


# 方法二
def peven(n):
    i = 0
    s = 0.0
    for i in range(2, n + 1, 2):
        s += 1.0 / i
    return s


def podd(n):
    s = 0.0
    for i in range(1, n + 1, 2):
        s += 1.0 / i
    return s


def dcall(fp, n):
    s = fp(n)
    return s


if __name__ == '__main__':
    n = int(input('input a number: '))
    if n % 2 == 0:
        sum = dcall(peven, n)
    else:
        sum = dcall(podd, n)
    print(sum)


# -----------------------------------------------------------------


# 题目7：（遍历列表）循环输出列表

# 方法一 直接输出列表中的所有元素
a7 = [1, 2, 3]
for item in a7:
    print(item)

# 方法二 根据索引值打印全部列表元素
l = ['moyu', 'niupi', 'xuecaibichi', 'shengfaji', '42']
for i in range(len(l)):
    print(l[i])
