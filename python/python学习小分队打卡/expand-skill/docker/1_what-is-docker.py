"""
    什么是虚拟化:
        虚拟化是一种资源管理技术,是将计算机的各种实体资源,如服务器,网络,内存及存储等,予以抽象
        转换后呈现出来.例如我们可以在windows系统上装虚拟机跑linux系统,但是系统明明是跑在硬件上的
        呀,所以这里就用到我们的虚拟化技术
        
    什么是docker:
        docker也是一个虚拟化的技术,功能类似虚拟机,但是不需要进行硬件的虚拟,因此比虚拟机更加轻量,
        
        使用docker就不用一个一个配置环境了,你可以下载人家配置好的环境镜像
        (类似于快照,或者源代码体积较小),通过镜像生成一个个容器(类似与通过快照生成虚拟机的一个操作系统环境)
        
    docker常用命令:
        1 帮助启动类命令:
            启动docker : systemctl start docker
            停止docker : systemctl start docker
            重启docker : systemctl restart docker
            查看docker状态 : systemctl status docker
            开机启动 : sysemctl enable docker
            查看docker概要信息 : docker info
            docker 总体帮助文档 : docker --help
            命令帮助文档 : docker 具体命令 --help
            
        2 镜像命令:
            1 docker images:
                列出本地主机上的镜像
                -a 列出本地所有的镜像, 含历史镜像层
                -q 只显示镜像id
                
            2 docker search 镜像名:
                在docker hub上的查找该镜像,显示有关该镜像的相关信息
                --limit 只列出n个镜像,默认25个
                docker search --limit5 django
                
            3 docker pull 镜像名:TAG (版本号没写默认是最新的也就是lastest):
                下载镜像
                
            4 docker system df
                查看镜像,容器,数据卷所占的空间
            
            5 docker rmi 镜像名称/镜像id
                删除镜像
                -f 强制删除
                删除多个
                docker rmi -f 镜像名1:TAG 镜像名2:TAG
                删除全部镜像
                
            虚悬镜像:
                仓库名,标签名都是none的镜像
                
        3 容器命令:
            1 新建+启动容器:
                docker run [options] image [command][ARG...]
                options:
                    --name='容器名称',不指定,就会随机分配
                    -d 后台运行容器并返回id
                    -i 交互式前台运行容器,通常与-t一起使用
                    -t 为容器重新分配一个伪输入终端,通常和-i一起使用(直接写成-it,docker中很多命令都可以这样组合使用)
                    -P 随机端口映射,大写P
                    -p 指定端口映射,小写p
                    docker容器运行时会有一个端口,但是docker内部的各种环境软件也要运行,所以也有
                    端口例如 8080:80就表示在8080端口的docker容器中,占用80端口的运行的程序
                    eg1:
                        运行ubuntu操作系统容器,并且调出能让我继续操作这个ubuntu系统的终端
                        docker run -it ubuntu /bin/bash
                        
            2 列出当前所有正在运行的容器:
                docker ps[options]
                -a 列出当前正在运行的容器+历史上运行过的
                -I 显示最近创建的容器
                -n 显示最近n个创建的容器
                -q 静默模式 只显示容器编号
                
            3 退出容器:
                exit:
                    run进去的,exit退出,容器停止
                ctrl+p+q:
                    run进去的,退出终端,但是容器不停止
                    
            4 启动已经停止运行的容器:
                docker start 容器id/容器名
                
            5 停止容器:
                docker stop 容器id/容器名
                
            6 强制停止容器:
                docker kill 容器id/容器名
            
            7 删除已停止的容器:
                docker rm 容器id/容器名
                -f 强制删除
                
            8 补充:
                1 启动守护式容器:
                    docker run -d 容器名 (也就是在后台运行)
                    注:
                        docker容器后台运行,必须有一个前台进程,容器运行的命令如果
                        不是那些一直挂起的命令(比如,top,tail),就会自动退出
                        因此当创建容器后,最好用docker ps -a 查看一些容器是否创建完成,
                        解决办法就是开启一个docker前台应用,也就是开启一个终端
                    
                2 查看容器日志:
                    docker logs 容器ID
                    
                3 查看容器内的进程:
                    docker top 容器ID
                    
                4 查看容器内部细节:
                    docker inspect 容器ID
                    
                5 进入正在运行的容器并以命令行交互:
                    1 docker exec -it 容器ID bashShell(ubuntu的是/bin/bash) 进入正在运行的容器
                        exec实在容器中打开新的终端,并且启动新的进程,在该进程中使用exit退出,不会导致容器退出
                        一般这种用的比较多
                        
                    2 docker attach 容器id 重新进入容器
                        这个不会启动新的进程,在改进程中使用exit,会导致容器退出
                        
                    3 在正式的生产环境程一般先使用-d在后台启动容器,然后在通过exec-it创建一个新的容器进程
                      开干,这样就不会相互影响
                
                6 在容器中拷贝文件到主机:
                    docker cp 容器id:要拷贝文件在容器内的路径 目标主机路径
                    
                7 导入和导出容器:
                    docker export 容器id > 文件名.tar(只能是tar,好像) (导出容器)
                    cat 文件名.tar | docker import -镜像用户/镜像名:镜像版本号  (导入容器)


            
        
        
"""