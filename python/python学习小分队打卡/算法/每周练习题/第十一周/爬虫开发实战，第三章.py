"""第三章 基本库的使用"""

# 3.1 urllib
# 分为四个模块
# request：基本的http请求模块，可以用来模拟发送请求
# error：异常处理模块，捕获异常，保证程序不会意外终止
# parse：一个工具模块，提供了许多url的处理方法，如拆分，解析，合并等
# robotparser：用来识别网站的robots.txt

# 3.1.1 发送请求
# urlopen()
# urllib.request提供的最基本的构造http请求的方法。

# 爬取源代码
# import urllib.request
# response = urllib.request.urlopen('https://www.baidu.com')
# print(response.read().decode('utf-8'))
#
# # 查看response的类型
# print(type(response))
#
# # 调用response的一些方法和属性
# # 通过status属性得到返回结果的状态码 200表示请求成功，404表示网页未找到
# print(response.status)
# # 输出响应的头信息
# print(response.getheaders())
# # 通过传递参数获取头信息中的Server值
# print(response.getheader('Server'))

# data参数
import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())



