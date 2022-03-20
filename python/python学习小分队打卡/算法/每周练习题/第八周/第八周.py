# 第八周
# 题目1：（随机数）输出一个随机数。
# 题目2：（按位与）学习使用按位与 & 。
# 题目3：（按位或）学习使用按位或 | 。
# 题目4：（按位异或）学习使用按位异或 ^ 。
# 题目5：（位取反、位移动）取一个整数a从右端开始的4〜7位。
# 题目6：（按位取反）学习使用按位取反~。
# 题目7：（画圈）画图，学用circle画圆形。

# python基础学习
# 看完第一章并完成第一章的检查点

# 爬虫学习
# 看完第一，二章


# 题目1：（随机数）输出一个随机数。

# 方法一
# random 模块中的 randint 方法
# 格式 random.randint(a, b)
import random
print(random.randint(1, 100))


# 方法二
# random.random()括号里不需要填入参数，返回一个大于等于0小于1的浮点数
print(random.random())


# 方法三
# random.uniform(a, b)返回a与b之间的一个浮点数
print(random.uniform(1, 100))


# ---------------------------------------------------------------


# 题目2：（按位与）学习使用按位与 &
# 按位与&，是针对二进制数的操作，指将两个二进制数的每一位都进行比较，如果两个相应的二进位都为 1
# 则此位为 1，否则为 0。在本例中.

# 5 的二进制表达为 101 ， 3 的二进制表达为 11 （为补全位数进行按位操作写作 011 ）
# ，则按位与操作后的结果为001 ，对应的十进制数为 1 。

# 0100 & 1010 = 0000 = 0
print(4 & 10)


# ----------------------------------------------------


# 题目3：（按位或）学习使用按位或 |
# 按位或是针对二进制数的操作，指将两个二进制数的每一位都进行比较，如果两个相应的二进位只要有一个为1
# 则此位为 1，否则为 0。在本例中， 101 与 011 进行按位或操作后的结果为 111 ，对应十进制数为 7
#
# 详细：3 | 5 —— 0000 0011 | 0000 0101 = 0000 0111 即为7
#
# 0111 | 1100 = 1111 = 15
print(7 | 12)


# -------------------------------------------------------


# 题目4：（按位异或）学习使用按位异或 ^ 。
# 按位异或是针对二进制数的操作，指将两个二进制数的每一位都进行比较，如果两个相应的二进位不同则
# 此位为1，相同为0。
#
# 详细：3 | 5 —— 0000 0011 | 0000 0101 = 0000 0110 即为6
#
#  1001 ^ 1011 = 0010 = 2
print(9 ^ 11)


# ------------------------------------------------


# 题目5：（位取反、位移动）取一个整数a从右端开始的5〜8位。

# 按位取反：
# x按位取反运算公式为： -(x+1)

# 位移动：
# 左移动公式：
# b << n == b * 2**n
# 例如：3 << 4 == 3 * 2**4 == 48

# 右移动公式：
# b >> n == b // 2**n (如果b是奇数，取商)
# 例如：4 >> 1 == 4 // 2**1 = 2

# 思路：
# bin(360) = 0b101101000
# 假如输入360，将输入的数字右移动4位(可以理解为将数字的二进制数的最后四位去掉)，得到bin(c):
# 0b10110 , 在通过c & b截取右边一到四位，(因为bin(b)为0b1111，根据 & 各数相比同一取一，
# 否则取零的规则，1111能截取到c的一到四位) 注：当位数不够时通过在数的前面补零来凑

a = int(input('输入一个数字: '))
b = 0                 # 0
b = ~b                # -1
b = b << 4              # 10000
b = ~b                # 1111
c = a >> 4
print(c)
d = c & b
print('a:', bin(a))
print('b:', bin(b))
print('c:', bin(c))
print('d:', bin(d))


# -------------------------------------------------------------------


# 题目6：（按位取反）学习使用按位取反~。
# 1变0， 0变1

# 按位取反：
# x按位取反运算公式为： -(x+1)

# -5
print(~4)

# 4，两个按位取反，值不变
print(~~4)


# -------------------------------------------------------------


# 题目7：（画圈）画图，学用circle画圆形。

# from ...import * 导入一个模块的所有函数，与import...不同的是，调用函数时不用写模块名
from tkinter import *
# 创建一个画布并设置
canvas = Canvas(width=800, height=600, bg='white')
# 布局设置
canvas.pack(expand=YES, fill=BOTH)
k = 1
j = 1
for i in range(26):
    canvas.create_oval(310-k, 250-k, 310+k, 250+k, width=1)
    k += j
    j += 0.3
# 循环显示
mainloop()


# --------------------------------------------------------------


