"""
    二进制文件存储进数据库

    文件存储:
        1 存储文件路径:
            好处: 节约数据库空间
        2 将文件以二进制存储在数据库:

"""
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

# 存储图片
# with open('image1.jpg', 'rb') as f:
#     data = f.read()
# try:
#     sql = "update class set image = %s where name= '严清越';"
#     cur.execute(sql, [data])
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)


# 获取图片
sql = "select image from class where name='严清越'"
cur.execute(sql)
data = cur.fetchone()
with open('image1_read.jpg', 'wb') as f:
    f.write(data[0])


# 关闭数据库
cur.close()
db.close()
