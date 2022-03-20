# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class MyspiderPipeline:
    def __init__(self):
        self.file = open('itcast.json', 'w')

    def process_item(self, item, spider):
        # 将item对象强转成字典,该操作只能在scrapy中使用
        item = dict(item)
        json_data = json.dumps(item) + ',\n'

        # 将数据写入文件
        self.file.write(json_data)
        return item

    def __del__(self):
        self.file.close()
