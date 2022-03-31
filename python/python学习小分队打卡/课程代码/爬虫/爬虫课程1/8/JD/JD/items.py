# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    # define the fields for your item here like:
    # 大分类名称和url
    big_category = scrapy.Field()
    big_category_link = scrapy.Field()
    
    # 小分类名称和url
    small_category = scrapy.Field()
    small_category_link = scrapy.Field()
    
    # 数据
    book_name = scrapy.Field()
    author = scrapy.Field()
    book_link = scrapy.Field()
    price = scrapy.Field()
    pass
