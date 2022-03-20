import time
import datetime


# 题目1： 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，
# 可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间
# 时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

i = int(input('请输入当月利润（单位为万元）：'))

if i <= 10:
    i *= 0.1
    print(f"当月奖金为{i}万元")
elif 10 < i <= 20:
    a = 1 + ((i-10)*0.075)
    print(f"当月奖金为{a}万元")
elif 20 < i <= 40:
    a = 1.75 + ((i-20)*0.05)
    print(f"当月奖金为{a}万元")
elif 40 < i <= 60:
    a = 2.75 + ((i-40)*0.03)
    print(f"当月奖金为{a}万元")
elif 60 < i <= 100:
    a = 3.35 + ((i-60)*0.015)
    print(f"当月奖金为{a}万元")
elif i > 100:
    a = 3.95 + ((i-100)*0.01)
    print(f"当月奖金为{a}万元")


# 题目2：题目 一个整数，它加上100后是一个完全平方数，
# 再加上168又是一个完全平方数，请问该数是多少？

# 网上看的做法
for i in range(1, 1000):
    for j in range(1, 1000):
        for k in range(1, 1000):
            if (i+100) == j*j and (i+268) == k*k:
                print(i)

# 发现网上的做法显示的很慢，而且貌似要占用很多资源，于是改进
for A in range(1, 1000):
    for a in range(1, 1000):
        if A + 100 == a * a:
            for b in range(1, 1000):
                if A + 268 == b * b:
                    print(A)

# # 老刘的做法
# jieguo=[]
# for i in range(1000):
#     flag1 = 0
#     f2 = 0
#     x1 = i+100
#     x2 = x1 + 168
#     for m in range(1000):
#         if x1 == m * m:
#             flag1 = 1
#             break
#     for n in range(10):
#         if x2 == (m+n) * (m+n):
#             f2 = 1
#             break
#     if flag1 == 1 and f2 == 1:
#         jieguo.append(i)
# print(f"这个数字是{jieguo}")

# # 看了老刘的做法，发现,如果：a * a == x + 100, b * b == x + 268, 那么(b * b) -
# # (a * a) == 168, 从这里发现，a与b的差值并不大，而且因为b平方数更大，所以当a,b的值改变时,
# # b的数值变化是小于a的，b-a会随着a的增大而减小，而根据a * a == x + 100可以得出a的范围,
# # a至少应该大于或等于10，所以在带入a = 10 得到b * b == 268 b大概等于17 差值为7，
# # 所以不需要遍历一千次去寻找第二个平方数，只需要将前一个平方数加上7的范围内寻找即可。
for A in range(1, 1000):
    for a in range(1, 1000):
        if A + 100 == a * a:
            for b in range(1, 7):
                if A + 268 == (a+b) * (a+b):
                    print(A)


# 题目3：暂停一秒输出，并格式化当前时间。（与上周稍微有差别，这个要格式化哈）
# 方法一
a = 0
while a <= 10:
    """利用time模块中的方法实现格式化本地时间"""
    print(time.strftime('%Y-%m-%d, %H:%m:%S', time.localtime()))
    a += 1
    # 每输出一次数据暂停一秒
    time.sleep(1)

# 方法二
a = 0
while a <= 10:
    """利用datetime模块可以省去格式化的功夫，但是后面有一串意义不明的小尾巴"""
    print(datetime.datetime.now())
    a += 1
    time.sleep(1)


# 题目4：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

month = int(input('繁殖第几个月?:'))
month1 = 1
month2 = 0
month3 = 0
month_e = 0
for i in range(1, month+1):
    month1, month2, month3, month_e = month_e + month3, month1, month2, \
                                       month_e + month3
    print(f'第{i}个月共, {month1 + month2 + month3 + month_e}, 对兔子')


# 题目5：判断101-200之间有多少个素数，输出所有素数。
# 思路是先根据能被除一和自身整除，求非素数，在将这些数添加到列表，在与101到200的列表求补集，
# 但是结构不符合预期，看了半天逻辑好像也没错，有些蒙
a = 0
listA = []
listB = list(range(101, 201))
for i in range(101, 201):
    for b in range(1, 201):
        if i % b == 0:
            if b != i and b != 1:
                listA.append(i)
                a += 1
print(set(listA))
# c = list(set(listB) - (set(listA)))
# print(c)


# 题目6：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

# 方法一
# 分别在1到10，0到10，0到10的范围内寻找数字的百位，十位和个位，当满足水仙花数的条件时就输出
for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            if a**3 + b**3 + c**3 == 100*a + 10*b + c:
                print(f'{a}{b}{c}')

# 方法二
# 遍历所有三位数，通过索引来判断三位数的个位十位和百位是否符合水仙花数的条件
for i in range(100, 1000):
    s = str(i)
    one = int(s[-1])
    ten = int(s[-2])
    hun = int(s[-3])
    if i == one**3+ten**3+hun**3:
        print(i)


# 题目7：将一个整数分解质因数。例如：输入90,打印出90=233*5。

a = int(input('输入一个整数：'))
print(a, ' = ', end='')
if a < 0:
    target = abs(a)
    print('-1*', end='')
flag = 0
if a <= 1:
    print(a)
    flag = 1
while True:
    if flag:
        break
    for i in range(2, int(a+1)):
        if a % i == 0:
            print("%d" % i, end='')
            if a == i:
                flag = 1
                break
            print('*', end='')
            a /= i
            break
