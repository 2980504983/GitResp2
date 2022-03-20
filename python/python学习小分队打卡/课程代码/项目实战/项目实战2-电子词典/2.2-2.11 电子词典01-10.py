"""
    电子词典:
        功能说明:
            1 用户可以登录和注册
            2 可以通过基本图形界面print提示客户端输入
            3 客户端启动后进入一级界面，登录注册退出
            4 用户登录后进入二级界面，查单词，历史记录，注销
        思考过程:
            1 确定技术方案 (套接字，并发，细节确定):
                * tcp数据报套接字
                * Process多进程
                * 历史记录 : 查看前十条
                * 注册成功: 直接登录

            2 数据表进行建立 (dict: words):
                * 用户表 user -> name passwd
                create table user (id int primary key auto_increment, name varchar(32) not null, passwd varchar(128) not null);

                * 历史记录表 hist -> id name word time
                create table hist (id int primary key auto_increment, name varchar(32), word varchar(28) not null, time datetime default now());

            3 结构设计 (几个模块 封装设计):
                客户端:

                服务端: 逻辑请求处理模块， 数据库操作模块

                函数: 用函数封装

                界面处理:
                    while True:
                        界面一
                        while True:
                            界面二

            4 功能分析和通信搭建:
                并发通信
                注册
                登录
                查单词
                历史记录

            5 罗列功能逻辑 (每个功能确定客户端和服务端分别该做什么):
                注册：
                    客户端:
                        输入注册信息
                        发送请求
                        得到反馈
                    服务端:
                        接收请求
                        判断是否允许注册
                        允许注册将用户信息存入数据库
                        给客户端反馈结果
                登录：
                    客户端:
                        输入用户名密码
                        发送请求给服务器 Q name word
                        得到服务器反馈
                    服务端:
                        接收请求
                        判断是否允许登录
                        发送结果

                查单词:
                    客户端:
                        输入单词，发送请求
                        等待接收结果

                    服务端:
                        接收请求
                        查找单词
                        发送结果
                        插入历史记录
                历史记录

            6 设定客户端服务端协议:
                注册  R
                登录  L
                查单词  Q
                历史记录  H
                退出  E

    扩展知识:
        getpass模块(隐藏输入)，
        pwd = getpass.getpass()
        在终端执行，输入会被隐藏，其他和input差不多，pycharm不支持

        hashlib模块(转换加密)
        hash = hashlib.md5() # 生成对象
        hash.update(pwd.encode()) # 算法加密
        pwd = hash.hexdigest() # 提取加密后的密码

        即使密码用算法加密了，也可以被逆推破解，因此可以用算法加盐
        算法加盐:
            就是提前准备一个字串(#$awv),也称之为盐. 当用户创建了密码后，将密码与盐进行混合拼接，在进行算法加密.
            这样，即使密码被破解了，黑客们得到的也是与盐混合的密码，如果不知道盐是什么，也就无法知道真正的密码
        hashlib模块也就加盐的接口:
            hash = hashlib.md5("盐".encode())  # 加盐处理
"""



