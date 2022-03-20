"""
    scrapy的工作流程:
        1 回顾之前爬虫的工作流程:
            详细见 crawler_process.jpg
            缺点: 各种流程,只要一步挂了,整个流程就挂了

        2 上面的流程可以改写为:
            详细见 scrapy_process_analysis.jpg 对scrapy流程的解析
            其实就是在爬虫的流程中,加入了引擎,因为你可以想一想,我们平时打电话,
            是直接将电话线连到别人那的吗？我们是有一个中转点的,哪个点事营业厅,也就是联通或者
            移动,在我们这里就是引擎.(各类模块将数据发送给引擎,引擎检索数据,无误后,在将数据发送给
            其它模块,这里引擎应该大概就是这个意思)

        3 scrapy的流程:
            详细见scrapy_process.png

        4 scrapy流程描述:
            详细见scrapy_process_describe.png

        5 scrapy的三个内置对象:
            详细见scrapy_built-in_obj.png
"""