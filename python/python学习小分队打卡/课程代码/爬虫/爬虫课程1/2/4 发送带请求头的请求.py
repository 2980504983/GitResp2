import requests

url = 'http://www.baidu.com'

# 不带请求头时打印的内容,只有2287字节
# response = requests.get(url)
# print(len(response.content.decode()))
# print(response.content.decode())

# 构建请求头
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
    (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
}


# 带了请求头后打印的内容，345024字节，第一层最基本的伪装
# response1 = requests.get(url, headers=headers)
# print(len(response1.content.decode()))
# print(response1.content.decode())


# 找到url中关键参数的方法:
# 通过不断的将参数删去，看响应内容是否改变

# 发送带参数的请求:
# 1 url中直接带参数

# url3 = 'https://www.baidu.com/s?wd=python&rsv_spt=1&rsv_iqid=0xc634dc03000
#         fa72''8&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=&tn=baiduhome
#         _pg&ch=&r' \'sv_enter=1&rsv_dl=ib&rsv_btype=i&inputT=1408'
#
# response = requests.get(url, headers=headers)
#
# with open('baidu.html', 'wb') as f:
#     f.write(response.content)


# 2 构建参数字典
# ?后面是参数
url3 = 'https://www.baidu.com/s?'

# 构建参数字典
data = {'wd': 'python'
    }

response = requests.get(url, headers=headers, params=data)
print(response.url)
with open('baidu1.html', 'wb') as f:
    f.write(response.content)
