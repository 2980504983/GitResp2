"""
	要求:抓取50页
		字段：总价，描述，评论数量，详情页链接
	用正则爬取。
"""


class Drug:
    def __init__(self):
        self.url = 'https://www.111.com.cn/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWeb'
            'Kit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
        }
    def run(self):
        # url
        pass
