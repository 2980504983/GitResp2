# 题目2
# 打印出如下图案（菱形）
# 方法一
# 这种方法通过两个遍历来实现，第一个遍历创建一个三角形，第二个
# 遍历创建一个相等的倒三角形，两个三角形组成一个菱形，这种方法long越大菱形越大，
# 可以大到解释器放不下
def line(long):
    c = 1
    for a in range(long, 0, -1):
        print(' '*a, end='')
        print('*'*c)
        c += 2
    for b in range(0, long+1):
        print(' '*b, end='')
        print('*'*c)
        c -= 2


line(40)


# 方法二
# 这个方法的菱形的大小是固定的，num的数值改变的是菱形上下的空行的数量
# 注：这种方法num的值必须大于等于1，否则，无法触发退出条件，会造成深度递归，num小于四不会显示
# 菱形
def draw(num):
    a = '*'*(2*(4-num)+1)
    # .center()方法，这里指创建一个9格长的横，a为中间的参数，两边用空格填充
    print(a.center(9, ' '))
    if num != 1:
        draw(num-1)
        print(a.center(9, ' '))


draw(4)
