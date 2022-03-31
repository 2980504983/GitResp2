"""
    表操作_查:
        select(查看表中数据):
            select * from 表名 [where 条件];
            select 字段名1, 字段名2 from 表名 [where 条件];

        where子句(筛选数据):
            通过一定运算条件，进行数据筛选

            mysql主要有以下几种运算符:
                算数运算符:
                    + - * / %(取余)

                比较运算:
                    =， !=， >， <， >=， <=， between and(两者之间)， not between and，in(在集合中)，not in，is NULL， is not NULL ...

                逻辑运算符:
                    not and or xor(相同为假，不同为真)

                位运算:
                    与python中一样

    更新表记录:
        update 表名 set 字段1 = 值1, 字段2= 值2,... where t条件;
        update class_1 set age=11 where name='yan';

    删除表记录:
        delete from 表名 where 条件;
        注意: delete语句后不加where条件，所有记录全班清空
        delete from class_1 where name='x';

    表字段的操作(alter)：
        详细见表字段操作.jpg



"""