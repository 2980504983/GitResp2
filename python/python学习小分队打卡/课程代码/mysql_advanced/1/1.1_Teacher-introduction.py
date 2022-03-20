"""
    MySQL基础回顾:
        1 数据库概念:
            数据库：
                存储数据的仓库,实时访问率高
                瓶颈:
                    并发

            数据库软件：
                真是软件例如mongoDB,MySQL,redis

            数据仓库:
                数据量更庞大,多种数据库的总和,更加侧重数据分析和数据挖掘,共企业决策分析使用,主要是数据查询,修改和删除很少,
                实时访问率低
                瓶颈:
                    磁盘 数据格式 带宽

        2 MySQL的特点:
            1 关系型数据库:
                表与表之间有关系
            2 跨平台
            3 支持多种编程语言
            4 基于磁盘存储,数据是以文件形式存放在数据库目录/var/lib/mysql下

        3 启动连接：
            服务端启动(忘记吧,不是你该用的,慎用,曾经一个程序员就因为离职然后关闭数据库被抓):

            客户端连接:
                mysql -hIP地址 -u用户名 -p密码
                本地连接可省略-h选项

        4 基本SQL命令:
            库管理:
                1 查看已有库:
                    show databases;
                2 创建库并指定字符集:
                    create database 库名 charset utf8; (不能使用utf-8)

                3 查看当前当前所在库:
                    select database();

                4 切换库：
                    use 库名

                5 查看库中已有表:
                    show tables;

                6 删除库:
                    drop database 库名;

            表管理:  (字段名不需要加引号)
                1 创建表并指定字符集：
                    create table 表名(字段名 字段类型 xxx,) charset=utf8
                    (直接指定utf8会有一个warning,因为mysql中有utf8mb3和utf8mb4,所以为了避免含义模糊需要你指定清楚)

                2 查看创建表的语句：
                    show create table 表名;

                3 查看结构:
                    desc 表名;

                4 删除表：
                    drop table 表名1,表名2,表名3

            表记录管理：
                跟where或者条件相关的写操作,要先查出来,也就是先查一遍,在进行写操作,关于数据库相关的操作一定要谨慎
                增：
                    insert into 表名(字段名) values(),();

                删：
                    delete from 表名 where 条件,谨慎删除(可以用一种方法替代,就是在创建一个字段表示前面的数据是否有效)

                改：
                    update 表名 set 字段名=值，字段名=值 where 条件；

                查：
                    select 字段名/* from where  (加一个\G格式化输出,更好看)

            表字段管理(alter table 表名):
                增:
                    alter table 表名 add 字段名 字段类型 [first| after 字段名]在某个字段前后

                删：
                    alter table 表名 drop 字段名；也不能随便删,只要跟删相关,要三思而后行

                改:
                    alter table 表名 modify 字段名 新类型；
                表重命名：
                    alter table 表名 rename 新表名；

        数据类型：
            四大数据类型：

                1 数据类型：
                    int(4字节)
                    smallint(2字节)
                    bigint
                    tinyint(一字节)
                    详细见Numeric-type.png

                    float(m, n)(单精度)
                    double(双精度)
                    decimal(货币类型)
                    详细见float-point_fixed-point.png

                2 字符类型：
                    char(4)定长
                    (例如申请四个字符实际只有三个字符,mysql会用空格补,但是查询的时候又会把空格删除,因此char的数据最好不能有空格,
                    一般用于密码)

                    varchar()不定长
                    详细见与char-varchar.png

                    text(大文本,什么新闻内容啊存这里)

                    blob

                3 枚举类型：
                    enum()(少用,坑挺多)

                    set()

                4 时间类型:
                    date
                    time
                    year
                    datetime
                    timestamp
                    注: 在企业中基本所有表中一定要有两个时间,创建时的时间, 更新时的时间(时间类型一般都是datetime)

                5 日期时间函数：
                    NOW()
                    CURDATE()
                    YEAR()
                    TIME()

                6 日期时间运算：
                    select * from 表名 where 字段名 运算符(NOW()-interval 间隔);
                    间隔单位： 1 day | 3 month | 2 year
                    eg1:查询一年前的用户充值信息
                    select * from 表名 where time < (NOW()-interval 1 year);

        MySQL运算符:
            1 数值比较:
                > >= < <= = !=

                eg1:
                    查询成绩不及格的学生
                    select * from students where score < 60;
                eg2:
                    删除成绩不及格的学生
                    delete from students where score < 60;

                eg3:
                    把id为3的学生的姓名改为 周芷若
                    update students set name='周芷若' where id=3;

            2 逻辑比较:
                and or

                eg1:
                    查询成绩不及格的男生
                    select * from students where score<60 and gender='M';

                eg2:
                    查询成绩在60-70之间的学生
                    select * from students where score <= 70 and score >= 60;

            3 范围内比较:
                between 值1 and 值2,   in(),   not in()
                
                eg1:
                    查询不及格的学生姓名及成绩:
                    select name, score form students where score between 0 and 59;

                eg2:
                    查询AID1905和AID1903班的学生姓名及成绩
                    select name, score from where class in('AID1905', 'AID1903');

            4 模糊查询:
                where 字段名 like 表达式(%_)  (%表示零和多个字符,_表示单个字符)
                eg1:
                    查询北京的姓赵的学生信息
                    select * from students where address='北京' and name like '赵%';

            5 NULL 判断:
                is NULL, is not NULL
                eg1:
                    查询姓名字段值NULL的学生信息
                    select * from where name is NULL;

        查询:
            order by:
                给查询的结果进行排序(永远放在SQL命令的倒数第二的位置写)
                order by 字段名 ASC/DESC(升序/降序)
                eg1:
                    查询成绩从高到底排序
                    select * from students order by score DESC

            limit:
                限制显示插叙记录的条数(永远放在SQL命令的最后写)
                limit n (显示前n条)
                limit m,n (从第(m+1)条记录开始,显示n条)
                eg1:
                    分页: 每页显示10条,显示第6页的内容
                    limit(6-1)*10, 10 
                    分页公式:
                        (m-1)*n, n (m表示要显示的页数, n表示每页显示数据的条数)
                    


                





"""