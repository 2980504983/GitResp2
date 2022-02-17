"""
    preserve log 保持连续抓包
    一般来说，看你是否是携带cookie登录的,就看你url中有没有.github后缀
"""

import requests
import re


def login():
    # session
    session = requests.session()
    # headers
    session.headers = {
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
        'like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    # url1 - 获取token
    url1 = 'https://github.com/login'
    # 发送请求获取响应
    res_1 = session.get(url1).content.decode()
    # 正则提取
    token = re.findall('" name="authenticity_token" value="(.*?)" />', res_1)[0]

    # url2 - 登录
    url2 = 'https://github.com/session'
    # 构建表单数据
    data = {
    'commit': 'Sign in',
    'authenticity_token': token,
    'login': '2980504983@qq.com',
    'password': '22330989650w',
    'webauthn - support': 'supported',
    }
    print(data)
    # 发送请求登录
    session.post(url2, data=data)
    # url3 = 验证
    url3 = 'https://github.com/2980504983'
    response = session.get(url3)
    with open('github.html', 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    login()
