"""
    将单词表存入数据库:
        1 创建数据库:
            create database dict charset=utf8;
        2 创建表:
            use dict
            create table words(id int primary key auto_increment, word char(32), mean text);
        3 将单词存入words单词表

"""
import pymysql
import re

# 打开单词表文件
f = open("dict.txt")  # 打开文件

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='qyzw',
                     password='223309',
                     database='dict',
                     charset='utf8')

# 获取游标(操作数据库，执行sql语句)
cur = db.cursor()

# 前面word，mean是字段，后面两个%s是等待传入的参数
sql = "insert into words (word,mean) values (%s, %s)"

for line in f:
    tup = re.findall(r"(\S+)\s+(.*)", line)[0]
    try:
        cur.execute(sql, tup)
        db.commit()
    except:
        db.rollback()

# 关闭数据库
cur.close()
db.close()


