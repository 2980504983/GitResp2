"""
    xpath表达式如何更加具有通用性:
        使用 | 可以让xpath两侧的表达式同时生效或者一侧生效
        将 https://www.aqistudy.cn/historydata/ 所有城市名称解析出来

        作业获取站长素材网站,指定素材

"""
import requests
from lxml import etree

url = 'https://www.aqistudy.cn/historydata/'
headers = {
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebK'
        'it/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
page_txt = requests.get(url=url, headers=headers).content.decode('utf-8')
tree = etree.HTML(page_txt)
# hot_cities = tree.xpath('//div[@class="bottom"]/ul/li/a/text()')
# all_cities = tree.xpath('//div[@class="bottom"]/ul/div[2]/li/a/text()')

# 管道符(|)的使用,更加具有通用性
print(tree.xpath('//div[@class="bottom"]/ul/li/a/text() | '
                 '//div[@class="bottom"]/ul/div[2]/li/a/text()'))


