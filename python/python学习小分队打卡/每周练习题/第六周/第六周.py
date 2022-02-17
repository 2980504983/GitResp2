# 题目1：（算素数）求100之内的素数。

# 方法一
# 思路是，判断一个数是否除了一和本身之外还能被其他数除尽，如果有就让v加一，最后如果v等于零并且该
# 数字大于一就打印这个数(因为素数是指只能被一和自身整除并且大于一的整数)，每判断完一个数字就把v
# 重置为零
def prime_number(a1):
    for b1 in range(1, a1+1):
        v = 0
        for c in range(2, b1):
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


# -------------------------------------------------------------------


# 题目2：（排序）对10个数进行排序。

# 方法一
# 这种方法通过使用列表的sort()方法（排序的方法）来实现
# 下面用了一个不定长参数，即*args，代表参数长度不确定，可输入的参数数量为 0~n
def px(*args):
    a2 = []
    for item in args:
        a2.append(item)
    a2.sort()
    print(a2)


px(2, 4, 5, 8, 2, 4, 3, 7, 1, 0, -1, -3, -4)


# 方法二
# 这个方法的思路很有意思，通过比较，先后确定列表下标0到9的数字，假设输入了4，3，2，1四个数字
# i = 0
# [4, 3, 2, 1]    # [3, 4, 2, 1]    #[2, 4, 3, 1]    #[1, 4, 3, 2]
# i = 1
# [1, 3, 4, 2]    # [1, 2, 4, 3]
# i = 2
# [1, 2, 3, 4]
raw = []
for i in range(10):
    x = int(input('int%d: ' % i))
    raw.append(x)

for i in range(len(raw)):
    for j in range(i, len(raw)):
        if raw[i] > raw[j]:
            raw[i], raw[j] = raw[j], raw[i]

print(raw)


# ------------------------------------------------------------------


# 题目3：（矩阵对角线之和）求一个3*3矩阵主对角线元素之和。

# 方法一
# 这里有一个比较新奇的用法，mat[][]是指列表里，下标为x的列表里，下标为x的元素
mat = [[1, 2, 3],
       [3, 4, 5],
       [4, 5, 6]
       ]
res = 0
for i in range(len(mat)):
    res += mat[i][i]
print(res)


# ------------------------------------------------------------------


# 题目4：（有序列表插入元素）有一个已经排好序的数组。现输入一个数，
# 要求按原来的规律将他插入数组中。

# 方法一
# 1.append() 向列表末尾增加一个元素。
# 2.extend() 向列表末尾增加多个元素。
# 3.insert()在列表中的任意位置增加一个元素。格式：list.insert(索引, 要添加的元素)
# 这种方法可以检测列表是递增还是递减，在按规律插入数字

c4 = [2, 1, 1, 1]


def pd(s, a4):
    if s[0] <= s[-1]:
        b4 = 0
        for s4 in s:
            if a4 <= s4:
                s.insert(b4, a4)
                break
            elif a4 > s[-1]:
                s.insert(len(s)+1, a4)
                break
            b4 += 1
        print(s)

    elif s[0] > s[-1]:
        b4 = 0
        for s4 in s:
            if a4 >= s4:
                s.insert(b4, a4)
                break
            elif a4 < s[-1]:
                s.insert(len(s) + 1, a4)
                break
            b4 += 1
        print(s)


pd(c4, 0)


# 方法二
# 这种方法的思路是先将要插入的元素直接添加进列表，然后在给列表排序
# 把元素a和列表里的元素从前往后比较，当发现某一元素大于或等于元素a，就从这个元素开始，将后面的
# 元素逐个往最后扔
lis = [1, 10, 100, 1000, 10000, 100000]
n = int(input('insert a number: '))
lis.append(n)
for i in range(len(lis)-1):
    if lis[i] >= n:
        # 这一步的意思是将列表的最后一个元素和第j个元素互换位置
        for j in range(i, len(lis)):
            lis[j], lis[-1] = lis[-1], lis[j]
        break
print(lis)


# ---------------------------------------------------------------------


# 题目5：（逆序列表）将一个数组逆序列表输出。

# 方法一
# 用第二题的思路解题
a5 = [1, 3, 0, 9, 9, 0]
for a in range(len(a5)):
    for b in range(len(a5)):
        if a5[a] < a5[b]:
            a5[a], a5[b] = a5[b], a5[a]
print(a5)


# 方法二
# sort()方法, 可以给一个reverse参数False或Ture来决定是正序还是倒序
b5 = [1, 0, 3, 5, 4, 2]
b5.sort(reverse=False)
print(b5)


# 方法三
# 这种方法只能将正序的列表改为倒序
lis = [1, 10, 100, 0, 10000, 100000]
for i in range(int(len(lis)/2)):
    lis[i], lis[len(lis)-1-i] = lis[len(lis)-1-i], lis[i]
print('第一种实现：')
print(lis)


# 方法四
# .reverse()反转列表，和方法三有同样的缺陷
lis = [1, 10, 100, 1000, 10000, 100000]
print('第二种实现：')
lis.reverse()
print(lis)


# ----------------------------------------------------------------


# 题目6：（类的方法与变量）模仿静态变量的用法。

# 方法一
# 静态变量的定义：静态变量初始化只会被执行一次
# 这个方法里第一个i之所以会一直显示0是因为，每次在打印i之前，i都会被重置，也就是每次遍历虽然
# 加等于一了，但是打印前i都被赋了一个0的值
def dummy():
    i = 0
    print(i)
    i += 1


class Cls:
    i = 0

    def dummy(self):
        print(self.i)
        self.i += 1


a = Cls()
for i in range(50):
    dummy()
    a.dummy()


# 方法二
# 静态变量的定义：静态变量初始化只会被执行一次
# 每个实例对象都能调用静态变量，但是并不能通过实例对象改变静态变量，如果通过实例对象改变静态变量
# 会创造一个新的仅属于该实例的变量，而原来的那个静态变量没变
class Static:
    """定义一个静态变量"""
    a6 = 0


b6 = Static()
c6 = Static()
for i in range(5):
    b6.a6 += 1
    c6.a6 += 2

print(b6.a6)
print(c6.a6)
print(Static.a6)


# ------------------------------------------------------------------


# 题目7：（变量作用域）学习使用auto定义变量的用法。

# 方法一
# 局部变量：
# 定义：在函数内部定义的变量，作用域仅仅限于函数内部
# 1不同函数可以定义同名或同值的局部变量，并且各用各自的，互不影响
#
# 全局变量：
# 与局部变量的区别就是作用域不同
# 1当局部变量和全局变量重复时，优先采用局部变量
# 2如果在函数内部要想对全局变量进行修改的话，必须用global关键字进行声明，也就是用global将局部
# 变量升级为全局变量

i = 0
n = 0


def dummy():
    i = 0
    print(i)
    i += 1


def dummy2():
    global n
    print(n)
    n += 1


print('函数内部的同名变量')
for j in range(20):
    print(i)
    dummy()
    i += 1
print('global声明同名变量')
for k in range(20):
    print(n)
    dummy2()
    n += 10
