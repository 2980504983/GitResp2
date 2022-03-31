"""
    实例:
        爬取雪球网中的咨询信息:
            https://xueqiu.com/
        分析:
            1 判定爬取的咨询数据是否为动态加载的数据?
                相关的更多的咨询数据是动态加载的,向下滑时,动态加载数据

            2 定位到ajax请求的数据包,提取出请求的url,响应数据为json形式的咨询数据:
"""

import requests

session = requests.Session()  # 创建session对象


main_url = 'https://xueqiu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                  '(KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'

}
# 第一次使用session捕获且存储cookie,猜测对雪球网的首页发起请求会产生cookie
session.get(main_url, headers=headers)


url = 'https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=322813&size=15'
response = session.get(url=url, headers=headers).json()
# 有了捕获cookie的操作,就可以正确爬取到数据了
print(response)







