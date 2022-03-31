"""
    外键(foreign key):
        让当前表字段的值在另一个表的范围内选择

        语法:
            foreign key(参考字段名)
            references 主表(被参考字段名)
            on delete 级联动作
            on update 级联动作
            
            eg1:
                主表
                mysql> create table master(id int auto_increment primary key,
                    -> name varchar(20),
                    -> class varchar(10),
                    -> money decimal(6,2)
                    -> )charset=utf8;

                mysql> create table slave(
                    -> stu_id int,
                    -> name varchar(20),
                    -> money decimal(6,2),
                    -> foreign key(stu_id) references master(id)
                    -> on delete cascade on update cascade)
                    -> charset=utf8;
                    
            注意: 一个字段不能又是主键,又是外键

            
        使用规则:
            1 主表,从表字段数据类型要一致
            2 主表被参考字段： KEY的一种,一般为主键
            
        
    小tip:
        查看表结构时,有时会出现int后面有括号的情况例如int(11),但是创建的时候明明没有加只写了int
        注意int(11) 和 varchar(11)后面的数字并不是一个意思,int后面的数字表示显宽度例如100就是三个长度

"""