"""
    利用requests.session 进行状态保持:
        作用:
            也就是不用每次请求都设置cookie，作用就是自动保持，cookie
        场景:
            连续的多次请求都需要带cookie
        使用方法:
            session = requests.session() # 实例化session对象
            response = session.get(url, headers, ...)
            response = session.post(url, data, ...)
            注: session对象发送get或post请求的参数,与requests模块发送请求的参数完全一致
"""

