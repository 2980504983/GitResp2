# 题目4：打破循环，求输入数字的平方，如果平方运算后小于 50 则退出。

# 方法一
while True:
    a4 = int(input('请输入数字：'))
    print(a4**2)
    if a4**2 <= 50:
        break
