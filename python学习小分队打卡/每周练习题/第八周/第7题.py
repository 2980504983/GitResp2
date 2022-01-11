# 题目7：（画圈）画图，学用circle画圆形。

# from ...import * 导入一个模块的所有函数，与import...不同的是，调用函数时不用写模块名
from tkinter import *
# 创建一个画布并设置
canvas = Canvas(width=800, height=600, bg='white')
# 布局设置
canvas.pack(expand=YES, fill=BOTH)
k = 1
j = 1
for i in range(26):
    canvas.create_oval(310-k, 250-k, 310+k, 250+k, width=1)
    k += j
    j += 0.3
# 循环显示
mainloop()
