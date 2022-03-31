"""
    下载菜鸟教程100例
"""
import requests
from lxml import etree
import os


class CaiNiao:
    def __init__(self):
        self.rookie100_url = "https://www.runoob.com/python/python-100-examples.html"
        self.headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
        }
        self.url_100 = []

    def get_response(self):
        response = requests.get(self.rookie100_url, headers=self.headers)
        return response.content

    def parse_url(self, response):
        # 创建elements对象
        html = etree.HTML(response)
        # 用正则匹配url
        self.url_100 = html.xpath(r"//div[@id='content']/ul/li/a/@href")

    def get_exercise(self, dirname):
        # for url in self.url_100:
        #     response = requests.get(url, headers=self.headers)
        for i in range(len(self.url_100)-90):
            response = requests.get('https://www.runoob.com' + self.url_100[i], headers=self.headers)
            html = etree.HTML(response.content)
            title = '题目:\n'+html.xpath(r'//div[@id="content"]/p[2]/text()')[0]

            analysis = '\n程序分析:\n'+html.xpath('//*[@id="content"]/p[3]/text()')[0]

            code = '\n# 答案代码:\n'+''.join(html.xpath(r"//div[@class='hl-main']/span/text()"))
            filename = f'第{i+1}例.py'
            with open(dirname+filename, 'w', encoding='utf8') as f:
                f.write(f'"""{title}\n{analysis}\n{code}\n"""')
            print(f'第{i+1}例爬取完成')


    def run(self):
        # 菜鸟100例主页面url
        # 创建请求头
        # 获取响应
        response = self.get_response()

        # 从响应中提取出100例的url存储在列表中
        self.parse_url(response)

        # 创建文件夹
        dirname = './cainiao_exercise/'
        if not os.path.exists(dirname):
            os.mkdir(dirname)

        # 遍历100例url列表
        # 进入url，获取响应
        # 从中提取100例每例的信息
        # 将信息存入文件夹的文件中
        self.get_exercise(dirname)


if __name__ == '__main__':
    a = CaiNiao()
    a.run()
