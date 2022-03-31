"""
    认识关系型数据库和MySQL
        1 数据库结构(图库结构)
            数据元素(单个数据) --> 记录(一条) --> 数据表(多条记录) --> 数据库

        2 数据库概念解析:
            数据表:
                存放数据的表格(二维表)
            字段:
                每列用来表示该列数据的含义
            记录:
                每个行，表示一组完整的数据

        3 MySQL特点:
            1 开源数据库，使用C和C++编写
            2 支持各种平台
            3 为各种语言提供API

        4 MySQL下载:
            linux：
                服务端: sudo apt-get install mysql-server
                客户端(图形化): sudo apt-get install mysql-client

            windows：
                官网下载

        5 启动和连接mysql:
            服务端启动:
                查看mysql状态: sudo/etc/init.d/mysql status
                启动服务: sudo /etc/init.d/mysql start (stop, restart)

            客户端连接:
                命令格式:
                    mysql -h主机地址 -u用户名 -p密码
                    mysql -hlocalhost -uroot -p223309
                    本地连接可省略 -h选项: mysql -uroot -p223309
            关闭连接:
                ctrl D
                exit

    SQL语句:


"""