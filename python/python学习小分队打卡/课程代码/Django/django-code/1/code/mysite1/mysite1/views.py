# file: mysite1/views.py

from django.http import HttpResponse


def page1_view(request):
    html = "<h1>title<h1>"
    return HttpResponse(html)

def pagen_view(request, n):
    # n绑定的是urls文件中正则分组中匹配的字符串,有几个正则分组就要有几个参数来绑定
    # 例如有两个分组就要创建两个形参来接受,n,n1
    html = "<h1>===这是第%s个页面<h1>" % n
    return HttpResponse(html)

def math_view(request, x, op, y):
    x = int(x)
    y = int(y)
    result = None
    if op == 'add':
        result = x+y
    elif op == 'sub':
        result = x-y
    elif op == 'mul':
        result = x*y
    if result is None:
        return HttpResponse("出错啦")
    html = '结果:'+str(result)
    
    # 调用请求体的信息,此时我们是服务端,所以应该是请求体,request还有很多属性,
    # 具体自行百度
    html1 = "你的IP是:" + request.META['REMOTE_ADDR']
    
    # HttpResponse 中的参数必须是一个字符串
    return HttpResponse(html1)
    
    # # HttpResponse 中的参数必须是一个字符串
    # return HttpResponse("结果:"+ str(result))

def person_view(request, **kwargs):
    s = str(kwargs)
    return HttpResponse(s)

def birthday_view(request, y, m, d ):
    html = "生日:"+y+'年'+m+'月'+d+'日'
    return HttpResponse(html)
    
