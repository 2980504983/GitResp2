import scrapy
from Douban.items import DoubanItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['douban.com']
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response, *args, **kwargs):
        el_list = response.xpath('//*[@class="info"]')
        # print(response.body.decode())
        # print(len(el_list))

        # 将数据提取,将其给到item类的实例,在返回给引擎
        for el in el_list:
            item = DoubanItem()
            item['name'] = el.xpath('./div[1]/a/span[1]/text()').extract_first()
            yield item

        url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        if url is not None:
            # 拼接url,让该url与start_urls进行拼接
            url = response.urljoin(url)

            # 再次对解析出来的url发起请求,因为默认的解析方法时parse,所以不需要指定callback
            yield scrapy.Request(
                url=url,
            )
        pass
