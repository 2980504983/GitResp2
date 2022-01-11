# 题目4：（复读机相加）求s=a+aa+aaa+aaaa+aa…a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。


# 方法一
# 自己琢磨的，看了答案之后发现答案并没有把式子列出来，虽然这种做法列出了式子，但是逻辑过于
# 杂乱

# a = input('请输入要向加的数字:')
# b = int(input('请输入相加的次数:'))
#
# c = 0
# d = 0
# e = a
# print('s = ', end='')
# for i in range(b):
#     d += int(e)
#     e += e[0]
#     c += 1
#     for o in range(i+1):
#         print(a, end='')
#     if c < b:
#         print("+", end='')
#
# h = str(d)
# print(' = ', end=h)

# 方法二
# 看了答案，感觉恍然大悟，自己前面的逻辑绕了一个大弯，结合答案改进
a1 = input('请输入要想加的数字:')
b1 = int(input('请输入要想加的次数:'))

d1 = 0
c1 = 0
print('s = ', end='')
for i in range(b1):
    d1 += int(a1)
    print(a1, end='')
    a1 += a1[0]
    c1 += 1
    if c1 < b1:
        print('+', end='')
print(' = ', end=str(d1))