# 1.1 什么是程序？
"""程序就是软件，它控制着计算机的一切，并且所有软件都是程序员和开发人员创建的"""
# 1.2 什么是硬件？
"""是指计算机的物理元件，是构成计算机的物理设备"""
# 1.3 列出计算机系统的五个主要部件？
"""中央处理器(cpu), 内存， 辅助存储设备(硬盘，CD等)， 输入设备， 输出设备"""
# 1.4 计算机实际运行程序的是哪个部件？
"""cpu"""
# 1.5 计算机运行时，哪个部件可用来存储程序及其数据？
"""内存"""
# 1.6 即使计算机没有电，哪个部件也能长时间的保存数据？
"""辅助存储设备"""
# 1.7 计算机的哪个部件从人和其他设备收集数据？
"""输入设备"""
# 1.8 计算机的哪个部件为人或其他设备格式化并显示数据？
"""输出设备"""
# 1.9 什么基本程序控制计算机硬件的内部运行？
"""操作系统"""
# 1.10 执行专门任务的程序(如病毒扫描程序，文件压缩程序或数据备份程序)称为什么软件？
"""系统软件"""
# 1.11 文字处理程序，电子表格程序，网页浏览器和游戏属于哪一类软件？
"""应用程序软件"""


# 1.12 多少内存足以存储ASCII字母表或小数字?
"""ASCII码一共128个，存储一个ASCII码需要一个字节(1b),所以需要128个字节"""
# 1.13 一个微小的可以设置为开或关的 “开关”，称为什么?
"""被称为位(bit)，一个字节有八位，也就是八bit"""
# 1.14 在什么编码系统中，所有的数值都写成0和1的字列?
"""二进制编码系统"""
# 1.15 ASCII 的用途是什么?
"""显示西方的英文字母，标点符号，以及数字0-9"""
# 1.16 什么编码方案足以代表世界上许多语言的特征?
"""Unicode"""
# 1.17 “数字化数据”和“数字设备”各是什么意思?
"""数字化数据是以二进制形式存储的数据，数字设备是可以与二进制数据一起工作的任何设备(例如计算机)"""


# 1.18 CPU 只能理解用什么语言编写的指令?
"""机器语言"""
# 1.19 程序在每次被 CPU执行时必须被复制到什么类型的存储器中?
"""内存"""
# 1.20 CPU 执行程序指令的过程是什么?
"""读取，解析，执行"""
# 1.21什么是汇编语言?
"""用于替代机器语言的一种低级语言(需要掌握cpu的工作原理)"""
# 1.22什么类型的编 程语言允许在不知道CPU如何工作的情况下编写功能强大且复杂的程序?
"""高级语言，例如python"""
# 1.23每种语言都有 一套在编写程序时必须严格遵守的规则，这套规则叫什么?
"""语法"""
# 1.24将高级语言 程序翻译为独立的机器语言程序的程序叫什么?
"""编译器(形成独立的机器语言程序，随时执行)"""
# 1.25翻译并执行高级语 言程序中的指令的程序叫什么?
"""解释器(翻译高级语言为机器语言，并立即执行)"""
# 1.26关键字拼写错误、 缺少标点符号或错误使用操作符造成的是什么类型的错误?
"""语法错误"""


# ------------------------------------------------------------------------


"""爬虫"""
"""第一章"""

# 1.1 查找xxx网页的全部HTML代码---------------------------------------
# from urllib.request import urlopen
#
# html = urlopen("http://baidu.com/pages/page1.html")
# print(html.read())


# 1.2 导入BeautifulSoup4库----------------------------------------------
# 我这里用pip的方法报错了，于是直接用pycharm安装了，过程：File —— Settings —— Project：
# xxx —— Python Interpreter —— +(点那个加号) —— 在搜索框里输入想导入库的名字 —— 点
# Install Package


# 1.2.2 运行BeautifulSoup-----------------------------------------------
# 运行时发现需要在BeautifulSoup里加上一个 html.parser参数，不然会报错
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html1 = urlopen('http://www.pythonscraping.com/pages/page1.html')
# bsObj = BeautifulSoup(html1.read(), "html.parser")
# print(bsObj.h1)


# 1.2.3 可靠的网络连接------------------------------------------------------
# http异常
# try:
#     html2 = urlopen("http://baidu.com/pages/page1.html")
# except HTTPError as e:
#     print(e)
# else:
#     pass


# 服务器不存在
# html = urlopen("http://baidu.com/pages/page1.html")
# if html is None:
#     print('URL is not found')
# else:
#     pass


# AttributeError错误
# html1 = urlopen('http://www.pythonscraping.com/pages/page1.html')
# bsObj = BeautifulSoup(html1.read(), "html.parser")
# # print(bsObj.nonExistenTag.somrTag)
#
# try:
#     badContent = bsObj.nonExistingTag.anotherTag
# except AttributeError as e:
#     print('Tag was not found')
# else:
#     if badContent == None:
#         print('Tag was not found1')
#     else:
#         print(badContent)


