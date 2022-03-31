"""
    使用xpath爬取图片名称和图片数据
        https://pic.netbian.com/4kfengjing/

    什么时候用bs4:
        要求解析出携带html标签的局部数据:
            用bs4,bs4在实现标签定位的时候,返回的直接就是定位到标签对应的字符串

"""
import requests
from lxml import etree
import os


# 创建文件夹
dirName = 'img'
if not os.path.exists(dirName):
    os.mkdir(dirName)


# 爬取多页
# 定义一个通用的url模板:不可变
url_page = 'https://pic.netbian.com/4kfengjing/index_%d.html'
headers = {
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebK'
        'it/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}

for page in range(1, 6):
    if page == 1:
        url = 'https://pic.netbian.com/4kfengjing/'
    else:
        url = f'{url_page}' % page

    page_text = requests.get(url=url, headers=headers).content.decode("gbk")
    tree = etree.HTML(page_text)
    li_list = tree.xpath("//ul[@class='clearfix']/li")

    for li in li_list:
        # 局部数据解析(将页面中的标签作为带解析的数据,再次使用xpath表达式解析数据)
        title = li.xpath('./a/img/@alt')[0]+'.jpg'  # 这里不能要用//开头 要用./因为这里是对获取的局部标签进行解析
        img_src = 'https://pic.netbian.com'+li.xpath('./a/img/@src')[0]

        # 发请求获取图片数据
        img_data = requests.get(url=img_src, headers=headers).content
        imgPath = dirName + '/'+title
        with open(imgPath, 'wb') as f:
            f.write(img_data)
        print(title, '保存成功')
