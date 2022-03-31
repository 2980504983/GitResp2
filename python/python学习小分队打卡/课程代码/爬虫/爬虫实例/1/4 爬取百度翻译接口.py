"""
    爬取百度翻译接口,输入英文返回中文翻译
"""
import requests


class BaiDuFanYi:
    def __init__(self, kw):
        self.kw = kw
        self.bash_url = 'https://fanyi.baidu.com/sug'
        self.headers = {

        }
        self.data = {
            'kw': self.kw
        }

    def run(self):
        # 创建基本url
        # 创建响应头
        # 创建参数表单
        # 根据url发送post请求获取响应
        response = requests.post(self.bash_url, headers=self.headers,
                                data=self.data)
        # 整理数据
        result = ''
        for i in response.json()['data']:
            result += i['v'] + '\n'
        print(self.kw + "的翻译结果为:")
        print(result)


if __name__ == '__main__':
    a = BaiDuFanYi('dog')
    a.run()
