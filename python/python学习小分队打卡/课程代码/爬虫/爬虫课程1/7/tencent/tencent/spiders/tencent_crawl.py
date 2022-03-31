import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# crawlspider经常应用于数据在一个页面上进行采集的情况,如果数据在多个页面上采集,
# 也就是要将数据拼全了再返回给引擎,通常使用spider类,用meta参数来实现(crawlspider虽然也有meta
# 但是用起来比较繁琐)
class TencentCrawlSpider(CrawlSpider):
    name = 'tencent_crawl'
    allowed_domains = ['careers.tencent.com']
    start_urls = ['https://careers.tencent.com/search.html?pcid=40001']

    # 链接提取规则
    rules = (
        # LinkExtractor用于设置链接提取规则,一般使用allow参数,接收正则表达式
        # follow参数决定是否在链接提取器,提取的链接的对应的响应中,继续用链接提取器提取链接
        # 使用Rule类生成链接提取规则对象
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item'),
    )

    # 在crawlspider中不能重写sparse方法,因为它已经帮我们重写了,如果你重写了,就会报错
    def parse_item(self, response):
        print(response.url)
