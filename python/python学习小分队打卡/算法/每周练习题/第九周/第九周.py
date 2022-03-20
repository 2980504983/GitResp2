# 题目1：（画线）画图，学用line画直线
# 题目2：（画矩形）画图，学用rectangle画方形
# 题目3：（画图丑）画图，综合例子
# 题目4：（字符串长度）计算字符串长度
# 题目5：（杨辉三角）打印出杨辉三角形前十行
# 题目6：（查找字符串）查找字符串
# 题目7：（画椭圆）使用tkinter画椭圆
# python基础学习
# 看完第二章并完成第二章的检查点
# 爬虫学习
# 看完第三、四章


# 题目1：（画线）画图，学用line画直线

# 方法一
# import tkinter
# # 创建并设置一个画布
# canvas = tkinter.Canvas(width=300, height=300, bg='pink')
# # 确定画布的位置
# canvas.pack()
# # 画一条线，接收x1,x2,y1,y2以及线的宽度五个参数
# canvas.create_line(20, 2000, 20, 20, width=4)
# # 循环显示
# tkinter.mainloop()


# 方法二
# if __name__ == '__main__':
#     from tkinter import *
#
#     canvas = Canvas(width=300, height=300, bg='green')
#     canvas.pack(expand=YES, fill=BOTH)
#     x0 = 263
#     y0 = 263
#     y1 = 275
#     x1 = 275
#     for i in range(19):
#         canvas.create_line(x0, y0, x0, y1, width=1, fill='red')
#         x0 = x0 - 5
#         y0 = y0 - 5
#         x1 = x1 + 5
#         y1 = y1 + 5
#
#     x0 = 263
#     y1 = 275
#     y0 = 263
#     for i in range(21):
#         canvas.create_line(x0, y0, x0, y1, fill='red')
#         x0 += 5
#         y0 += 5
#         y1 += 5
#
#     mainloop()


# -------------------------------------------------------------------


# 题目2：（画矩形）画图，学用rectangle画方形
import tkinter

# 创建并设置画布
canvas = tkinter.Canvas(width=800, height=500, bg='blue')
# 确定画布位置
canvas.pack()
# 创建并设置一个方形
canvas.create_rectangle(10, 200, 300, 400)
# 循环显示
tkinter.mainloop()


# -------------------------------------------------------------------


# 题目3：（画图丑）画图，综合例子
if __name__ == '__main__':
    from tkinter import *
    # 创建一个画布
    canvas = Canvas(width=300, height=300, bg='green')
    # 确定画布的显示位置
    canvas.pack(expand=YES, fill=BOTH)
    x0 = 150
    y0 = 100
    # 创建三个不同的椭圆
    canvas.create_oval(x0 - 10, y0 - 10, x0 + 10, y0 + 10)
    canvas.create_oval(x0 - 20, y0 - 20, x0 + 20, y0 + 20)
    canvas.create_oval(x0 - 50, y0 - 50, x0 + 50, y0 + 50)

    # 导入数学模块
    import math

    B = 0.809
    for i in range(16):
        a = 2 * math.pi / 16 * i
        x = math.ceil(x0 + 48 * math.cos(a))
        y = math.ceil(y0 + 48 * math.sin(a) * B)
        # 画一条线
        canvas.create_line(x0, y0, x, y, fill='red')
    # 画一个椭圆
    canvas.create_oval(x0 - 60, y0 - 60, x0 + 60, y0 + 60)

    for k in range(501):
        for i in range(17):
            a = (2 * math.pi / 16) * i + (2 * math.pi / 180) * k
            x = math.ceil(x0 + 48 * math.cos(a))
            y = math.ceil(y0 + 48 + math.sin(a) * B)
            # 画一条红色的线
            canvas.create_line(x0, y0, x, y, fill='red')

        for j in range(51):
            a = (2 * math.pi / 16) * i + (2 * math.pi / 180) * k - 1
            x = math.ceil(x0 + 48 * math.cos(a))
            y = math.ceil(y0 + 48 * math.sin(a) * B)
            # 画一条红色的线
            canvas.create_line(x0, y0, x, y, fill='red')
    mainloop()