# 重构一下
# from urllib.request import urlopen
# from urllib.error import HTTPError
# from bs4 import BeautifulSoup
#
#
# def get_title(url):
#     # 如果是http异常返回none
#     try:
#         html = urlopen(url)
#     except HTTPError as e:
#         return None
#     # 如果是AttributeError错误返回none(可以理解为在一个空文件里找文件错误)
#     try:
#         bsObj = BeautifulSoup(html.read(), 'html.parser')
#         title = bsObj.body.h1
#     except AttributeError as e:
#         return None
#     # 没问题就返回title
#     return title
#
#
# title = get_title('http://www.pythonscraping.com/pages/page1.html')
# # 如果标题不存在打印不存在，否则打印标题
# if title == None:
#     print('Title could not be found')
# else:
#     print(title)


"""第二章"""


# 2.2在端一碗BeautifulSoup ----------------------------------------------
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
# bsObj = BeautifulSoup(html, 'html.parser')
#
# nameList = bsObj.findAll('span', {'class': 'green'})
# for name in nameList:
#     # .get_text()会将html文件中的标签都清楚，然后返回一个只包含文字的字符串
#     print(name.get_text())


# 2.2.1 BeautifulSoup 的 find() 和 findAll() ---------------------------------
# findAll(tag, attributes, recursive, text, limit, keywords),一般用前面两个参数，即
# 通过标签和属性查找标签
# findAll('span', {'class': "green"}) 在span标签下，获取属性为绿色的信息
# find(),和findAll()差不多，find()是寻找单个数据


# 2.2.2 其它BeautifulSoup对象 -------------------------------------------------
# BeautifulSoup 对象
# 即我们自己定义的，用来存储从网络上爬取数据的对象

# 标签tag 对象
# 数据中内容的标签

# NavigableString 对象
# 用来表示标签里的文字，而不是标签

# Comment 对象
# 用来查找html文档的注释标签。


# 2.2.3 导航树 (通过位置查找标签)-------------------------------------------------
# 子标签和后代标签(子标签是指父标签的下一代标签，后代标签是指父标签的所有后代标签)

# 寻找子标签通常在find()后加上.children，而后代标签则是.descendants
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# bsObj = BeautifulSoup(html, 'html.parser')
#
# for child in bsObj.find('table', {'id': "giftList"}).children:
#     print(child.get_text())

# 处理兄弟标签
# 通过next_siblings()函数，获取兄弟标签，首先兄弟标签不包括自身，也就是说不会返回自己。
# 在就是，这个函数只调用后面的兄弟标签，也就是所选目标后面的兄弟标签
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# bsObj = BeautifulSoup(html, 'html.parser')
#
# # 这里返回的就是tr的兄弟标签
# for sibling in bsObj.find('table', {'id': "giftList"}).tr.next_siblings:
#     print(sibling.get_text())

# 让标签的选择更加具体
# 上一个案例中我们用了兄弟标签 bsObj.find('table', {'id': "giftList"}).tr, 我们也可以
# 用其它的方法，像bsObj.table.tr或bsObj.tr，但是这样写不够稳定，在兄弟标签里我们利用了标签
# 的属性{"id": "giftList"},这样即使网页发生小的变动，我们也能通过属性查找到我们想要的标签

# 父标签处理
# # parent父标签，previous_sibling前一个兄弟标签
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# bsObj = BeautifulSoup(html, 'html.parser')
# print(bsObj.find("img", {'src': '../img/gifts/img1.jpg'}).parent.
#       previous_sibling.get_text())


# 2.3 正则表达式 -----------------------------------------------------
# aa* : a后面跟的a*表示'重复任意次a,包括零次'，这样保证字母a至少出现一次

# bbbbb : 表示b重复五次

# (cc)* : 表示有两个任意次的c,也可以是零次

# (d| ) : (|)表示这个或哪个


# 2.4 正则表达式和BeautifulSoup
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
#
# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bsObj = BeautifulSoup(html, 'html.parser')
# images = bsObj.findAll("img", {'src': re.compile('\.\.\/img\/gifts/img.*\.jpg'
#                                                  )})
# for image in images:
#     print(image['src'])


# 2.5 获取属性
# 获取一个标签(tag)的全部属性，它返回的是一个字典对象
# tag.attrs
# 可以获取和操作这些属性，比如获取图片的资源位置src，可以下面这行代码
# img_tag.attrs['src']


# 2.6 lambda表达式
# 我们可以把一些特定的函数作为findAll的参数，条件是，这些函数必须把一个标签作为参数，并且返回
# 的结果是一个布尔值。
# 例如，下面的代码可以获取用两个属性的标签
# soup.findAll(lambda tag: len(tag.attrs) == 2)


# 2.7 超越BeautifulSoup
# lxml
# 用c语言写成，处理html文档速度非常快

# HTML parser
# python自带的解析库，无需安装
