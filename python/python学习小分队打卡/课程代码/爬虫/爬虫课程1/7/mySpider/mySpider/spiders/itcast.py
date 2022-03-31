import scrapy
from mySpider.items import MyspiderItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    # 2 检查域名
    allowed_domains = ['itcast.cn']
    # scrapy中有一个方法会自动向start_urls发起响应,只要你不重写,scrapy会将响应内容
    # 发送到下面parse作为response
    # 1 修改起始url
    start_urls = ['https://www.itcast.cn/channel/teacher.shtml#ajavaee']

    # 3 在parse中是实现爬取逻辑
    def parse(self, response, *args, **kwargs):
        # 定义对于网站的相关操作
        # with open('itcast.html', 'wb') as f:
        #     f.write(response.body)
        # 获取所有教师节点,scrapy提供了xpath方法,不用在导入
        node_list = response.xpath('//div[@class="li_txt"]')
        for node in node_list:
            # temp = {}
            item = MyspiderItem()

            # xpath方法返回的是选择器对象列表(scrapy的一个对象)
            # 用先查看数据在列表的哪一位,在用extract()方法提取数据
            # 你也可以直接使用extract_first()获取索引零上的数据,使用它还有一个优点
            # 如果没有找到数据,使用索引会报错,而使用extract_first不会报错会返回None
            # xpath结果为只含有一个值得列表,可以使用extract_first(),如果为多个值
            # 则使用索引配合extract()
            item['name'] = node.xpath('./h3/text()')[0].extract()
            item['title'] = node.xpath('./h4/text()')[0].extract()
            item['desc'] = node.xpath('./p/text()')[0].extract()

            yield item

