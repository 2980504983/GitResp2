"""
    中间件的使用:
        1学习目标:
            1 使用中间件实现随机UA的方法
            2 通过中间件是实现代理ip
            3 scrapy和selenium的配合使用

        2 scrapy中间件的分类和作用:
            1 scrapy中间件的分类:
                根据scrapy运行流程中所在位置的不同分为(图上的位置)
                1 下载器中间件
                2 爬虫中间件

            2 scrapy中间件的作用(预处理request和response对象):
                1 对headers或者cookie进行更换和处理
                2 使用代理ip等
                3 对请求进行定制化操作

                但在scrapy默认的情况下,两种中间件都在middlewares.py中
                爬虫中间件的使用方法和下载器中间件的使用方法相同,且功能重复,
                通常使用下载器中间件

        3 下载器中间件的使用方法(同一种中间件可以有多个):
            1 在middleware.py中定义中间件类
            2 在中间件中,重写处理请求或者响应的方法:
                1 process_request(self, request, spider)
                    1 返回None 如果所有下载器中间件器中间件都返回None,则请求最终被交给下载器处理
                    2 返回request 如果返回为请求,则将请求交给调度器
                    3 返回response 如果返回为响应,将响应对象交给spider进行解析
                    详细见using-middleware.py

                2 process_response(self, request, response, spider)
                    当下载器完成http请求,传递响应给引擎的时候使用
                    1 返回request 如果返回为请求,则将请求交给调度器
                    2 返回response 如果返回为响应,将响应对象交给spider进行解析
                    详细见using-middleware.py
            3 在settings文件中开启中间件的使用:
                同管道的方法,找到中间件配置,打开就行了


"""