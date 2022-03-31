"""
    删除外键:
        alter table 表名 drop foreign key 外键名;
    查看外键名:
        show create table 表名;
        
    级联动作:
        cascade:
            数据级联删除,更新(参考字段)
            
        restrict(默认):
            从表相关联记录,不允许主表操作
            
        set null:
            主表删除,更新,从表相关联字段值为NULL
            
        注: 写外键要清楚的知道该外键的级联动作是那些
"""