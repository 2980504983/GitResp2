# 第六周
# 题目1：（算素数）求100之内的素数。
# 题目2：（排序）对10个数进行排序。
# 题目3：（矩阵对角线之和）求一个3*3矩阵主对角线元素之和。
# 题目4：（有序列表插入元素）有一个已经排好序的数组。现输入一个数，
# 要求按原来的规律将他插入数组中。
# 题目5：（逆序列表）将一个数组逆序列表输出。
# 题目6：（类的方法与变量）模仿静态变量的用法。
# 题目7：（变量作用域）学习使用auto定义变量的用法。


# 题目1：（算素数）求100之内的素数。

# 方法一
# 思路是，判断一个数是否除了一和本身之外还能被其他数除尽，如果有就让v加一，最后如果v等于零并且该
# 数字大于一就打印这个数(因为素数是指只能被一和自身整除并且大于一的整数)，每判断完一个数字就把v
# 重置为零
def prime_number(a):
    for b in range(1, a+1):
        v = 0
        for c in range(2, b):
            if b % c == 0:
                v += 1
        if v == 0 and b > 1:
            print(b)


prime_number(1000)


# 方法二
# 思路和方法一类似，也是通过判断一个数是否除了一和本身之外还能被其他数除尽，这种方法里，如果出现
# 了这种情况就停止，如果遍历完了，没出现那种情况就打印那个数
lo = int(input('下限：'))
hi = int(input('上限：'))
for i in range(lo, hi+1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)