# -------------------------------------------------------------------


# 题目4：（字符串长度）计算字符串长度

# 方法一
# len()方法
str4 = 'red'
str41 = 'blue'
print(len(str4), len(str41))


# 方法二
# 遍历
a = 0
for s in str4:
    a += 1
print(a)


# ------------------------------------------------------------------


# 题目5：（杨辉三角）打印出杨辉三角形前十行

# 方法一
# 通过列表来实现，将第一行作为一个列表存储在一个列表中，然后再根据行数创建新的列表，每个列表的值
# 都是有前一个列表的前两个值相加得到。
def yang_hui(num=10):
    l = [[1]]
    for i in range(1, num):
        l.append([(0 if j == 0 else l[i-1][j-1]) + (0 if j == len(l[i-1])
                else l[i-1][j]) for j in range(i+1)])
    return l


print(yang_hui(10))


# 方法二
# map()接收一个函数，和n个列表，并将函数作用与所有列表
# 这题的思路是，通过将一行的前面加上一个零，在在后面加上一个零，并让两行相加。可以运行一下，我把
# 这两行的打印也加上了
def generate(numRows):
    r = [[1]]
    for i in range(1, numRows):
        r.append(list(map(lambda x, y: x+y, [0]+r[-1], r[-1]+[0])))
        # print((list(map(lambda x, y: x+y, [0]+r[-1], r[-1]+[0]))))
        print(r[-1]+[0])
        print([0]+r[-1])
    return r[:numRows]


a = generate(10)
for i in a:
    print(i)


# --------------------------------------------------------------------


# 题目6：（查找字符串）查找字符串

# 方法一
# 通过find()方法查找字符串， 并返回下标
str6 = input('情输入要查找的字符串：')
str6a = '爱国守法，爱岗敬业'


def find_str():
    a6 = str6a.find(str6)
    if a6 == -1:
        print('没有这个字符')
    else:
        print(f'你输入的字符的下标是{a6}')


find_str()


# --------------------------------------------------------------------


# 题目7：（画椭圆）使用tkinter画椭圆
import tkinter

# 创建一个画布
canvas7 = tkinter.Canvas(height=400, width=400, bg='pink')

# 确定画布的位置
canvas7.pack()

# 画一个椭圆
canvas7.create_oval(200, 400, 80, 150, width=1)

# 循环显示
canvas7.mainloop()


# ------------------------------------------------------------------


# 2.1 程序员的客户是谁？
"""给程序员钱的人"""
# 2.2 什么是软件需求？
"""就是指软件需要实现什么样的功能，有什么要求"""
# 2.3 什么是算法？
"""把需求按照逻辑顺序排好"""
# 2.4 什么是伪码？
"""伪码并不是真实的代码，往往是对需求实现的概括"""
# 2.5 什么是流程图？
"""流程图是用于设计程序的，是以图形的方式来表示程序中应该完成的处理步骤的手段"""
# 2.6 椭圆，平行四边形，矩形在流程图中表示什么意思？
"""椭圆是启动符和终止符，平行四边形是输入符和输出符， 矩形是处理符"""


# 2.7 编写一条显示你姓名的语句
print("YanQingYue")
# 2.8 编写一条显示下列文本的语句(python's the best)
print("python's the best")
# 2.9 编写一条显示下列文本的语句(The cat said "meow")
print('The cat said "meow"')


