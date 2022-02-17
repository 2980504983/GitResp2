from urllib.request import urlopen
from bs4 import BeautifulSoup

# 基本使用
# html = urlopen("http://www.baidu.com")
# bsobj = BeautifulSoup(html.read(), 'lxml')
# print(bsobj)


# 爬取http://www.pythonscraping.com/pages/warandpeace.html网站
url = 'http://www.pythonscraping.com/pages/warandpeace.html'
# 访问网页并获取响应内容
html1 = urlopen(url)
bsobj1 = BeautifulSoup(html1, 'lxml')

namelist = bsobj1.findAll("span", {"class": "green"})
for name in namelist:
    print(name.get_text)


