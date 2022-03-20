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


