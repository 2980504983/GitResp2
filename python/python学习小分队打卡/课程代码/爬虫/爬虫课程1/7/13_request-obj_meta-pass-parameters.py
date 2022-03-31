"""
    meta参数的使用:
        meta可以实现数据在不同解析函数中的传递
        当要爬取的数据不在同一页中,也就是要再次发起请求获取一次数据时,就要用meta
        注:
            meta参数是一个字典
            meta字典中有一个固定的键proxy,表示代理ip
            
    scrapy中Request方法中meta参数的用法
        首先我们要知道meta是一个字典,它的主要作用是用来传递数据的
        meta = {'key1':value1},如果想在下一个函数中取出value1, 只需得到上一个函数的meta['key1']即可, 
        因为meta是随着Request产生时传递的,下一个函数得到的Response对象中就会有meta,即response.meta.

"""