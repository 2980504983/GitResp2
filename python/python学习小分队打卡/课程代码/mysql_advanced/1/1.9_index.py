"""
    索引概述:
        对数据库表的一列或多列的值进行排序的一种结构(使用Btree(b+树)实现的)
        
        b树和b+树的区别:
            自行百度,写下来补充(还有一个B*树)
            B树的特点:
                1 全部节点均包含索引(id)+数据
                2 范围查询,从根节点遍历至指定数据
                
            B+树的特点:
                1 非子叶节点只保存索引(树的宽度大于B树,从而降低磁盘IO)
                2 叶子节点保存所有的索引和数据
                3 叶子节点之间相互连接,形成链表结构
                
            详细见 B+树.png 和 B树.png
                
            【范围查询】
        优点:
            加快数据检索速度
            
        缺点:
            占用物理空间(/var/lib/mysql)
            当对表中数据更新时,索引需要动态维护,降低数据维护速度
            
        索引示例:
            1 开启运行时间检测:
                show variables like '%pro%';(查看mysql的一些属性)
                set profiling=1;
                
            2 执行查询语句(无索引)
                select name from students where name='Tom99999';
                
            3 查看执行时间:
                show profiles;
                
            4 在name字段创建索引
                create index name on students(name);
            
            5 再次执行查询语句:
                select name form student where name='Tom99999';
                
"""