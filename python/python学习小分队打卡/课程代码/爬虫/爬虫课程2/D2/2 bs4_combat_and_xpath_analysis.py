"""
    1 bs4实战
        爬取三国演义全篇内容
        url=http://www.shicimingju.com/book/sanguoyanyi.html

    2 xpath解析:
        解析原理:
            1 实例化一个etree对象
            2 调用etree对象的xpath方法结合着不同的xpath表达式实现标签的定位和数据解析

        实例化etree对象的方式:
            etree.parse(filename) 将本地html文档加载到该对象中
            etree.HTML(page_test) 将网站获取的页面数据加载到对象中

        标签定位:
            1 标签定位:
                非最左侧的/: 表示一个层级
                最左侧的/: 表示该xpath表达式一定要从跟标签进行定位也就是/html
                非最左侧的//: 表示多个层级
                最左侧的//: 表示xpath可以从任意位置进行标签定位
                属性定位: tagName[@attrName='value']
                索引定位: tagName[index] index从1开始
                模糊匹配: tagName[contains(@class, 'ng')] 如果一个标签class属性中有ng
                        tagName[starts-with(@class, 'ta')] class属性以ta开头
            2  取文本
                /text():直系文本内容(类似bs4的.string)
                //text():所有文本内容(类似bs4的.text)
            3  取属性
                /@attrName


"""


# 1-----------------------------------------------------
import requests
from bs4 import BeautifulSoup

# 发起请求,获取响应内容
url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
headers = {
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
page_txt = requests.get(url=url, headers=headers).content.decode()

# 打开文件:
fp = open('./sanguo.txt', 'w', encoding='utf-8')

# 数据解析(提取详情页url,章节标题,章节内容),使用bs4
# 创建bs4对象
soup = BeautifulSoup(page_txt, 'lxml')
a_list = soup.select('.book-mulu > ul > li > a')

for a in a_list:
    title = a.string
    detail_url = 'https://www.shicimingju.com' + a['href']

    # 对详情页发请求,并从中解析出章节内容
    page_text_detail = requests.get(url=detail_url, headers=headers).content.decode('utf-8')
    soup1 = BeautifulSoup(page_text_detail, 'lxml')
    # 定位内容所在的标签
    div_tag = soup1.find('div', class_='chapter_content')
    # 获取该标签下的所有文本
    content = div_tag.text
    fp.write(title+':\n'+content+'\n')
    print(title, '保存成功')
fp.close()
