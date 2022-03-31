# pymysql 读操作数据库基本流程

import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='qyzw',
                     password='223309',
                     database='stu',
                     charset='utf8')

# 获取游标(操作数据库，执行sql语句)
cur = db.cursor()

# 获取数据库数据
sql = 'select * ...'

cur.execute(sql)  # 执行正确后cur调用函数获取结果，并不是直接返回，但是承载了数据，后面每查询一个，
                    # 就会向后迭代一个

# 获取一个查询结果
one_row = cur.fetchone()
print(one_row)  # 元组

# 获取多个查询结果
many_row = cur.fetchmany(2)
print(many_row)  # 元组套元组

# 获取所有查询结果
all_row = cur.fetchall()
print(all_row)


# 关闭数据库
cur.close()
db.close()
