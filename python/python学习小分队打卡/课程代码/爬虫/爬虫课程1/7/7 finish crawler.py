"""
    完成爬虫:
        1 修改起始url
        2 检查修改允许的域名
        3 在parse方法中实现爬取逻辑


        # xpath方法返回的是选择器对象列表(scrapy的一个对象)
        # 用先查看数据在列表的哪一位,在用extract()方法提取数据
        # 你也可以直接使用extract_first()获取索引零上的数据,使用它还有一个优点
        # 如果没有找到数据,使用索引会报错,而使用extract_first不会报错会返回None
        # xpath结果为只含有一个值得列表,可以使用extract_first(),如果为多个值
        # 则使用索引配合extract()

        解析完数据后,直接return就好了,但是注意,直接return的话函数就结束了,此时如果有翻页需求
        就会有些麻烦,所以爬虫中通常使用yield来返回数据,这样函数就不会直接结束

    注意:
        1 爬虫类中必须有parse方法
        2 如果网站比较复杂,也可以定义其它方法
        3 从数据中提取的url,必须属于allowed_domains范围内,但是start_urls中的url地址不受这个限制
        4 parse()函数中使用yield返回数据
        5 yield能传递的对象只能是: BaseItem, Request, dict, None

    定位元素以及提取数据:
        1 response.xpath():
            返回一个类似list的类型,里面包含的是selector对象,有一些额外的方法

        2 额外的方法:
            extract() 返回一个包含有字符串的列表

        3 extract_first() 返回列表中的第一个字符串,列表为空返回None


    response响应对象的常用属性:
        1 response.url 当前响应的url
        2 response.request.url 当前响应对应的请求的url地址
        3 response.headers 响应头
        4 response.requests.headers 当前响应的请求头
        5 response.body 响应体,也就是html代码,bytes类型
        6 response.status 响应状态码
"""