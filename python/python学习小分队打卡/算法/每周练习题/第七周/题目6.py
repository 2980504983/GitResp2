# 题目6：数字比大小，数字比较。

# 方法一
a6 = int(input('请输入要比较的第一个数字：'))
b6 = int(input('请输入要比较的第二个数字：'))

if a6 > b6:
    print(f"{a6} > {b6}")
elif a6 == b6:
    print("%d = %d" % (a6, b6))
else:
    print('{} < {}'.format(a6, b6))

