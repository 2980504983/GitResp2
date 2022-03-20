"""
    scrapy管道的使用:
        1 pipeline中常用的方法:
            1 process_item(self, item, spider)
                1 管道类中必须有
                2 实现对item数据的处理
                3 必须return item
            2 open_spider(self.spider) 在爬虫开启的时候仅执行一次:
            3 close_spider(self.spider) 在爬虫关闭的时候仅执行一次
            4 一个项目中有多个爬虫:
                如果一个项目中有多个爬虫,就需要创建多个管道对应各个爬虫的存储,
                但是如果直接创建多个管道,运行一个爬虫,所有管道都会进行数据的存储,
                所以可以将__init__方法删去,重写一个open_spider(self,spider)方法
                spider就是爬虫类(我们写解析数据的哪个文件的爬虫类)的实例,可以通过 一个
                判断 if spider.name == 'xxx': 如果xxx是执行爬虫名字才执行,这样就实现
                了一个管道对应一个爬虫了
                详细见 pipeline_example.png
                      pipeline-notice.png
                注意:加了管道类还不够,还要在settings文件中添加管道信息

        2 管道文件的修改
"""