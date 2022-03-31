"""
    SQL语句:
        操作关系型数据库的语句,以分号结尾

    MySQL 数据库操作:
        数据库操作:
            1 查看已有数据库:
                show databases;

            2 创建库(指定字符集):
                create database 库名 (character set utf8)可选

            3 查看创建的数据库的语句:
                show create database 库名;

            4 查看当前正在使用的数据库:
                select database();

            5 切换库:
                use 库名;

            6 删除库:
                drop database 库名;

            7 库名的命名规则:
                数字，字母，下划线，不能使用纯数字
                不能使用特殊字符以及mysql关键字

        数据表的管理:
            1 表结构设计初步
                1 根据需求判断要存什么内容
                2 根据内容设计字段
                3 根据字段特征选择数据类型(字段中的内容数据类型必须一致)
            2 数据类型支持:
                数字类型:
                    整数类型:
                        TINYINT, SMALLINT, MEDIUMINT, INT, BIGINT
                        (区别是所占磁盘空间大小不同,例如TINYINT占一字节, 有符号范围(-128, 127), 无符号范围(0, 255))
                        详细区别见mysql数字类型.jpg
                    定点类型:
                        DECIMAL
                    浮点类型(近似值):
                        FLOAT， DOUBLE
                    比特值类型 - BIT，0表示假，1表示真

                字符串类型:
                    CHAR 和 VARCHAR类型
                        char:
                            定长效率高， 会浪费空间
                        varchar:
                            不定长效率低，不会浪费空间
                    text 和 blob:
                        text:
                            文本
                        blob:
                            二进制文件
                    enum 和 set:
                        enum:
                            用来存储给出的一个值
                        set:
                            用来存储给出的值中的一个或多个值



                    详细见mysql字符串类型.jpg



"""