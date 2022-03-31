"""
    requests_verify
    当一个网站的ca证书没有经过官网认证，那么访问时就会出现警示信息，爬虫会报错证书认证失败
    此时我们只要将verify改为false，关闭证书认证即可,会报出一个警告，但是可以无视
"""

import requests

url = "https://sam.huat.edu.cn:8433/selfserver/"

response = requests.get(url, verify=False)

print(response.content)
