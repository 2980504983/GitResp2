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
