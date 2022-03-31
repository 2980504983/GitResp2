"""
    mongodb增删改查:
        1 插入数据:
            db.集合名称.insert(document)

        2 保存:
            db.集合名称.save(document)

        3 查询:
            db.集合名称.find()

        4 更新：
            db.集合名称.update(query,{update},{multi:boolean})
            参数:
                query: 查询条件
                update: 更新操作符
                multi: 可选,默认为false,表示只更新找到的第一条数据,值为true表示更新所有满足条件的数据

        5 删除:
            db.集合名.remove(query,{justOne:boolean})
                参数:
                    justOne： 如果设置为true表示只删除一条,默认为false也就是全部删除
"""