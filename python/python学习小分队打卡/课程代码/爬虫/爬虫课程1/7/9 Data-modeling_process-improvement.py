"""
    scrapy数据建模与请求:
        通常在做项目的过程中,在item.py中进行数据建模

        1 为什么建模:
            1 定义item即提前规划好那些字段需要抓,防止手误,因为定义好之后,在运行过程中,系统会
              自动检查
            2 配合注释,看起来更清晰
            3 scrapy的一些组件需要item建模做支持

        2 如何建模:
            在item.py中定义要提取的字段:
                name = scrapy.Field() 讲师名字

        3 如何使用模板类:
            模板类定义以后需要在爬虫中导入并且实例化,之后的使用方法和使用字典相同

        注:
            1 python中导入路径的要诀,从哪里开始运行,就要从哪里开始导入

    开发流程总结:
        1 创建项目
            scrapy startproject 项目名
        2 明确目标
            在items.py文件中进行建模
        3 创建爬虫
            scrapy genspider 爬虫名 允许的域
        4 完成爬虫:
            修改start_urls
            检查修改allowed_domains
            编写解析方法
        5 保存数据:
            在pipelines.py文件中定义对数据处理的管道
            在settings.py文件中注册启用管道



"""