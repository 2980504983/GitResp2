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

