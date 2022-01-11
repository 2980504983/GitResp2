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
