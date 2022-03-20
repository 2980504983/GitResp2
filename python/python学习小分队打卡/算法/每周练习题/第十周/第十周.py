# 第十周
# 题目1：画椭圆、矩形
# （利用ellipse 和 rectangle 画图）
# 题目2：画组合图形
# （一个最优美的图案）
# 题目3：三数排序
# （ 输入3个数a,b,c，按大小顺序输出。）
# 题目4：交换位置
# （输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。）
# 题目5：旋转数列
# （有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数）
# 题目6：报数
# （有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，
# 问最后留下的是原来第几号的那位。）
# 题目7：字符串长度II
# （写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。）
# python基础学习
# 看完第三章并完成第三章的检查点
# 爬虫学习
# python3网络爬虫开发实战，第二章


# 题目1：画椭圆、矩形
# （利用ellipse 和 rectangle 画图）
import tkinter
# 设置并创建画布
canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()
# 在画布上创建一个矩形
canvas.create_rectangle(100, 200, 150, 50)
# 在画布上创建一个椭圆
canvas.create_oval(100, 200, 150, 50)
# 显示画布
tkinter.mainloop()


# ------------------------------------------------------------------


# 题目2：画组合图形
# （一个最优美的图案）


# 方法一
import tkinter

canvas = tkinter.Canvas(width=800, height=800)

canvas.pack()

x1 = 100
x2 = 200
y1 = 300
y2 = 400

for i in range(5):
    canvas.create_oval(x1, x2, y1, y2)
    x1 -= 10
    y1 -= 10
    for s in range(3):
        canvas.create_rectangle(x1, x2, y1, y2)

tkinter.mainloop()


# 方法二
# 好好看
import math
from tkinter import *

class PTS:
    def __init__(self):
        self.x = 0
        self.y = 0
points = []


def LineToDemo():
    screenx = 400
    screeny = 400
    canvas = Canvas(width=screenx, height=screeny, bg='white')

    AspectRatio = 0.85
    MAXPTS = 15
    h = screeny
    w = screenx
    xcenter = w / 2
    ycenter = h / 2
    radius = (h - 30) / (AspectRatio * 2) - 20
    step = 360 / MAXPTS
    angle = 0.0
    for i in range(MAXPTS):
        rads = angle * math.pi / 180.0
        p = PTS()
        p.x = xcenter + int(math.cos(rads) * radius)
        p.y = ycenter - int(math.sin(rads) * radius * AspectRatio)
        angle += step
        points.append(p)
    canvas.create_oval(xcenter - radius, ycenter - radius,
                       xcenter + radius, ycenter + radius)
    for i in range(MAXPTS):
        for j in range(i, MAXPTS):
            canvas.create_line(points[i].x,points[i].y,points[j].x,points[j].y)

    canvas.pack()
    mainloop()


if __name__ == '__main__':
    LineToDemo()


# ---------------------------------------------------------------------------


# 题目3：三数排序
# （ 输入3个数a,b,c，按大小顺序输出。）

# 方法一
a3 = int(input('请输入数字a：'))
b3 = int(input('请输入数字b：'))
c3 = int(input('请输入数字c：'))

d3 = [a3, b3, c3]
d3.sort(reverse=True)
for item in d3:
    print(item, end=',')


# 方法二
# 这种方法作者经常用，应该是一种比较经典的算法
raw = []
for i in range(3):
    x = int(input('int%d: ' % (i)))
    raw.append(x)

for i in range(len(raw)):
    for j in range(i, len(raw)):
        if raw[i] > raw[j]:
            raw[i], raw[j] = raw[j], raw[i]
print(raw)

raw2 = []
for i in range(3):
    x = int(input('int%d: ' % (i)))
    raw2.append(x)
print(sorted(raw2))


# ---------------------------------------------------------------


# 题目4：交换位置
# （输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。）

# 方法一
a4 = True
c4 = 1
d4 = []
while a4:
    b4 = input('请输入数组的第%d个数，输入q退出：' % c4)
    c4 += 1
    if b4 != 'q':
        d4.append(int(b4))
    else:
        a4 = False

"""
1.获取数组最大数和最小数在列表中的位置
2.将最大元素和最小元素分别与第一个和最后一个互换位置
"""
# 获取列表中最大值的位置
h4 = d4[:]
h4.sort()
f4 = h4[-1]
g4 = d4.index(f4)

