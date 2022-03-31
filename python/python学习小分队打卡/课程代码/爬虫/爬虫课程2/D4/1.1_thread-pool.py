from multiprocessing.dummy import Pool
import requests
import time


urls = ['http://127.0.0.1:5000/yang',
        'http://127.0.0.1:5000/yan',
        'http://127.0.0.1:5000/lily'
        ]


def do_request(url):
    page_text = requests.get(url=url).content.decode()
    print(len(page_text))


# ---------普通的同步代码(一般的爬虫)--------------执行6秒
start = time.time()
for url in urls:
    page_text = requests.get(url=url).content.decode()
    print(len(page_text))
print("总耗时:", time.time()-start)


# -------------异步爬虫-------------------执行2秒
start = time.time()
# 实例化一个线程对象,开启三个线程
pool = Pool(3)
# 注意urls会被自动变成一个个元素,不需要遍历
result_list = pool.map(do_request, urls)
print("总耗时:", time.time()-start)
