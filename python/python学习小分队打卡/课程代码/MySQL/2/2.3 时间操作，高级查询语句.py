"""
    高级查询语句:
        模糊查询和正则查询:
            like 用于在where子句中进行模糊查询，like子句中使用 % 表示任意0个或多个字符， _ 表示任意一个字符
            例子: select * from 表名 where name like 'A%';

            mysql中对正则表达式支持有限，只支持部分正则元字符
            例子: select * from 表名 where 字段名 regexp 正则表达式;


"""