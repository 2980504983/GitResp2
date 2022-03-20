import scrapy
import json
from jsonpath import jsonpath

class JobSpider(scrapy.Spider):
    name = 'job'
    # 2 检查修改allowed_domains
    allowed_domains = ['163.com']
    # 1 修改start_url
    start_urls = ['https://hr.163.com/api/hr163/position/queryPage']

    # scrapy中默认请求时get,这里重写发送请求的方法,将其改成post,并设置参数
    def start_requests(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
        }
        url = "https://hr.163.com/api/hr163/position/queryPage"
        yield scrapy.FormRequest(url, formdata={'currentPage': '1', 'pageSize': '10'}, headers=headers, )

    def parse(self, response, *args, **kwargs):
        # 1 提取数据
        # 获取所有职位节点列表
        print(response.body.decode())
        temp = json.loads(response.body.decode())
        print(temp)
        node_list = temp.jsonpath('$..list')
        print(node_list)

        # 2 模拟翻页(改变post表单中提交的参数)
        pass
