"""
    1 安装 scrapy:
        sudo apt-get install scrapy
        pip3 install scrapy

    2 scrapy 项目开发流程:
        1 创建项目:
            scrapy startproject mySpider

        2 生成一个爬虫:
            scrapy genspider itcast.cn

        3 提取数据:
            根据网站结构在spider中实现数据采集相关内容

        4 保存数据:
            使用pipeline进行数据后续处理和保存
"""