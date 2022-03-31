"""
    抓包技巧:
        All,XHR(ajex),js, 按住ctrl可以多选

    数据提取:
        1 响应内容的分类:

            1 结构化响应内容:
                1 json数据(json字符串):
                    可以通过 re, json, jsonpath模块来提取特定数据
                2 xml数据:
                    可以通过 re, lxml模块提取数据

            2 非结构化响应内容:
                1 html数据:
                    可以通过re,和lxml模块提取数据

            注: html和xml都是带标签的，他们有什么区别，xml为了传输和存储数据，侧重点在于数据
            内容本身，html的重点则是显示数据

        2 常用数据解析方法:
            详细见，常用数据解析方法.jpg
            Beautifulsoup模块，性能较差，速度慢，因此用的少

"""