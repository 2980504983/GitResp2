"""
    爬取百度产品，并将url与产品用字典连接，并将各种产品分类
"""
import requests
import re


class BaiDu:
    def __init__(self):
        # 设置url
        self.url = 'http://www.baidu.com/more'

    def get_data(self):
        # 设置请求头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
        }
        # 发送请求并获取响应
        response = requests.get(self.url, headers=headers)
        return response.content

    def parse_data(self, response):
        # 从html中提取各项功能分类并存入字典中,get_text()获取文本信息
        features_dict = {}
        response1 = response.decode()
        a = 0
        pattern = r'<!--.+-->\s*[\S|\s]*?<div class="cl"></div>'
        temp = re.findall(pattern, response1)
        list2 = {}
        for item in temp:
            key = re.findall(r'<!--(.+)-->', item)[0]
            values = re.findall(r'<a (.+)</a>', item)
            list1 = []
            if a == 0:
                del values[4]
                del values[2]
                del values[0]
            list2[key] = list1
            a += 1
            for item1 in values:
                url = re.findall(r'"(http://.*?|https://.*?)"', item1)
                name = re.findall(r'>(.+?)\b', item1)
                list1.append((url[0], name[-1]))
        print(list2)
        # 返回信息字典
        return features_dict

    def run(self):
        # url
        # headers
        # 发送get请求获取响应
        response = self.get_data()
        # 从响应结果提取信息
        res = self.parse_data(response)


if __name__ == '__main__':
    a = BaiDu()
    a.run()
