"""
    输入关键词，爬取百度贴吧前十页的源码
"""

import requests
import os


class BaiDuTieBa:
    def __init__(self):
        self.tieba_url = 'https://tieba.baidu.com/f?'
        self.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537'
                  '.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
        }

    def get_response(self, page, content):

        # 创建存储路径
        dirname = f'./tieba/{content}/'

        # 如果没有该文件夹，就创建
        if not os.path.exists(dirname):
            # 创建多级目录，即如果传入路径为tieba/内容，如果贴吧或者内容不存在，就都会替你创建
            # mkdir则只能一级一级的创建目录，如果前面的tieba不存在则会直接报错
            os.makedirs(dirname)

        for i in range(page):
            # 每次构建不同的提交参数
            params = {
                'ie': 'utf-8',
                'kw': content,
                'pn': str(i * 50)
            }
            response = requests.get(self.tieba_url, headers=self.headers,
                                    params=params)
            # 存储响应源码
            with open(dirname + f"{content}第{i+1}页.html", 'w', encoding='utf-8') as file:
                file.write(response.content.decode('utf-8'))


if __name__ == "__main__":
    a = BaiDuTieBa()
    a.get_response(5, '星际争霸')
