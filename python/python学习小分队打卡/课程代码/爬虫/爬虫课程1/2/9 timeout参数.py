import requests

# 设置timeout参数
url = "http://twitter.com"
response = requests.get(url, timeout=2)
