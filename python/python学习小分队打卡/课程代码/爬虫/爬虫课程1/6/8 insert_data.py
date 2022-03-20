"""
    Mongodb的增删改查:
        1 插入数据:
            db.集合名称.insert(document)
            db.stu.insert({"name":"g"})
            插入文档时,如果不指定_id参数,系统会自动分配一个唯一的objectid

        2 保存:
            db.集合名称.save(document)
            db.stu.save({_id:'xxxxxx','name':'wang', gender:2})
            如果_id已经存在,会修改该id对应的数据,如果不存在则添加,这种操作叫做upsert操作

        3 查询:
            db.集合名称.find()
            db.集合名称.findOne()



"""