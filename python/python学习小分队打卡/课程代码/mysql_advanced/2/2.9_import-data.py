"""
    数据导入:
        可以导入的文件:
            .sql 全是sql语句 
            .csv 全是数据(Excel)
        作用:
            把文件中的内容导入到数据库中
        语法:
            方式一(数据文件):
                load data infile '文件名'
                into table 表名(在插入数据前,要先建立好对应的表)
                fields terminated by '分隔符'
                lines terminated by "\n"; (这里表示以什么换行)
                
            方式二(sql语句文件):
                source 文件名.sql
                
    数据导出:
        作用:
            将数据库中表的记录保存到文件中
            
        语法:
            select ... from 表名 (可以指定字段)
            into outfile '文件名'
            fields terminated by '分隔符'
            lines terminated by '以什么换行';
            
    注意:
        mysql有一个自定义的安全路径用于存放导入和导出的文件,当要导出或导入的文件不在里面会报错
        查看mysql安全存放文件的路径 show variables like '%secure%';
                
    练习:
        添加id字段,要求主键自增长,显示宽度为3,位数不够用0填充:
            alter table 表名 add id int(3) zerofill primary key auto_increment first;
                 
"""