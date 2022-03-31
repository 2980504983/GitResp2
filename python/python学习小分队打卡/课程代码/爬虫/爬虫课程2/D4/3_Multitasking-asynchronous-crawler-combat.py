import requests
import asyncio
import time
import aiohttp
from lxml import etree


urls = [
    'https://www.baidu.com',
    'https://www.baidu.com',
    'https://www.baidu.com'
    
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebK'
                  'it/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
                  
}

# 异步持久化存储数据,异步爬虫将数据异步的装进列表,
# 在模仿异步爬虫的原理将这个列表里的数据进行异步存储
data_list = []

# async def get_request(url):
#     # requests是一个不支持异步的模块
#     page_text = requests.get(url).text
#     return page_text

async def get_request(url):
    
    # 实例化一个请求对象
    async with aiohttp.ClientSession() as sess:
        # 用asyncio内置的sleep暂停两秒查看异步效果
        await asyncio.sleep(2)
        # 调用get发起请求,返回一个响应对象
        # get/post(url, headers, params/data, proxy)
        async with await sess.get(url=url, headers=headers) as response:
            # text()获取了字符串形式的响应数据
            # read()获取byte类型的响应数据
            page_text = await response.text()
            return page_text

# 解析函数的封装
def parse(t):
    # 获取请求到页面源码数据
    page_text = t.result()
    # print(page_text)
    tree = etree.HTML(page_text)
    parse_text = tree.xpath('//*[@id="su"]/@value')[0]
    print(parse_text)

if __name__ == '__main__':
    start = time.time()
    tasks = []
    for url in urls:
        c = get_request(url)
        task = asyncio.ensure_future(c)
        task.add_done_callback(parse)
        tasks.append(task)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print("总耗时:",time.time()-start)
