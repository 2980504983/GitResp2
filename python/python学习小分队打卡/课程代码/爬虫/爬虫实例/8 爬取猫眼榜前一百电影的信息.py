"""
    爬取猫眼榜前100电影信息
    留着，破解不了它的 index 和 signKey
"""
import requests


class MaoYan:
    def __init__(self):
        self.base_url = 'https://www.maoyan.com/board/4?timeStamp=1646292475614&channelId=40011&index=7&signKey=4327339006193f923ab12738f69c23be&sVersion=1&webdriver=false&offset=90'

        self.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/53'
                '7.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
        }

    def get_response(self):
        response = requests.get(self.base_url, headers=self.headers)
        print(response.content.decode('utf-8'))

    def run(self):
        # url
        # headers
        # 发送请求获取响应
        self.get_response()
        #


if __name__ == '__main__':
    maoyan = MaoYan()
    maoyan.run()