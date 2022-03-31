"""
    requests模块:
        requests库官方文档是中文的，是python的第三方模块

        requests模块的作用:
            发送http请求，获取响应数据

        requests模块发送get请求:

        1 response.text是requests模块按照chardet模块推测出的编码字符集进行解码的结果
        2 网络传输的字符串都是bytes类型。所以response.text = response.content.decode('
          推测出的编码字符集')
        3 我们可以在网页源码中搜索charset， 尝试参考该编码字符集，注意存在不准确的情况

        response.text：
            str
            requests自动推测文本编码

        response.content
            bytes
            没有指定，自己指定

        常见的编码字符集:
            utf-8
            gbk
            gb2312
            ascii
            iso-8859-1



"""

import requests

# 目标url
url = "https://www.baidu.com"

# 向目标url发送get请求
response = requests.get(url)


# 打印编码格式
print(response.encoding)

# 指定编码格式
response.encoding = 'utf8'

# 表示打印源码str类型数据
print(response.text)

# .content是二进制格式，加个decode()就好了,decode()按照指定格式解码，默认utf-8
print(response.content.decode())

