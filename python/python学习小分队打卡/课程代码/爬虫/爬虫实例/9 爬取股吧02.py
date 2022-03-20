"""
    爬取股吧:
        爬取目标：
            爬取前十页的阅读数,评论数,标题,作者,更新时间,详情页url

    思路:
        股吧url下一页有规律,可直接访问
        基础url
        headers
        拼接出前十页url
        for循环获取响应
        从响应中提取出阅读数,评论数,标题,作者,更新时间,详情页url,
        将数据存入文件中
"""
import requests
from lxml import etree
import os
import re


class GuBa:

    def __init__(self):
        self.base_url = 'https://guba.eastmoney.com/default,99_%s.html'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebK'
            'it/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
        }

    def save(self, data, filename, nums):
        with open(filename+f'/第{nums}页', 'w', encoding='utf-8') as f:
            for i in range(len(data['title_list'])):
                # 去除评论数，与阅读数数据中的空格
                read_nums = re.findall(r'\s*(\S*)\s*', data['read_nums'][i])
                reviews = re.findall(r'\s*(\S*)\s*', data['reviews'][i])
                # 循环写入数据
                f.write(data['title_list'][i] + '\t' +
                        data['article_url'][i] + '\t' +
                        data['name_list'][i] + '\t' +
                        read_nums[0] + '\t' +
                        reviews[0] + '\t' +
                        data['update_time'][i] + '\n')

    def parse_data(self, data):
        html = etree.HTML(data)
        title_list = html.xpath('//*[@id="main-body"]/div[4]/div[1]/div[3]/div/div[2]/div[1]/ul/li/span/a/@title')
        name_list = html.xpath('//*[@id="main-body"]/div[4]/div[1]/div[3]/div/div[2]/div[1]/ul/li/cite[3]/a/font/text()')
        update_time = html.xpath('//*[@id="main-body"]/div[4]/div[1]/div[3]/div/div[2]/div[1]/ul/li/cite[5]/text()')
        article_url = html.xpath('//*[@id="main-body"]/div[4]/div[1]/div[3]/div/div[2]/div[1]/ul/li/span/a[@title]/@href')
        read_nums = html.xpath('//*[@id="main-body"]/div[4]/div[1]/div[3]/div/div[2]/div[1]/ul/li/cite[1]/text()')
        reviews = html.xpath('//*[@id="main-body"]/div[4]/div[1]/div[3]/div/div[2]/div[1]/ul/li/cite[2]/text()')
        res = {'title_list': title_list,
               'name_list': name_list,
               'update_time': update_time,
               'article_url': article_url,
               'read_nums': read_nums,
               'reviews': reviews
               }
        return res

    def get_response(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content

    def run(self):
        filename = './guba_info'
        # 创建股吧信息存储目录
        if not os.path.exists(filename):
            os.mkdir(filename)
        # 将每页url拼接好，传给get_response获取响应看，再把数据传给parse_data进行数据解析，
        # 解析完毕后，给save通过文件存储
        for i in range(1, 11):
            response = self.get_response(self.base_url % str(i))
            data = self.parse_data(response.decode('utf-8'))
            self.save(data, filename, i)
            print(f"第{i}页爬取完成")


if __name__ == '__main__':
    guba = GuBa()
    guba.run()
