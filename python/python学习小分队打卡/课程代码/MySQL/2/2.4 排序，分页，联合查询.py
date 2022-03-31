"""
    排序：
        order by 子句来将查询数据排序后再返回数据:
        例子: select * from 表名 where order by 字段名;
        后面加上一个desc表示降序

    分页(限制操作个数):
        limit 子句用于限制select语句返回的数据数量，或者update，delete语句的操作数量
        例子: delete from 表名 where age=17 limit 1;

    联合查询:
        union 操作符用于连接两个以上的select 语句，将结果组合一个结果集合中。多个select语句会删除重复的数据(也可以通过参数设置可以有重复)
        例子: select * 表名 where score = 100 union select * from 表名 where sex='w';
        union 比and的效率高 ，union后面加一个 all表示不去重，两个select语句字段个数必须一致

    数据备份(不属于sql语句,要在终端执行，即推出mysql登录):
        1 备份命令格式:
            mysqldump -u用户名 -p库名> 备份地址/新库名.sql
            all-databases 备份所有数据库

        2 恢复命令格式:
            mysql -u用户名 -p备份到那个数据库(库名) < 库名(要备份的数据库).sql



"""