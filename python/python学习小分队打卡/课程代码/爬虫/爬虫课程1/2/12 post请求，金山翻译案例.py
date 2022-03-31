"""
    requests 模块发送post请求
    post请求，就是比get请求多了一个要发送的数据参数，data(是个字典)
"""
import requests
import json

# response = requests.post(url, data)


# 获取金山词典的翻译

class King:
    def __init__(self):
        self.url = 'https://dict.iciba.com/dictionary/word/suggestion?word=' \
                   '%25E5%25AD%2597%25E5%2585%25B8&'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
        }
        pass

    def get_data(self):
        response = requests.get(self.url, headers=self.headers)
        return response.content

    def parse_data(self, data):
        # 将获得的json字符串转化成字典
        dict_data = json.loads(data)
        print(dict_data['message'][0]['paraphrase'])

    def main(self):

        # 编写爬虫逻辑
        # url
        # headers
        # 发送get请求获取响应
        response = self.get_data().decode()
        # 数据解析(json)
        self.parse_data(response)


if __name__ == '__main__':
    a = King()
    a.main()
