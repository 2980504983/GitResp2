"""
    嵌套查询(子查询):
        把内层的查询结果作为外层的查询条件
        
        语法:
            select ... from 表名 where 条件(select ...);
            
        eg1:
            select name,attack from sanguo where attack <
            (select avg(attack) from sanguo);
            
        eg2:
            select name, attack from sanguo where (country, attack ) in
            (select country, max(attack) from sanguo group by country)



"""