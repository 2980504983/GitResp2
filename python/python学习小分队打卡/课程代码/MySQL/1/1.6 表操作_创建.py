"""
    表的基本操作:
        创建表(指定字符集):
            create table 表名(字段名 数据类型， 字段名 数据类型，...);
            1 如果想设置数字为无符号加上 unsigned
            2 不想字段为Null， 设置字段属性为not null，如果设置后输入了空则会报错
            3 default 表示设置一个字段下面内容的默认值
            4 auto_increment 定义列的自增属性，一般用于主键(也就是唯一确定一条记录的标志，类似id的作用)，数值会自动加一
            5 primary key 关键字用于定义列为主键，主键的值不能重复

            例子:
            mysql> create table interest (id int primary key auto_increment,name varchar(32) not null,hobby
            set('sing','dance','draw'),price decimal(7,2),lever char not null,comment text);

        查看表:
            show tables;

        查看表如何被创建:
            show create table 表名;

        查看表结构:
            desc 表名;

        删除表:
            drop table class

    数据的基本操作:
        插入:
            insert into 表名 values(值1，值2...)，...; (每一组值代表一条记录)(用该方法输入信息时必须囊括所有字段，有默认值也不行)
            insert into 表名(字段1,...) values(值1,...),...; (这种方法，前面写了那些字段，后面值对应写上就好啦，
                                                            没填的有默认值就是默认值，没有的就是null)
"""