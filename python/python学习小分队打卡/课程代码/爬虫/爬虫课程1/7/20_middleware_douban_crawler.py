"""
    利用scrapy爬取豆瓣top250:
        url = https://movie.douban.com/top250

        1 创建scrapy项目:
            scrapy startproject Douban

        2 在item文件中进行数据建模:
            设置要爬取的字段

        3 创建爬虫:
            cd Douban
            scrapy genspider movie douban.com

        4 在spider中编写提取数据的逻辑:
            ...
            将数据提取完毕后,通过实例化一个item类的对象,将数据根据字段填充进去,在
            yield 返回给引擎

        5 设置请求头:
            在settings文件中设置USER_AGENT
            并关闭robots.txt(注释它)

        6 运行爬虫:
            scrapy crawl movie


"""