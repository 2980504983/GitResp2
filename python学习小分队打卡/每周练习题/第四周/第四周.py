# 题目1
# 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
# 已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，
# c说他不和x,z比，请编程序找出三队赛手的名单。

# 方法一
# 直接按着逻辑实现代码,思路是创建甲乙两队的列表，分别遍历，在根据限制条件选出名单，这种思路
# 的难点是在遍历的时候，每个队伍的对手不唯一，也就是会同时出现ay, cy类似的情况，
# 所以可以通过确定元素后就将其移除的方法来调整。
listJia = ['c', 'b', 'a']
listYi = ['x', 'y', 'z']
for a in listJia:
    for b in listYi:
        v = a + b
        if v != 'ax' and v != 'cx' and v != 'cz':
            print(f'{v[0]} VS {v[1]}')
            listYi.remove(b)

# 方法二
# 这种方法的思路更清楚，不过解释器有警示信息，而且代码有些地方有些多余和不足，例如开始的信息
# 没必要用集合，删除元素的操作也可以直接在定义的时候选择不添加，不过添加后在删除在逻辑上更贴切
# a=set(['x','y','z'])
# b=set(['x','y','z'])
# c=set(['x','y','z'])
# c-=set(('x','z'))
# a-=set('x')
# for i in a:
#     print(i)
#     for j in b:
#         for k in c:
#             if len(set((i,j,k)))==3:
#                 print('a:%s,b:%s,c:%s'%(i,j,k))

# 改进方法二
a = ['y', 'z']
b = ['x', 'y', 'z']
c = ['y']
for i in a:
    for j in b:
        for k in c:
            if len({i, j, k}) == 3:
                print('a:%s,b:%s,c:%s' % (i, j, k))


# ------------------------------------------------------------------


# 题目2
# 打印出如下图案（菱形）
# 方法一
# 这种方法通过两个遍历来实现，第一个遍历创建一个三角形，第二个
# 遍历创建一个相等的倒三角形，两个三角形组成一个菱形，这种方法long越大菱形越大，
# 可以大到解释器放不下
def line(long):
    c1 = 1
    for a1 in range(long, 0, -1):
        print(' '*a1, end='')
        print('*'*c1)
        c1 += 2
    for b1 in range(0, long+1):
        print(' '*b1, end='')
        print('*'*c1)
        c1 -= 2


line(40)


# 方法二
# 这个方法的菱形的大小是固定的，num的数值改变的是菱形上下的空行的数量
# 注：这种方法num的值必须大于等于1，否则，无法触发退出条件，会造成深度递归，num小于四不会显示
# 菱形
def draw(num):
    a2 = '*'*(2*(4-num)+1)
    # .center()方法，这里指创建一个9格长的横，a为中间的参数，两边用空格填充
    print(a2.center(9, ' '))
    if num != 1:
        draw(num-1)
        print(a2.center(9, ' '))


draw(4)


# -------------------------------------------------------------------


# 题目3
# 斐波那契数列II, 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13…求出这个数列的前20项之和

# 方法一
items = 20
re = 0
mo = 1
de = 2
for item in range(1, items+1):
    re += de/mo
    de, mo = de + mo, de
    # de = de + mo
    # mo = de - mo
    print(re)


# -----------------------------------------------------------------


# 题目4
# 阶乘求和,求1+2!+3!+…+20!的和。

# 方法一
# 用遍历的方法求解，思路是：先将每个数自己的阶乘求出来，再把它们相加
# 遍历1到nums，在将数值num0再次遍历，求出num0的阶乘，在将其全部相加
def sum1(nums):
    b4 = 1
    a4 = 0
    for num0 in range(1, nums+1):
        for num1 in range(1, num0+1):
            b4 *= num1
        a4 += b4
        b4 = 1
    print(a4)


sum1(3)


# 方法二
# 用递归的方法来实现
# def sum2(nums):
#     b = 1
#     a = 0
#     for num0 in range(1, nums+1):
#         b *= num0
#     a += b
#     if nums-1 > 0:
#         sum2(nums-1)
#     print(a)
#
#
# sum2(3)


# 方法三
# 思路很好，先把阶乘化简在求值（有点难理解）
res = 1
for i in range(3, 1, -1):
    res = i * res+1
    print(res)


# --------------------------------------------------------------


# 题目5
# 递归求阶乘,利用递归方法求5!。

# 方法一
# 普通形式
def sum3(nums):
    if nums > 0:
        return nums * sum3(nums-1)
    else:
        return 1


print(sum3(5))


# 方法二
# 特殊的格式实现(三元运算)
#
def factorial(n):
    return n*factorial(n-1) if n > 1 else 1


print(factorial(5))


# 三元运算的一些格式
# def aa():
#     a = 0
#     b = 1
#     c = 2
#     if a > b:
#         print(a)
#     else:
#         return c
# 转化成三元运算的格式(return可以省略)
a = 0
b = 1
c = 2
print(a) if a > b else c

# 三元运算的嵌套
if a > b:
    print(a)
else:
    if b > c:
        print(b)
    else:
        print(c)


print(a) if a > b else print(b) if b > c else print(c)


# ------------------------------------------------------------------


# 题目6
# 递归输出,利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

# 方法一
# 用reversed()方法翻转字符串，在遍历
text = 'YanQingYue'
for a in reversed(text):
    print(a, end='')

print(text[1:])


# 方法二
# 通过字符串的下标以及递归的方法来实现
def rec(string):
    if len(string) != 1:
        # 字符串下标是从零开始的，这里的意思是将去掉开头第一个字母的字符串作为下一次
        # 方法调用的字符串
        rec(string[1:])
    # 这里开始有些不理解，我觉得这里应该只输出一次，就是在输出字符串的最后一个字母的时候代码
    # 就应该结束，后面反应过来了，在输出第一个要打印字母后，代码只是完成了最后一个递归的方法，
    # 还要接着运行前面递归的代码，也就是前面剩下的print.
    print(string[0])


rec(input('string here:'))


# --------------------------------------------------------------------


# 题目7
# 递归求等差数列，有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，
# 他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。
# 最后问第一个人，他说是10岁。请问第五个人多大？

# 方法一
# 方法接收第一个人的年龄，第几个人，年龄差，三个参数
def year(first, people_nums, age_cha):
    first += age_cha
    if people_nums > 2:
        year(first, people_nums-1, age_cha)
    else:
        print(first)


year(10, 5, 2)


# 方法二
def age(n):
    if n == 1:
        return 10
    return 2+age(n-1)


print(age(5))
