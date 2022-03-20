"""
    中间件selenium的使用:
        使用场景:
            1 需要的数据是页面渲染之后才出来的(也就是刚开始发送过来的数据经过
                渲染(计算等操作)才是最终呈现的数据)
            2 模拟登录时,很难,可以用selenium先登录在取出cookie在爬取

        使用原理:
            如果要爬取的数据是js生成的,可以通过在中间件中设置selenium获取渲染后的页面源码
            ,在通过中间件将response返回给引擎

        使用方法:
            在中间件文件中,定义一个类,class SeleniumMiddleware:
            详细见seleniumMiddleware.py
"""