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
