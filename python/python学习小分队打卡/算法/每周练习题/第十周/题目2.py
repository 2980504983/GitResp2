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
