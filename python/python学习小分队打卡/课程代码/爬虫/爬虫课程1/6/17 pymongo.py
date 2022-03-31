"""
    安装pymongo:
        pip install pymongo
"""
from pymongo import MongoClient


# 创建数据库连接对象
client = MongoClient('ip', port=34342)

# 选择一个数据库,没有权限认证直接选择你要操作的数据库就好啦
db = client['admin']

db.authenticate('user', 'pwd')

# 选择一个集合
col = client['数据库']['集合']

# 插入
col.insert({'data': 'data'})

