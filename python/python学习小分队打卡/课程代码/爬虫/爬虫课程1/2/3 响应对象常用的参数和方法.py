"""
    常见的响应对象参数和方法:
        response.url 响应url
        response.status_code 状态码(不一定可信)
        response.request.headers 响应对应的请求头
        response.headers 响应头
        response.cookies 响应的cookie(经过了set-cookie动作，返回cookieJar类型)
        response。json() 自动将json字符串响应内容转化为python对象(dict or list)

"""
import requests

url = "http://www.baidu.com"

response = requests.get(url)

print(response.url)
print(response.status_code)
print(response.request.headers)
print(response.headers)
