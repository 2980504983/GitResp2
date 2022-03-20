"""
    在scrapy中处理翻页请求:
        构造请求对象,并发送请求:
            实现方法:
                1 确定url地址
                2 构造请求,scrapy.Request(url, callback)
                    callback: 回掉,指定解析函数名称,表示请求返回的响应使用哪一个函数进行解析
                3 把请求交给引擎,yield scrapy.Requests(url,callback)

    网易招聘爬虫案例:
        

"""