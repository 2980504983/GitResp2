"""
    url 结构:
        protocol(协议)://hostname(主机名/域名)[port,一般不用填]/path(路由地址,表示服务器主机一个目录或者文件的地址) 
        [?query 表示查询][#fragment 信息片段]
        
    view(视图函数):
        用于接受客户请求并通过HttpResponse对象返回数据的函数
        eg1:
            def xxx_view(request[其他参数])
                return HttpResponse对象
                
    Django中的路由配置:
        1 创建一个视图文件
        2 在django项目中的urls文件中,导入视图文件
        3 将视图文件中写好的时间处理函数与特定的路由相关联

    小tip:
        ctrl + c 是终止程序
        ctrl + z 是将程序放在后台,程序处于停止状态
        python中 == 表示的是两个变量的值是否相等 ,is 表示的是两个变量值是否相等,
        并且内存地址是否相同,即是否是同一个对象
"""