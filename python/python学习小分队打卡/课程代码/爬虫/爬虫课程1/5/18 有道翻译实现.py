import requests
import hashlib
import time
import random


class YouDao:
    def __init__(self, word):
        self.url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Apple"
                          "WebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
            "Cookie": "OUTFOX_SEARCH_USER_ID=-2146489312@10.169.0.84; OUTFOX_SEAR"
                          "CH_USER_ID_NCOO=874039880.084492; JSESSIONID=aaaPfxeOjj_vW95vdby9x; ___rl__test__cookies=1646449233007",
            "Referer": "https://fanyi.youdao.com/"
        }
        self.formdata = None
        self.word = word

    def generate_formdata(self):
        """
            生成formdata,用python模拟实现
            ts: r = "" + (new Date).getTime(),
            salt: ts + parseInt(10 * Math.random(), 10),
            sign: n.md5("fanyideskweb" + e + i + "Ygy_4c=r#e#4EX^NUGUc5")
        """
        ts = str(int(time.time()*1000))
        salt = ts + str(random.randint(0, 9))
        tempstr = "fanyideskweb" + self.word + salt + "Ygy_4c=r#e#4EX^NUGUc5"
        md5 = hashlib.md5()
        md5.update(tempstr.encode())
        sign = md5.hexdigest()
        self.formdata = {
            'i': self.word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'lts': ts,
            'bv': '56d33e2aec4ec073ebedbf996d0cba4f',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }

    def get_data(self):
        response = requests.post(self.url, data=self.formdata, headers=self.headers)
        return response.content

    def run(self):
        # url
        # headers
        # formdata
        self.generate_formdata()
        print(self.formdata)
        # 发送请求
        data = self.get_data()
        print(data)
        #
        pass


if __name__ == "__main__":
    youdao = YouDao('人生苦短我用python')
    youdao.run()