# 2.10 什么是变量？
"""变量是代表存储在计算机存储器中某个数值的名字"""
# 2.11 在python语言中，下列变量名那些是非法的，为什么？
""" x 合法
    99bottles 非法 第一个字符只能是字母或下划线
    july2009 合法
    theSales 合法
    r&d 非法 不能使用python中的关键字
    grade_report 合法
"""
# 2.12 变量名Sales 和 sales 是指同一个变量吗？为什么是或为什么不是？
"""不是，python中的变量名是区分大小写的，这是两个不同的变量"""
# 2.13 下面这条赋值语句是有效的还是无效的，为什么？(72 = amount)
"""无效的，变量要在左边"""
# 2.14下列代码将显示出什么？(val = 99 /print('The value is', 'val'))
"""显示The value is val"""
# 2.15 判断变量的类型 (value1 = 99， value2 = 45.9)
"""value1 是 int类型， value2 是 float类型"""
# 2.16 请问下列程序将显示什么内容？(val = 99 / val = 0 / print(val))
"""0"""


# 2.22 怎样才能抑制print函数输出结束是的换行？
"""将print中的end参数改为空格"""
# 2.23 如何改变在传给print函数的各个输出项之间自动显示的字符？
"""可以修改print的sep参数"""
# 2.24 转义字符\n的含义是什么？
"""换行符"""
# 2.25 运算符+被用于两个字符串之间时的功能是什么？
"""将两个字符串相连"""
# 2.26 语句显示的结果是什么？(print(format(65.4321, '.2f')))
"""65.43  其中2表示精确的位数，f表示前面数字的类型"""


# 2.27 什么是有名常量？
"""有名常量指的是一个在程序执行过程中数值恒定不变的名字,通常字母都是大写"""
# 2.28 采用有名常量的三个好处是什么？
"""1增强程序的自解释性，2易于程序的大面积修改，3消除点击错误 """
# 2.29 请编写一条python语句来为10%的折扣定义一个有名常量
"""MM = 0.1"""

# 机器龟的猎户座星群程序代码

# 创建伪码
# 第一步 创建一个界面作为猎户座星系
# 第二步 确定猎户座星系上每颗星的名字和对应的坐标
# 第三步 在每个坐标上创建一个点并显示其名字来代表该星
# 第四步 按照一定顺序将每颗星用线连起来


# 代码实现
# 导入机器龟库
import turtle

# 设置界面的大小为500,600
turtle.setup(500, 600)

# 隐藏海龟的路线
turtle.penup()
# 隐藏海龟本体
turtle.hideturtle()

# 设定各星星的坐标(用的是有名常量)

BETE_X = -70
BETE_Y = 200

SAI_X = -90
SAI_Y = -180

TAK_X = -40
TAK_Y = -20

LAM_X = 0
LAM_Y = 0

MINT_X = 40
MINT_Y = 20

MEI_X = 80
MEI_Y = 180

RIGEL_X = 120
RIGEL_Y = -140

# 把星星画出来并显示名字

# 让海龟去到这个坐标
turtle.goto(BETE_X, BETE_Y)
# 生成一个点
turtle.dot()
# 创建名字
turtle.write('Betegeuse')

turtle.goto(SAI_X, SAI_Y)
turtle.dot()
turtle.write('Saiph')
turtle.goto(TAK_X, TAK_Y)
turtle.dot()
turtle.write('Alnitak')
turtle.goto(LAM_X, LAM_Y)
turtle.dot()
turtle.write('Alnilam')
turtle.goto(MINT_X, MINT_Y)
turtle.dot()
turtle.write('Mintaka')
turtle.goto(MEI_X, MEI_Y)
turtle.dot()
turtle.write('Meissa')
turtle.goto(RIGEL_X, RIGEL_Y)
turtle.dot()
turtle.write('Rigel')

# 连线
turtle.pendown()
turtle.goto(MINT_X, MINT_Y)
turtle.goto(MEI_X, MEI_Y)
turtle.penup()
turtle.goto(MINT_X, MINT_Y)
turtle.pendown()
turtle.goto(TAK_X, TAK_Y)
turtle.goto(SAI_X, SAI_Y)
turtle.penup()
turtle.goto(TAK_X, TAK_Y)
turtle.pendown()
turtle.goto(BETE_X, BETE_Y)

# 保持界面(意义相当于mainloop)
turtle.done()
