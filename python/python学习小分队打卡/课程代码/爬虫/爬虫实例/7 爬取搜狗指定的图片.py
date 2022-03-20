"""
    爬取搜狗网指定图片

        # url
        # headers
        # 接收搜索内容，与爬取页数(每页48张)
        # 拼接url,拼接出每页url
        # 创建存储目录,如果不存在，则创建
        # 向每页url发送请求获取响应
        # 从响应中提取每页图片的url
        # 访问url获取响应
        # 从响应中获取数据
        # 将数据存入文件
"""
import requests
import threading
from queue import Queue
import json
from jsonpath import jsonpath
import os
import time


class SouGou:
    def __init__(self):
        self.url = 'https://pic.sogou.com/napi/pc/searchList?mode=1&start=%s&xml_len=48&query='
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWe'
            'bKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
        }
        # 下载图片计数变量
        self.nums = 0

    # 获取一页图片的响应
    def get_response(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content

    # 获取一页图片的url
    def get_url(self, content, page_nums):
        url_queue = Queue()
        self.url += content
        for i in range(int(page_nums)):
            url = self.url % (str(i*48))
            url_queue.put(url)
        return url_queue

    # 存储图片
    def storage(self, content):
        with open(self.dir_filename+'/%s.jpg'%(str(time.time()).replace('.', '_')), 'wb') as f:
            f.write(content)
            self.nums += 1
            print(f'已经保存{self.nums}张图片')

    # 提取一页图片中所有url，获取响应，提取数据并存储
    def parse_storage_data(self, data):
        # 将json字符串转换为json对象
        temp = json.loads(data)
        # 获取一页所有图片的url
        pic_url = jsonpath(temp, '$..items..thumbUrl')
        for item in pic_url:
            content = self.get_response(item)
            self.storage(content)

    # 创建子进程，多任务进行爬取
    def start(self, url_queue):
        while True:
            if url_queue.empty():
                break
            else:
                # 从页面url队列中获取url任务
                url = url_queue.get()

                # 获取url响应，并从中提取出图片
                data = self.get_response(url)
                self.parse_storage_data(data.decode())

    # 启动方法，负责创建文件夹，接收参数，创建子进程
    def run(self):
        # url
        # headers
        # 接收搜索内容，与爬取页数(每页48张)
        content = input('请输入搜索内容:')
        page_nums = input('请输入搜索页数(每页48张图片)')

        # 拼接url，拼接出每页url
        url_queue = self.get_url(content, page_nums)

        # 创建存储目录,如果不存在，则创建
        self.dir_filename = f'./SouGouImg/{content}'
        if not os.path.exists('./SouGouImg'):
            os.mkdir('./SouGouImg')

        if not os.path.exists(self.dir_filename):
            os.mkdir(self.dir_filename)

        # 创建多线程任务
        crawl = []
        for i in range(5):
            t = threading.Thread(target=self.start, args=(url_queue,))
            crawl.append(t)  # 存储线程对象
            t.start()



if __name__ == '__main__':
    sougou = SouGou()
    sougou.run()
