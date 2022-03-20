"""
    爬取新浪网指定内容，并将相应内容的第一页文章返回
"""
import requests
from bs4 import BeautifulSoup
import re


class News:
    def __init__(self):
        self.url1 = 'https://search.sina.com.cn/?'
        self.url_title_list = []
        pass

    def get_response(self, params):
        headers = {
 'user-agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / '
              '537.36(KHTML, likeGecko) Chrome / 98.0.4758.102Safari / 537.36'
        }
        response = requests.get(self.url1, headers=headers, params=params)

        return response.content

    def get_url_title(self, response):
        soup = BeautifulSoup(response, 'lxml')
        temp = soup.findAll('h2')
        for item in temp:
            url = re.findall(r'"(.+?)"', item.decode())
            temp1 = re.findall(r'_blank">(.*?)<', item.decode())
            temp2 = re.findall(r'"red">(.*)</font>', item.decode())
            temp3 = re.findall(r'</font>(.*)</a>', item.decode())
            if len(temp1) == 0:
                temp1.append('')
            text = temp1[0] + temp2[0] + temp3[0]
            self.url_title_list.append((text, url[0]))

    def main(self):
        # 指定搜索内容
        msg = input("请输入要搜索的内容:")
        # 通过搜索内容构建url1
        # 构建参数字典
        params = {
            'q': msg,
            'c': 'news',
            'from': 'channel',
             'ie': 'utf-8'
        }
        # 发送get请求，获取响应
        response = self.get_response(params)
        # 从响应内容中提取出各种文章标题，以及各种url(只爬取第一页)
        # 创建url列表
        self.get_url_title(response)
        # for访问url列表，根据url访问文章，获取响应
        # 从响应中提取文字，并与文章标题结合
        print(self.url_title_list)


if __name__ == '__main__':
    news = News()
    news.main()
