"""
    创建爬虫
        命令:
            进入项目目录执行
            scrapy genspider 爬虫名称 允许爬取的域名
            爬虫名称:
                作为爬虫运行时的参数
            允许爬取的域名:
                为对于爬虫设置爬取范围,设置之后用于过滤要爬取url,如果爬取的url与允许的域不同
                则被过滤掉
            实例:
                cd mySpider
                scrapy genspider itcast itcast.cn

            爬虫文件的介绍:
                三个参数:
                    name
                    allowed_domains
                    start_urls 设置起始的url,我们只需设置就好,scrapy会自动的向该url发起请求
                               获取响应
                一个方法:
                    parse 解析方法,通常用于解析起始url响应,response就是起始url获取的响应,
                    注: response貌似要加上body才是网页的源码

    运行爬虫:
        在项目目录下执行 scrapy crawl 爬虫名称
        scrapy crawl 爬虫名称 --nolog 不显示日志

"""