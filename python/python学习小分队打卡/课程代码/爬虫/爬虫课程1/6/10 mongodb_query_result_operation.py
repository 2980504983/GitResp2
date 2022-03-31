"""
    自定义查询：
        mongo shell 是一个js的执行环境,使用$where 写一个函数,返回满足条件的数据
        示例:
            db.stu.find({$where:function(){return this age>30}})

    skip和limit
        find().limit(num) 限制数据数量为num
        find().skip.limit(num) 跳过num条数据
        注: 两者可以直接组合使用,并且skip的优先级更高,find().limit(n).skip(n),仍然会先执行skip

    投影:
        就是筛选你想看到的数据
        db.stu.find({},{条件})

    排序:
        db.集合名称.find().sort({字段：1,...})
        示例:
            按照性别降序,在根据年龄升序
            db.stu.find({gender:-1, age：1}) (复合排序)

    统计个数:
        .count() 里面还可以加条件

    去重:
        对集合进行去重
        db.集合名.distinct()

        对查询结果进行去重
        db.集合名.distinct('hometown',{age:18})

"""