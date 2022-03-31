"""
    索引分类:
        普通(MUL) 和 唯一(UNI):
            使用规则:
                1 可以设置多个字段
                2 普通索引: 
                    字段值无约束,KEY表示为MUL
                3 唯一索引(unique):
                    字段值不允许重复,但可以为NULL,KEY标志为UNI
                4 那些字段创建索引:
                    经常用来查询的字段,where条件判断字段,order by排序字段
                    
            创建普通索引和唯一索引:
                创建表时:
                    create table 表名(
                        字段名 数据类型,
                        ...,
                        index(字段名), 创建普通索引
                        unique(字段名), 创建唯一索引
                    );
                    
                已有表中创建:
                    create [unique] index 索引名 on 表名(字段名);
                    
                查看索引:
                    1 desc 表名;
                    2 show index from 表名[\G];
                    
        主键(PRI)和自增长(auto_increment)
            使用规则:
                1 一个表里只能有一个主键字段
                2 所带约束: 不允许重复,且不能为NULL
                3 KEY标志(primary): PRI
                4 通常设置记录标号字段id,能唯一锁定一条记录
                
            创建:
                创建表添加主键:
                    create table name(
                        id int auto_increment,
                        name varchar(20),
                        primary key(id)
                    )charset=utf8, auto_increment=10000; 设置自增长起始值为10000(可以哄人,因为把自增长起始值设的高一点,当返回数据时,
                                                                              显示的id会高,就好像真的有那么多用户一样,但是记得以后操作要减回去)
                    还有一种方法: id int primary key auto_increment,
                    
                已有表添加主键:
                    alter table 表名 add primary key(id);
                    
                已有表操作自增长属性:
                    1 已有表添加自增长属性:
                        alter table 表名 modify id int auto_increment;
                    2 已有表重新指定起始值:
                        alter table 表名 auto_increment=20000;
                        
            删除:
                1 删除自增长属性(modify):
                    alter table 表名 modify id int;
                    
                2 删除主键索引:
                    alter table 表名 drop primary key;
                    
                


"""