"""
    crawlspider(一个爬虫模板):
        继承于Spider爬虫类,功能更强,但是理解起来更为复杂

        1 可以自动根据规则提取链接并发送给引擎
        2 性能更高

        使用:
            1 创建crawlspider爬虫:
                -t表示选择模板
                scrapy genspider -t crawl name domains

    scrapy shell的使用:
        在终端输入 scrapy shell即可进入
        挺好用的, scrapy shell url 会直接对该url发起请求
        你可以在里面直接操作获取到的数据,response.status 获取状态码
"""