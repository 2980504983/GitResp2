"""
    mysql查询语句的执行顺序(前面的数字表示优先级,越小越先执行,排列的顺序表示写的时候的顺序):

        3 select ... 聚合函数 from 表名

        1 where ... 

        2 group by...

        4 having ...

        5 order by ...

        6 limit ...



    聚合函数:
        avg(字段名) 该字段平均值
        max(字段名) 该字段最大值
        min(字段名) 最小值
        sum(字段名) 所有和
        count(字段名) 统计该字段记录的个数 (count中的字段名填id是最稳妥的,因为如果是其他字段名有可能值是NULL,而如果有一条记录的该字段名的值是NULL,
                                        会被count跳过,也就是count的字段名最好要是不会出现空值的字段名,否则会出现遗漏的情况)

        eg1:
            找出表中的最大攻击力的值:
            select max(attack) from sanguo;

        eg2:
            蜀国英雄中攻击值大于200的英雄的数量
            select count(id) as number from sanguo where country='蜀国' and attack > 200;
            (as number 就是在显示的时候将 count(id)变成number,相当于临时去一个别名)

    grounp by:
        给查询的结果进行分组:
            eg1:
                计算每个国家的平均攻击力:
                select country,avg(attack) from sanguo group by country;
                分组操作相当与mysql先根据你给的字段进行分组,在分别进行查询

            eg2:
                select country, count(id) as number from sanguo 
                where gender='M' group by country 
                order by number DESC
                limit 2;

            注:
                用了group by后 select 后面你自定义的原生字段,要么是被聚合函数包裹的,要么就是被分组的字段
                如果出现了有没有被聚合函数包裹,并且也不是被分组的字段,就会报错

    having语句:
        对分组聚合后的结果在进行进一步筛选：
            eg1:
                找出平均攻击力大于105的国家的前2名,显示国家名称和平均攻击力
                select country,avg(attack) from sanguo 
                group by country 
                having avg(attack) > 105
                order by avg(attack) DESC
                limit 2;

        注: having 语句通常与group by联合使用,因为where只能筛选分组前的数据,而having是筛选分组后的数据
            having 语句弥补了where不能与聚合函数联合使用的不足

    distinct语句:
        不显示字段重复值
            eg1:
                表中有哪些国家:
                select distinct country from sanguo;
            eg2:
                计算一共有多少个国家:
                select count(distinct country) from sanguo

        注: distinct右边的字段不能做聚合,
            并且如果distinct右边有多个字段,则多个字段都相同才是重复值

    查询表记录时做数学运算:
        运算符: + - * / % **
        eg1:
            查询时显示攻击力翻倍
            select name, attack*2 from sanguo;
        eg2:
            更新蜀国所有英雄攻击力 * 2
            update sanguo set attack=attack*2 where country='蜀国';

        注: 是否改变数据库中的值,在于前面是写操作还是读操作
                



    SQL中只要用到聚合函数就一定要用到group by 吗?:
        答：看情况
        1、当聚集函数和非聚集函数出现在一起时,需要将非聚集函数进行group by
        2、当只做聚集函数查询时候,就不需要进行分组了。

        举例来说，
        SELECT SUM(TABLE.A )  FROM  TABLE
        上述SQL不需要使用Group by 进行分组,因为其中没有非聚合字段,所以不用Group by 也可以。
        如果是SELECT SUM(TABLE.A ),MAX(B), FROM  TABLE GROUP BY B
        由于B是非聚合字段,则需要使用MAX()或者其他聚合函数并且Group by 才可以正常执行

                




"""