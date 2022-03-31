"""
    用中间件随机请求头:
        1 在settings文件中:
            创建USER_AGENT_LIST = []
            里面放许多请求头
        2 进入middlewares.py文件中(将原有内容注释掉或者删掉)
        3 定义一个中间件类(class RandomUserAgent):
            在类中定义一个方法:
                def process_request(self request, spider):
                    ua = random.choice(USER_AGENT_LIST)
                    request.headers['User-Agent'] = ua
        4 在settings文件中将中间件功能开放,修改一下类名

"""