# 获取列表中的最大值
f4 = h4[0]
i4 = d4.index(f4)

# 将最大元素和最小元素分别与第一个和最后一个互换位置
d4[g4], d4[0] = d4[0], d4[g4]
d4[i4], d4[-1] = d4[-1], d4[i4]
print(d4)


# 方法二
li = [3, 2, 5, 7, 8, 1, 5]

li[-1], li[li.index(min(li))] = li[li.index(min(li))], li[-1]

m = li[0]
ind = li.index(max(li))
li[0] = li[ind]
li[ind] = m

print(li)


# ------------------------------------------------------------------------


# 题目5：旋转数列
# （有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数）

# 方法一
# 直接饮用collections库中的旋转函数
from collections import *
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
deq = deque(li, maxlen=len(li))
print(li)
""" 向右旋转 deque n 步（默认 n=1）。如果 n 为负，则向左旋转。"""
deq.rotate(int(input('rotate:')))
print(list(deq))


# ---------------------------------------------------------------------


# 题目6：报数
# （有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，
# 问最后留下的是原来第几号的那位。）

# 方法一
# 这个方法没写好，写到后面发现把题目搞错了
"""
1.input n的值
2.根据n创建一个1到n的序数列表
3.弹出报到三的元素，重复此操作
4.输出最后留下的数
"""

# n = int(input('请输入n的值：'))
#
# a6 = []
# for i in range(1, n+1):
#     a6.append(i)
#
#
# def fun6(a=1):
#     for s in range(1, len(a6)+1):
#         if s % 3 == 0:
#             print(a6)
#             a6.remove(a6[s-a])
#             a += 1
#     if len(a6) >= 3:
#         fun6()
#
#
# fun6()


# 方法二
if __name__ == '__main__':
    nmax = 50
    n = int(input('请输入总人数:'))
    num = []
    for i in range(n):
        num.append(i + 1)

    i = 0
    k = 0
    m = 0

    while m < n - 1:
        if num[i] != 0: k += 1
        if k == 3:
            num[i] = 0
            k = 0
            m += 1
        i += 1
        if i == n: i = 0

    i = 0
    while num[i] == 0: i += 1
    print(num[i])


# -----------------------------------------------------------------


# 题目7：字符串长度II
# （写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。）

# 方法一
def lenofstr(s):
    return len(s)


print(lenofstr('tanxiaofengsheng'))


# ----------------------------------------------------------------------


# 3.1 控制结构是为了控制一段语句的执行顺序而引入的逻辑结构
# 3.2 程序仅在特定环境下才执行某些语句
# 3.3 仅提供了一条可选择的路径
# 3.4 被if语句测试的表达式
# 3.5 可以用关系运算符测试两个数值间的特定关系
# 3.6 if y > 20: x = 0
# 3.7 if sales >= 10000: commissionrate = 0.2

# 3.8 双分支是当条件为真时执行一条路径，当条件为假时执行一条路径
# 3.9 采用if else来编写双分支
# 3.10 a = 0
# print(a) if a == 0 else a += 1
# 3.11 print()

# 3.13 if number = 1 print(1)

# 3.14 用逻辑符连接的布尔表达式

# 3.15 and一假全假， or一真全真
# 3.16 T F F T F
# 3.17 因为and一假全假 所以只要测试到一个假的，就不会继续测试下去了，or也是同理，这就是短路定值
# 3.18 if speed>0 and speed<200: print(The number is valid)
# 3.19 if not speed>0 and speed<200: print(The number is valid)

# 3.20 Ture 或者 False
# 3.21 布尔变量通常被当做标志变量


# 命中目标游戏
# 伪码
"""
1.创建一个窗口
2.随机生成一个图形作为目标
3.获取机器龟的朝向以及坐标，获取玩家输入的角度和力量值
4.根据角度和力量值判断力量龟是否击中目标
5.显示路线，并返回结果
"""

import turtle
import random

# 创建并设定窗口大小
turtle.setup(500, 600)

# 生成一个任意位置和大小的圆形目标
turtle.hideturtle()
turtle.penup()
target_x = random.randint(-200, 200)
target_y = random.randint(-200, 200)
turtle.goto(target_x, target_y)
turtle.pendown()
turtle.circle(random.randint(10, 90))

# 重新确定机器龟的坐标，并使其走到一定位置上
# 保持界面显示
turtle.done()
