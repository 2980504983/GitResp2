# -*- coding: utf-8 -*-

from JD.items import JdItem

import scrapy
import jsonpath,json
from lxml import etree

# ---------1 导入分布式爬虫类
# from scrapy_redis.spiders import RedisSpider


# ----------2 继承分布式爬虫
class BookSpider(scrapy.Spider):
    name = 'book'
# ------------3 注释start_url和allowed_aomains
    # # 修改允许的域
    # allowed_domains = ['jd.com']
    # # 修改起始的url
    # start_urls = ['https://pjapi.jd.com/book/sort?source=bookSort']
# ------------4 设置redis_key
    reids_key = 'py21'
    
# -----------5 设置__init__
    def __init__(self, name=None, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = list(filter(None, domain.split(',')))
        super(BookSpider, self).__init__(**kwargs)
        
# -------------6 设置settings文件

    # 重写请求方法
    def start_requests(self):
        url = self.start_urls[0]
        temp = 'shshshfpa=b7071086-4a7e-60d2-8ac2-868abd9b10c7-1642297986; shshshfpb=p6A4NAK8yKsDeEmywpc5LsA; __jdu=16422979858191314349208; unpl=JF8EAMlnNSttUU1QAUsGHBpATg5WW1oPSR4HP2MFVw0LHgMMH1EbEBF7XlVdXhRKFR9sZBRUWFNKUQ4YBisSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAhwXE0hVUlZUDEIXC29lBVFfXUNXBBIyKxUge21cXV8ITB8zblcEZB8MF1QNEgoYE11LWlFdXgBNHwprbgVcXVpLUQceChgTGXtcZF0; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_8755a569a4b3466385a512abdf85b130|1647929066552; areaId=21; ipLoc-djd=21-1861-0-0; PCSYCityID=CN_360000_361100_0; shshshfp=1d19db7ff430ff2f8d258c8973921c30; shshshsID=c1344c4ed7311a46cd28b62f6284fe32_1_1647929069019; __jda=122270672.16422979858191314349208.1642297985.1642467270.1647929067.4; __jdc=122270672; o2-webp=true; __jdb=122270672.5.16422979858191314349208|4.1647929067; 3AB9D23F7A4B3C9B=TLXV4U55UF5BTJP72QO22OELQIG7BITBKGL7HRIXEKGLYKE3T44LSZELCMAU2FC7BH2HBLGWBRTCHCLXQITQVWDA44'
        cookies =  {data.split('=')[0]:data.split('=')[-1] for data in temp.split(';')}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                           '(KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
            'Referer': 'https://book.jd.com/'
                           
        }
        
        yield scrapy.Request(
            url=url,
            callback=self.parse,
            cookies=cookies,
            headers=headers
        )
        
    

    def parse(self, response):
        temp = json.loads(response.body.decode())
        # 提取大分类节点
        node_list = jsonpath.jsonpath(temp, '$..data[*]')
        
        # 遍历大分类节点,提取数据
        for node in node_list[:1]:
            big_category = jsonpath.jsonpath(node, '$.categoryName')

            big_category_f_id = int(jsonpath.jsonpath(node, '$.fatherCategoryId')[0])
            big_category_id = int(jsonpath.jsonpath(node, '$.categoryId')[0])
            big_category_link = 'https://channel.jd.com/%d-%d.html'%(big_category_f_id,big_category_id)
                                                                     
            
            small_node_f_id = jsonpath.jsonpath(node, '$..sonList[*].fatherCategoryId')
            small_node_id = jsonpath.jsonpath(node, '$..sonList[*].categoryId')
            small_node_name = jsonpath.jsonpath(node, '$..sonList[*].categoryName')
            
            # 遍历小节点,提取数据
            for i in range(len(small_node_f_id)):
                temp = {}
                
                small_category = small_node_name[i]
                small_node_link = 'https://list.jd.com/%d-%d-%d.html'% (big_category_f_id,int(small_node_f_id[i]), int(small_node_id[i]))
                
                temp['big_category'] = big_category
                temp['big_category_link'] = big_category_link
                temp['small_category'] = small_category
                temp['small_category_link'] = small_node_link
                
                
                temp1 = 'shshshfpa=b7071086-4a7e-60d2-8ac2-868abd9b10c7-1642297986; shshshfpb=p6A4NAK8yKsDeEmywpc5LsA; __jdu=16422979858191314349208; unpl=JF8EAMlnNSttUU1QAUsGHBpATg5WW1oPSR4HP2MFVw0LHgMMH1EbEBF7XlVdXhRKFR9sZBRUWFNKUQ4YBisSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAhwXE0hVUlZUDEIXC29lBVFfXUNXBBIyKxUge21cXV8ITB8zblcEZB8MF1QNEgoYE11LWlFdXgBNHwprbgVcXVpLUQceChgTGXtcZF0; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_8755a569a4b3466385a512abdf85b130|1647929066552; areaId=21; ipLoc-djd=21-1861-0-0; PCSYCityID=CN_360000_361100_0; shshshfp=1d19db7ff430ff2f8d258c8973921c30; shshshsID=c1344c4ed7311a46cd28b62f6284fe32_1_1647929069019; __jda=122270672.16422979858191314349208.1642297985.1642467270.1647929067.4; __jdc=122270672; o2-webp=true; __jdb=122270672.5.16422979858191314349208|4.1647929067; 3AB9D23F7A4B3C9B=TLXV4U55UF5BTJP72QO22OELQIG7BITBKGL7HRIXEKGLYKE3T44LSZELCMAU2FC7BH2HBLGWBRTCHCLXQITQVWDA44'
                cookies =  {data.split('=')[0]:data.split('=')[-1] for data in temp1.split(';')}
                headers = {
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                                        '(KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
                            'Referer': 'https://book.jd.com/'
                            }
            # 模拟点击,向小分类连接发起请求(应该就是把请求创建好,返回给引擎,在由他帮我们发送请求,
            # 我们需要指定请求数据的回调方法,也就是解析方法,并且将temp作为meta参数传给引擎,meta可以被传给下一个爬取
            # 的解析请求,让它把爬取到的数据也存入temp中,meta是一个字典)
            yield scrapy.Request(
                url=temp['small_category_link'],
                callback=self.parse_book_list,
                meta={"py21":temp},
                headers=headers,
                cookies=cookies
            )
            
    def parse_book_list(self, response):
        # print(response.body)
        temp = response.meta['py21']
        # print(response.body.decode())
        
        response = response.body.decode('utf-8')
        tree = etree.HTML(response)
        book_list = tree.xpath('//*[@id="J_goodsList"]/ul/li/div')
        
        for book in book_list:
            item = JdItem()
            
            item['big_category']=temp['big_category']
            item['big_category_link']=temp['big_category_link']
            item['small_category']=temp['small_category']
            item['small_category_link']=temp['small_category_link']
            item['book_name'] = book.xpath('./div[3]/a/em/text()')
            item['author'] = book.xpath('./div[4]/span[1]/a/text()')
            item['book_link'] = book.xpath('./div[1]/a/@href')

            print(item)
        
        
        