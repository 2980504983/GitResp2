"""

1 运用urllib的接口快速将爬取到的图片存储到文件中
    import urllib
    img_url = ''
    # 发起请求，并将响应保存到指定路径,但是无法进行ua伪装
    urllib.request.urlretrieve(img_url, '要保存图片的路径')

2 element中的源码数据为当前页面所有数据加载完毕后对应的完整的页面源码数据(包括动态加载的数据)
  而network中的显示的源码数据,只是单独一个请求获取的响应数据(不包括动态加载的数据)
  因此如果目标网站,有动态加载的数据，就不能直接分析element中的源码数据,而是要分析network中
  获取的响应的源码数据

3 在findall(正则,数据,re.S) 不考虑换行

    bs4:
        1 数据解析的通用原理:
            1 定位标签
            2 从标签或者标签的属性中获取数据

        2 bs4数据解析原理:
            1 实例化一个BeautifulSoup对象,且将带解析的页面源码数据加载到该对象中
            2 调用BeautifulSoup对象中相关方法,或者属性进行标签定位和文本数据的提取

        3 环境安装:
            pip install lxml 解析器
            pip install bs4

        4 BeautifulSoup对象的实例化:
            1 BeautifulSoup(fp, 'lxml') 用于将本地存储的html文档中的数据进行解析,fp=open(...)
            2 BeautifulSoup(page_text, 'lxml') 用于解析从互联网上请求到的页面源码

        5 BeautifulSoup相关方法:
            标签定位:
                soup.tagName: 只能定位第一个tagName标签

                soup.find('tagName', attrName='value') 属性定位,只返回第一个

                soup.findAll 用法更find一样,findAll返回的是一个列表

                soup.select('选择器') 根据选择器定位
                    常用选择器:
                        类选择器
                        id选择器
                        层级选择器  >:表示一个层级  空格表示多个层级

            取数据:
                .text 返回该标签中所有的文本内容,包括该标签的标签中的文本内容

                .string 返回的是该标签中的文本内容,不包括该标签的标签中的文本内容

            取属性:
                tagName['attrName']





"""

from bs4 import BeautifulSoup

fp = open("filename", 'r')
soup = BeautifulSoup(fp, 'lxml')
