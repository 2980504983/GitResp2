# # 题目1：(分数归档)利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，
# # 60-89分之间的用B表示，60分以下的用C表示。
# 分数查询
score = int(input("请输入你的分数："))
if 0 <= score <= 100:
    if score >= 90:
        print('A')
    elif 60 <= score < 89:
        print('B')
    else:
        print("C")
else:
    print("请输入正确的分数")

# 将分数批量转化成A，B，C等级
transcript = {'杨紫婉': 99, '严清越': 90, '林千霜': 80, '尹云昕': 85, '杜纨倾': 95,
              '苏亦然': 95}
for key, value in transcript.items():
    if value >= 90:
        transcript[key] = 'A'
    elif 60 <= value < 89:
        transcript[key] = 'B'
    else:
        transcript[key] = "C"

print(transcript)


# 题目2：（输出日期）输出指定格式的日期。
import time
import datetime

# 改变h,m,d等的大小写会有不同的输出效果
print(time.strftime('%Y-%m-%d, %H:%m:%S', time.localtime()))

# 输出今天的时间
print(datetime.date.today())

# 自己设定时间，自动以时间格式输出
print(datetime.date(2333, 2, 3))

# 时间的格式化输出，后面的年月日可更改
print(datetime.date.today().strftime('%d/%m/%Y'))

# 先设定一个时间，在通过函数将其更改在输出
day = datetime.date(1111, 2, 3)
day = day.replace(year=day.year+22)
print(day)


# 题目3：（字符串构成）输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
string = input('请输入字符串：')
alp = 0
num = 0
spa = 0
oth = 0
for item in range(len(string)):
    # 判断字符中遍历的值是否符合条件
    if string[item].isalpha():
        alp += 1
    elif string[item].isalnum():
        num += 1
    elif string[item].isspace():
        spa += 1
    else:
        oth += 1
print('英文字母: {}'.format(alp))
print(f'数字: {num}')
print('空格: %d' % spa)
print('其它: %r' % oth)


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


# 题目5：（完数）一个数如果恰好等于它的因子之和，这个数就称为"完数"。
# 例如6=1＋2＋3.编程找出1000以内的所有完数。
# 方法一
# 遍历1000中的数
for a in range(1, 1000+1):
    # 在每次更换数字a时重置c
    c = 0
    # 在a-1的范围内寻找它的因子b
    for b in range(1, a):
        # 如果b是a的因子且b与a不相等，就让c加上该因子
        if a % b == 0:
            c += b
    # 当因子和c等于a时输出a或c
    if c == a:
        print(a)


# 方法二
# 该方法运用了集合去重的性质
def factor(num):
    # 将输入的值转化成int类型
    target = int(num)
    # 集合存储因子并对其进行去重
    res = set()
    # 寻找在target-1的范围内寻找因子
    for i in range(1, target):
        if target % i == 0:
            # 返回第一个因子
            res.add(i)
            # 返回第二个因子
            res.add(target/i)
    # 返回集合
    return res


# 遍历1000内的数并将其输入factor方法中
for b in range(1, 1001):
    # 如果b等于集合里各数之和减去b,输出b
    if b == sum(factor(b))-b:
        print(b)


# 题目6：（高空抛物）一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# 再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
def high(x, y):
    if y > 0:
        y -= 1
        return high(float(x/2), y)
    else:
        return x


c = int(input("请输入反弹次数："))
h = int(input('请输入原高度：'))
answer = high(h, c)
an = str(answer)
print(f'第{c}次反弹{an}这么高')


# 题目7：（猴子偷桃）猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，
# 又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃
# 了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少
peach = 1
for i in range(9):
    peach = (peach+1)*2
print(peach)
