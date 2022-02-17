"""
    理解使用代理的过程:
        什么是代理:
            1 代理ip是一个ip，指向的是一个代理服务器
            2 代理服务器能够帮我们向目标服务器转发请求

        正向代理和反向代理:
            1 从发送请求的一方角度上，来区分正反向代理
            2 为浏览器和客户端转发请求的，叫做正向代理， (浏览器知道请求给谁了例如vpn)
            3 不为浏览器或客户端转发请求，而是为最终处理请求的服务器，转发请求的，叫做反向代理，
              浏览器不知道请求给谁了(例如nginx)
            注: 知不知道最终服务器的地址作为判断标准

        代理ip(代理服务器)的分类:
            1 根据代理ip的匿名程度分:
                1 透明代理 (服务器知道是代理，还知道你的ip)
                2 匿名代理 (服务器知道是代理，但不知道你的ip)
                3 高匿代理 (服务器判断不出是代理) (写爬虫高匿最好)
            2 根据协议分类:
                http代理
                https代理
                socks隧道代理

    requests中代理的使用:
        proxies代理参数的使用:
            requests.get(url, proxies=proxies)
        proxies的形式是字典:
            proxies = {'http': url, 'https': url}

        代理使用失败，要么卡滞，要么报错

"""
import requests

# proxies代理的使用

url = 'http://www.baidu.com'
proxies = {
    'http': 'http://152.136.62.181:9999'
}
response = requests.get(url, proxies=proxies)
response.encoding = 'utf8'
print(response.text)
