"""
    pymysql使用流程
        1 建立数据库连接(db = pymysql.connect(...))
        2 创建游标对象(c = db.cursor())
        3 游标方法 c.execute('insert...')
        4 提交到数据库 db.commit()
        5 关闭游标对象 c.close()
        6 断开数据库连接 db.close()

    常用函数:
        db = pymysql.connect(参数列表)
        host:
        port:
        user:
        password:
        database:
        charset: 编码方式

        db对象的方法:
            db.commit()提交数据库
            db.rollback()回滚
            cur = db.cursor()返回游标对象，用于执行具体sql命令
            db.close()

            cur对象的方法:
                cur.execute(sql命令，[列表])执行sql命令
                cur.close() 关闭游标对象
                cur.fetchone()获取查询结果集的第一条数据
                cur.fetchmany(n)获取n条
                cur.fetchall()获取所有记录
"""

# pymysql 写操作数据库基本流程

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

# 执行sql语句
try:
    sql = "insert into "  # sql语句要保证去掉外面两个引号，能直接在终端执行，也就是内部表示字符串的还要再加引号
    cur.execute(sql)  # 执行语句
    db.commit()  # 提交写操作
except Exception as e:
    db.rollback()  # 退回到commit之前
    print(e)

# 关闭数据库
cur.close()
db.close()
