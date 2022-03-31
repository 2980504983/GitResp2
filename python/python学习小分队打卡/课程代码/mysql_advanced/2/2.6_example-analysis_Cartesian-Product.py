"""
            
    笛卡尔积(谨慎使用):
        就是一个集合与另一个集合交叉
        select 字段名列表 from 表名列表;
        eg1:
            select tt1name from tt1,tt2;
            返回tt1表的所有字段和tt2表的所有字段,的所有排列组合(数据量大谨慎使用)
            
        谨慎使用,笛卡尔积的量是很大的,会大量占用内存
        及时你在多表查询
        
        
    多表查询:
        1 根据文件执行sql语句:
            source 文件路径(文件必须是sql脚本也就是后缀名为sql的文件)
            
        2 必须在表不存在时才创建表(建议加,这样更安全)
            create table if not exists 表名(...)
            
        3 多表查讯示例:
            1 不推荐:
                eg1:
                    select province.pname, city.cname from province,
                    city where province.pid = city.cp_id;
                    
            2 连接查询(推荐使用):
                1 内连接:
                    select 字段名 from 表1 inner join 表2 on 条件 inner
                    join 表3 on 条件;
                    
                    eg1:
                        select province.pname, city.cname from province inner join
                        city on province.pid = city.cp_id;
                        
                2 外连接:
                    左外连接:
                        以左表为主显示查询结果(没匹配上的会显示空)
                        select 字段名 from 表1 left join 表2 on 条件 left
                        join 表3 on 条件;
                        
                    右外连接:
                        用法同左连,以右表为主显示结果
                        select 字段名 from 表1 right join 表2 on 条件 right
                        join 表3 on 条件;
                                      
                
        注意:
            1 多表查询的时候要写表名.字段名,不要直接写字段名
            2 记住多表查询的时候一定要带条件,否则就是笛卡尔积,但是即使加了where也是在笛卡尔积中查询的,
              所以笛卡尔积最好别用

"""