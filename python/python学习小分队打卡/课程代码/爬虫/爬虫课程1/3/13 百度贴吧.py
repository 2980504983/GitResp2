"""
    百度贴吧爬虫
        翻页获取标题及url

    ctrl+f 响应内容中搜索
    html中绿色字体表示被注释了，xpath不会识别:
        解决方法:
           1 需要修改user-Agent换低端一些的浏览器高端浏览器有时会将html信息注释，但是他
           靠引擎仍可以玩出信息，低端浏览器不行，所以不会注释，换个低端浏览器请求头就好了

           2 将data数据的注释符号去掉data.decode().replace("<--!","").replace("-->","")

    找翻页url时尽量不要使用索引，容易变化
"""

import requests
from lxml import etree


class Tieba:
    def __init__(self, name):
        self.url = "https://tieba.baidu.com/f?ie=utf-8&kw={}".format(name)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKi'
            't/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'

            # 'User-Agent': "Mozilla/4.0 (compatible; MSIE 5.01; windows NT 5.0; DigExt)"
        }

    def get_data(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content

    def parse_data(self, data):
        # 创建elements对象
        data = data.decode().replace("<!--", "").replace("-->", "")
        html = etree.HTML(data)

        el_list = html.xpath('//li/div/div[2]/div[1]/div[1]/a')
        # print(len(el_list))

        data_list = []

        for el in el_list:
            temp = {}
            temp['title'] = el.xpath("./text()")[0]
            temp['link'] = 'http://tieba.baidu.com' + el.xpath("./@href")[0]
            data_list.append(temp)

        # 获取下一页url
        try:
            next_url = 'https:' + html.xpath('//a[contains(text(), "下一页>")]/@href')[0]
        except:
            next_url = None

        return data_list, next_url

    def save_data(self, data_list):
        # 假装保存
        for data in data_list:
            print(data)

    def run(self):
        # url
        # headers
        next_url = self.url
        while True:
            # 发送请求获取响应
            data = self.get_data(next_url)
            # 从响应中提取数据(数据和翻页用的url)
            data_list, next_url = self.parse_data(data)

            self.save_data(data_list)

            print(next_url)
            # 判断是否终结
            if next_url == None:
                break


if __name__ == '__main__':
    a = Tieba("星际争霸")
    a.run()
