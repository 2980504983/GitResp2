# 题目1：（反向输出）给一个不多于5位的正整数，要求：一、求它是几位数，二、
# 逆序打印出各位数字。

# 方法一
# 直接打印c会显示内存地址, 应该用list()把c转化成一个列表在输出
def a1(num):
    if 0 <= num < 100000:
        b1 = str(num)
        c = reversed(b1)
        print(f'它是{len(b1)}位数,倒着打印:', end='')
        for i in c:
            print(i, end='')
    else:
        print('请输入一个不多于5位的正整数。')


a1(10000)


# 方法二
# 这种方法通过字符串的下标来翻转数字，相比与用reversed()会更简洁和方便
n = int(input('\n输入一个正整数：'))
if 0 <= n < 100000:
    n = str(n)
    print('%d位数' % len(n))
    print(n[::-1])
else:
    print('请输入一个不多于5位的正整数。')


# -----------------------------------------------------------------


# 题目2：（回文数）一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，
# 十位与千位相同。

# 方法一
# 这里的回文数貌似并不需要数字完全连续，所以直接判断字符串的正序和倒序是否相等就行了
a2 = input('请输入数字：')
if a2 == a2[::-1]:
    print(f'{a2}是回文数')
else:
    print(f'{a2}不是回文数')


# 方法二
# 这种方法的思路是，从数字的第一个数字和最后一个数字开始一起向内，
# 两个两个进行比较，看是否相等，如果有不相等的，就输出不是，反之就是
n = input("随便你输入啥啦：")
a = 0
b = len(n)-1
flag = True
while a < b:
    if n[a] != n[b]:
        print('不是回文串')
        flag = False
        break
    a, b = a+1, b-1
if flag:
    print('是回文串')


# ----------------------------------------------------------------


# 题目3：（字母识词）请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，
# 则继续判断第二个字母。

# 方法一
# 先判断是否是有两种可能的字母，如不是，判断字母与星期几的首字母相同，就打印星期几
# 如是，就在判断。这种方法代码显得比较臃肿,lower()方法是把输入字母变成小写，
# 这样就算输入大写的字母也能判断
weekday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday',
           'saturday', 'sunday']
s3 = input('请输入第一个字母：')
for item in weekday:
    if s3.lower() == 't':
        s4 = input('你输入的字母有两种可能，请再输一个：')
        if s4.lower() == 'u':
            print(weekday[1:2])
            break
        else:
            print(weekday[3:4])
            break
    elif s3.lower() == 's':
        s5 = input('你输入的字母有两种可能，请再输一个：')
        if s5.lower() == 'u':
            print(weekday[6:5:-1])
            break
        else:
            print(weekday[5:4:-1])
            break
    if s3.lower() == item[0:1]:
        print(item)


# 方法二
# 如果输入t或s，就在让其输入第二个字母，在通过第二个字母来判断是星期几
# 这种方法通过将，相同首字母的的星期，通过第二个字母联系在一个字典中，在将该字典当成一个
# 集合与相同的首字母联系，并将它和其他不重复的星期，放在同一个字典中,这样当代码为重复星期的
# 首字母时就在让她输入第二个字母, 在通过首字母相同星期的字典找出是星期几
weekT = {'h': 'thursday', 'u': 'tuesday'}
weekS = {'a': 'saturday', 'u': 'sunday'}
week = {'t': weekT, 's': weekS, 'm': 'monday', 'w': 'wednesday',
        'f': 'friday'}
a = week[str(input('请输入第一位字母:')).lower()]
if a == weekT or a == weekS:
    print(a[str(input('请输入第二位字母:')).lower()])
else:
    print(a)


# ----------------------------------------------------------------------


# 题目4：（反向输出II）按相反的顺序输出列表的值。

# 方法一
# reversed()方法，
# 不能像下下行代码那样直接打印，因为reversed()返回的是一个迭代器(我也不是很清楚啥是迭代器)
# 正确的做法是通过for in 来逐个获取里面的值
A4 = [1, 2, 3, 4]
# print(reversed(listA4))
a4 = reversed(A4)
b4 = []
for a in a4:
    b4.append(a)
print(b4)


# 方法二
# 通过下标来实现，这里是借助原有列表，创建一个逆序的列表
# 这种方法更简便一些
listC4 = [5, 6, 7, 8]
d4 = listC4[::-1]
print(d4)


# ---------------------------------------------------------------------


# 题目5：（列表转字符串）按逗号分隔列表。

# 方法一
# 遍历和print的end方法
a5 = [1, 2, 3, 4]
for a in a5:
    print(a, end=',')


# 方法二
# .join()方法, 分割字符串, 前面的参数是以什么分割, 后面是分割的对象
# 后面部分的格式比较特殊，意思应该是，遍历列表，将得到的参数转化成字符串，在返回给join()方法
b5 = [5, 6, 7, 8]
print(','.join(str(n) for n in b5))


# -----------------------------------------------------------------


# 题目6：（调用函数）练习函数调用。

# 创建一个屏幕
# 这里的函数用到了pygame, 如果要运行的化要先导入pygame模块，导入步骤，1点击File,
# 2点击settings, 3点击project: 项目名, 4点击python Interpreter, 5点击＋号
# 搜索并安装pygame
import pygame


class Screen:
    def __init__(self):
        """创建屏幕所需的资源"""

        # 初始化pygame
        pygame.init()

        # 设置屏幕大小(改变数字可以改变屏幕的大小)
        self.screen = pygame.display.set_mode((1000, 500))

        # 设置屏幕名称
        pygame.display.set_caption('屏幕显示')

    def run(self):
        """显示屏幕"""
        while True:
            # 检测按键按Q退出
            self.keyboard()

            # 设置屏幕颜色(改变数字可以改变屏幕的颜色)
            self.screen.fill((50, 20, 20))

            # 显示屏幕
            pygame.display.flip()

    def keyboard(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()


if __name__ == '__main__':
    A6 = Screen()
    A6.run()


# -------------------------------------------------------------------


# 题目7：（设置输出颜色）文本颜色设置

# 基本格式
# print(\033[显示方式;前景色;背景色m输出内容\033[0m)
# 其中，显示方式、前景色、背景色都是可选参数（可缺省一个或多个）。

# 显示方式	效果
# 0	默认
# 1	粗体
# 4	下划线
# 5	闪烁
# 7	反白显示

# 字体色编号	背景色编号	颜色
# 30	40	黑色
# 31	41	红色
# 32	42	绿色
# 33	43	黄色
# 34	44	蓝色
# 35	45	紫色
# 36	46	青色
# 37	47	白色

print('\033[1;44;31m 字体加粗，蓝底红字 \033[0m')
print('\033[4;45;30m 下划线，紫底黑字 \033[0m')
