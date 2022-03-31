"""
    创建项目指令:
        django-admin startproject 项目名称
        
    运行服务器项目:
        python3 manage.py runserver 可以指定选用本地的那个ip和端口
        
    django文件构成:
        1 manage.py:
            django的主模块,在开发阶段用于管理整个项目的开发运行的调试
            
            它包含很多管理项目的子命令:
                python3 manage.py runserver 启动服务
                python3 manage.py startapp 创建应用
                ...
            在改文件中有一句execute_from_command_line(sys.argv)。sys.argv就是我们在终端输入的参数例如runserver,
            它就是通过传递这个参数给execute..方法,并让它执行
            不加参数,直接执行 python3 manage.py会显示所有子命令
            
        2 mysite1(项目名) 项目包文件夹:
        
            1 __init__.py:
                包初始化文件,当此项目包被导入(import)时,此文件会自动运行
                
            2 wsgi.py:
                WSGI 即 web server gateway interface (web网关接口)
                web服务网关接口的配置文件,进部署项目时使用
                
            3 urls.py:
                项目的基础路由文件,所有的动态路径必须走该文件进行匹配
                
            4 settings.py:
                项目配置文件,文件中的一些全局变量会为框架运行传递一些参数
                启动服务时会调用settings.py文件
                你也可以自定义一些参数
                
            注: django文件每当改变并保存后,如果你此时正在运行,就会重新启动,
                BASE_DIR 是动态生成的项目跟目录,__file__表示当前文件的路径
                ALLOWED_HOSTS = [] 表示允许那些主机访问,['*']表示所有机器都能访问
                TIME_ZONE 表示显示那个时间,默认是英国时间
                
            
        
"""