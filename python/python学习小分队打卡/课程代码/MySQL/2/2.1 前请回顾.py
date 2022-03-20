"""
    前请回顾:
        1 基础概念:
            1 为什么要用数据库:
                存储方便，效率高，降低冗余，提高一致性
            2 什么是数据库:
                存储数据的仓库
            3 数据库简单分类:
                关系型:
                    二维表，sql语句
                非关系型:
                开源&非开源
                大型&中型&小型
            4  关系型数据库的组成结构:
                数据元素 --> 记录(一行) --> 数据表 --> 数据库
                数据库(database)
                数据表(table)
                字段(column)
                记录(row)
                主键(用于区分各个记录，primary key)

        2 mysql：
            关系型，开源，c/c++写的, 安装
        3 sql语句:
            数据库操作:
                show databases; 查看数据库
                create database name; 创建一个数据库
                select database(); 查看当前正在使用的数据库
                show create database name; 查看数据库创建语句
                use name; 切换数据库
                drop database name; 删除数据库

            数据表操作:
                show tables 查看数据表
                create table name column1 type... 创建数据表
                    字段描述:
                        primary key 主键
                        unsigned  无符号
                        not null
                        default 默认值

                    数据类型:
                        数字:
                            整数，小数，布尔
                        字符串:
                            (char,varchar ,blob,text,enum, set...)
                        时间日期:
                            还没讲
                desc name 查看表结构
                drop table 删除数据表

            增删改查:
                增:
                    insert into 表名 values(值1，值2...)，...; (每一组值代表一条记录)(用该方法输入信息时必须囊括所有字段，有默认值也不行)
                    insert into 表名(字段1,...) values(值1,...),...;

                删:
                    delete from 表名 where 条件;
                    注意: delete语句后不加where条件，所有记录全班清空
                    delete from class_1 where name='x';

                改:
                    update 表名 set 字段1 = 值1, 字段2= 值2,... where t条件;
                    update class_1 set age=11 where name='yan';
                查:
                    select * from 表名 [where 条件];
                     select 字段名1, 字段名2 from 表名 [where 条件];

                where子句:
                    算数，逻辑，比较，位运算

            表结构修改语句:
                    在文件夹1中，详细见表字段操作.jpg

"""