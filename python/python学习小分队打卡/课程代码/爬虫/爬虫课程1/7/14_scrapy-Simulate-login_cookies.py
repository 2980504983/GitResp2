"""
    scrapy模拟登录:
        1 回顾之前模拟登录的方法:
            1 requests实现模拟登录:
                1 直接携带cookies请求页面
                2 找url地址,发送post请求存储cookie
                注: 一般还要配合session使用

            2 selenium实现模拟登录:
                1 找到对应input标签,输入文本点击登录

            3 scrapy的模拟登录:
                1 直接携带cookies
                2 找url地址,发送post请求存储cookie
                注: 和requests差不多,但是实现略有不同

        2 scrapy模拟登录:
            1 直接携带cookies参数:
                应用场景(什么时候用cookies参数):
                    1 cookie过期时间很长,常见于一些不规范的网站
                    2 能在cookie之前把所有数据拿到
                    3 配合其它程序使用,比如使用selenium把登录之后的cookie获取并保存到
                      本地,scrapy发送请求之前先读取本地cookie
                    注: 这种方法还是很简单的,不过你要先登录,获取到cookies,然后通过这个cookies
                        登录
                        scrapy 中cookie不能存放在headers中

                实现(以登录github为例):
                    重构scrapy的starte_rquests方法


            2 找url地址,发送post请求存储cookie:
                1 scrapy.Request发送post请求:
                    我们可以通过scrapy.Request()指定method,body参数来发送post请求,但是
                    通常使用scrapy.FormRequest()来发送post请求

                2 思路分析:
                    1 找到post的url地址: 点击登录按钮进行抓包,然后定位url地址为https://github.com.session
                    2 找到请求体的规律,分析post请求的请求体,其中包含的参数均在前一次的响应中
                    3 是否登录成功,通过请求个人主页,观察是否包含用户名


"""