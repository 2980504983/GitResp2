"""
    练习:
        1 创建数据库 grade
            create database grade charset=utf8
        2 在数据库中创建表 student
        3 表字段如下:
            id name age hobby score
            use grade
            create table student (id int primary key auto_increment, name varchar(32),age int,hobby set())

        4 插入若干数据:
            age 4-16
            score 0--100
            hobby football computer running basketball
            insert into student values (1, 'yang', 8, 'running,computer', 99, )
        5 查找
            1 查找所有年龄不到10岁，或者大于14岁的同学
            2 查找兴趣爱好中包含computer的同学
            3 查找年龄大于等于15 又喜欢足球的同学
            4 查找不及格兴趣爱好又不为空的同学
            5 查找成绩大于90分的所有同学，只看姓名和成绩

        插入字段
        ALTER TABLE <表名> ADD <新字段名> <数据类型> [约束条件] AFTER <已经存在的字段名>;

"""