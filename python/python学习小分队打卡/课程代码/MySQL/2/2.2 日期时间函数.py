"""
    时间数据类型:
        时间和日期类型:
            date(年月日), datetime(年月日时分秒), timestamp(时间戳)...
            详细见 时间和日期类型.jpg
        时间格式：
            详细见 时间和日期类型.jpg
            注意: datatime 不给值默认返回null
                 timestamp 不给值默认返回系统当前时间

        日期时间函数(用于填写数据元素):
            now() 返回服务器当前时间
            curdate() 返回当前日期
            curtime() 返回当前时间
            date(date)  返回指定时间的日期
            time (date)  放回指定时间的时间

        修改时间日期例子: update student set 入学时间='2019/5/6' where score=99;

        时间类型数据可以比较大小where子句

        日期时间运算:
            select * from 表名 where 时间 > (time ('03:00:00')-interval 30 minute);
            表示查找表中时间大于两分半的记录

            查找距离现在一个星期之内的时间
            select * from 表名 where 时间 > (now()-interval 7 day);




"""