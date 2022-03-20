import asyncio
import time
import requests


async def get_request(url):
    print("正在请求的url", url)
    time.sleep(2)
    print("请求结束", url)
    return "bobo"


urls = [
    'www.1',
    'w2',
    '3'
]


if __name__ == "__main__":
    start = time.time()
    # 多任务列表
    tasks = []
    # 1 创建协程对象
    for url in urls:
        c = get_request(url)
        # 2 创建任务对象
        task = asyncio.ensure_future(c)
        tasks.append(task)

    # 3 创建事件循环对象
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(tasks) 不能直接这样写

    # 必须使用wait方法对tasks进行封装才可
    loop.run_until_complete(asyncio.wait(tasks))
    print('总耗时:', time.time()-start)



