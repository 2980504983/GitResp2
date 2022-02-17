"""
    cookiejar转换方法:
        utils
"""

import requests

url = 'http://www.baidu.com'
response = requests.get(url)

print(response.cookies)  # 这就是一个cookiejar对象

# cookiejar转字典
dict_cookies = requests.utils.dict_from_cookiejar(response.cookies)
print(dict_cookies)

# 字典转cookiejar，会丢失cookie对应的域名
jar_cookies = requests.utils.cookiejar_from_dict(dict_cookies)
print(jar_cookies)
