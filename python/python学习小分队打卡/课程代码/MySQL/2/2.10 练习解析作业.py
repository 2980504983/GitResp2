"""
    练习:
        编写一个程序，模拟注册和登录的过程
            * 创建一个user表 包含用户名和密码字段
                create table user (id int primary key auto_increment, name varchar(32) not null,
                passwd varchar(32) not null);

            * 应用程序中模拟注册和登录功能
            * 注册则输入用户名密码将用户名密码存入数据库，用户名不能重复
            * 登录时比对信息

"""
import pymysql

# 登录模拟
# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='qyzw',
                     password='223309',
                     database='stu',
                     charset='utf8')

# 获取游标(操作数据库，执行sql语句)
cur = db.cursor()

# 注册
def register():
    name = input("用户名:")
    passwd = input("密码：")
    # 判断用户名是否重复
    sql= "select * from user where name='%s'" % name
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        return False
    try:
        sql="insert into user (name, passwd) values(%s,%s);"
        cur.execute(sql, [name,passwd])
        db.commit()
        return True
    except:
        db.rollback()
        return False


# 登录:
def login():
    name = input("请输入用户名:")
    passwd = input("请输入密码:")
    sql = "select * from user where name='%s' and passed='%s'" % (name, passwd)
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        return True


while True:
    print("""========1 注册=========2 登录========""")
    cmd = input("请输入命令:")
    if cmd == '1':
        # 执行注册
        if register():
            print("注册成功")
        else:
            print("注册失败")
    elif cmd == '2':
        # 执行登录
        if login():
            print('登录成功')
        else:
            print('登录失败')
    else:
        print("功能尚未完成")


# 关闭数据库
cur.close()
db.close()
