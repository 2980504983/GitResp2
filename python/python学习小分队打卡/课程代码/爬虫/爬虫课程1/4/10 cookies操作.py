"""
    selenium对cookie的处理,
    当遇到一个网站非常复杂，解不过去了，需要cookie，就可先用selenium获取所有的
    cookies，然后将cookies转化为字典，再用requests模块进行爬取
"""
from selenium import webdriver

url = 'https://www.baidu.com'

driver = webdriver.Chrome()

driver.get(url)

# 获取在百度上的所有cookies
# cookies = driver.get_cookies()
# print(cookies)

# 将cookies转化成字典
cookies = {}
for data in driver.get_cookies():
    cookies[data['name']] = data['value']

print(cookies)
