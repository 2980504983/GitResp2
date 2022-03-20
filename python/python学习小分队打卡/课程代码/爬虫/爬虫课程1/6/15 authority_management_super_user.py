"""
    mongodb权限管理:
        mongodb默认是没有用户的,但是因为，爬虫在互联网上爬取数据,因此如果你的mongodb没有设置密码和权限,别人找到你的ip,就可以直接对你
        的数据库进行修改了

    mongodb的权限管理方案:
        mongodb默认没有管理员帐号,所以要先添加管理员帐号,并且mongodb服务器需要在运行的时候开启验证模式

    创建超级用户:
        sudo mongo
        use admin
        db.createUser({'user':Yang, "pwd":1234,roles:['root']})

    创建普通用户:
        一般用户是创建在admin上,创建普通用户:
        db.createUser({user:'python', pwd:'123', roles[{db:'text1', role:'read'},{...}]})
        因为用户是创建在数据库上的,但是没切换一个数据库就要登录就很麻烦,因此可以用上面的方法,将用户创建在admin上,然后
        规定他在那些数据库上有那些权限

"""