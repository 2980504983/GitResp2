"""
{
  "code": "10001",
  "msg": "获取成功",
  "data": {
    "count": 5,
    "proxy_list": [
      {
        "ip": "113.123.116.186",
        "port": 18573
      },
      {
        "ip": "117.69.189.143",
        "port": 14282
      },
      {
        "ip": "60.166.119.234",
        "port": 45576
      },
      {
        "ip": "111.179.186.66",
        "port": 45625
      },
      {
        "ip": "180.124.156.251",
        "port": 35193
      }
    ]
  }

"""
from lxml import etree
import requests
import json
import jsonpath

# 封装代理池
url = 'http://www.zdopen.com/ShortProxy/GetIP/?api=202203122048277944&akey=a967b598bd7a7aac&count=5&timespan=4&type=3'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                  ' (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}

page_text = json.loads(requests.get(url, headers=headers).content.decode())
temp_list = jsonpath.jsonpath(page_text, '$..proxy_list')[0]  # 代理池
# print(temp_list)

# 对快代理发起一个高频的请求,让它封我的ip
# page_url = 'https://www.kuaidaili.com/free/inha/%d/'
# ips = []
# for page in range(1, 10):
#     new_url = format(page_url % page)
#     page_text = requests.get(url=new_url, headers=headers).content.decode()
#     tree = etree.HTML(page_text)
#     # 在xpath表达式中不可以出现tbody标签,会导致xpath表达式失效
#     tr_list = tree.xpath('//div[@id="list"]//tr')
#     for tr in tr_list:
#         ip = tr.xpath('./td[0]/text()')
#         ips.append(ip)
# print(len(ips))
# print(ips)


# 使用代理机制破解ip被封
for i in range(len(temp_list)):
    print(temp_list)

    ip = temp_list[i]['ip']
    port = temp_list[i]['port']
    print(ip, port)
    page_url = 'https://www.kuaidaili.com/free/inha/%d/'
    ips = []
    for page in range(1, 10):
        new_url = format(page_url % page)
        proxies = {'https': f'{ip}:{port}'}
        print(proxies)
        page_text = requests.get(url=new_url, headers=headers, proxies=proxies).content.decode()
        tree = etree.HTML(page_text)
        # 在xpath表达式中不可以出现tbody标签,会导致xpath表达式失效
        tr_list = tree.xpath('//div[@id="list"]//tr')
        for tr in tr_list:
            ip = tr.xpath('./td[0]/text()')
            ips.append(ip)
        print(len(ips))
        print(ips)
