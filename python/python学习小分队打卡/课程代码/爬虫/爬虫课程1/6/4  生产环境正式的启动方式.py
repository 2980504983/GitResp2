"""
    生产环境正式的启动方式(开启mongodb server):
        sudo mongod [--auth --dbpath=dbpat --logpath=logpath --append --fork] [--f logfile]
        只以 sudo mongod 命令启动时, 系统默认将数据存放在了/data/db目录下了,这个目录需要手动创建。
        --dbpath 指定数据库的数据存放路径
        --logpath 指定日志存放的路径
        --append 或 --logappend 设置日志写入形式为追加模式
        --fork 或 -fork 开启新的进程运行mongodb服务
        --f 或 -f 配置文件路径(可以将上述配置信息写入文件然后通过该文件中的参数进行加载启动)
        --auth 以权限认证的方式启动

    查看是否启动:
        ps aux|grep mongod

    启动mongodb客户端(mongo shell):
        启动本地客户端: mongo
        查看帮助: mongo-help
        退出: ctrl c  or exit

    mongodb的简单使用:
        在开启mongodb server的情况下，在进入mongo shell后 就可以简单的使用了

    mongodb数据库命令:
        查看当前数据库:
            db(没有切换数据库的情况下默认使用test数据库,text数据库直接用show dbs是查看不出来的,因为前面的命令是查看在磁盘中的数据库,而test
               是存在内存中的)

        查看所有数据库:
            show dbs/show databases

        切换数据库(没有则创建数据库):
            use db_name

        删除当前数据库：
            db.dropDatabase(), 你在那个数据库上就删除那个数据库



            



"""