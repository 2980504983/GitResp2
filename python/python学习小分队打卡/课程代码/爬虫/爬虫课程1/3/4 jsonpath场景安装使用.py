"""
    数据提取-jsonpath模块

        1 jsonpath使用场景:
            多层嵌套的复杂字典直接提取数据
        2 安装:

        3 jsonpath模块提取数据的方法:
            from jsonpath import jsonpath
            ret = jsonpath(a, 'jsonpath语法规则字符串')

        4 jsonpath语法规则:
            详细见jsonpath语法规则.jpg
            最常用语法(其它用的很少，简单看看就好):
                $  根节点(最外层的大括号)
                .  子节点
                ..  内部任意位置，子孙节点

"""
from jsonpath import jsonpath

# 一般的要使用jsonpath，需要一个json格式的数据，但是我们从网上获取的json数据一般都是字符串类型的，
# 因此我们要先通过json模块，用json.loads()接口将字符串类型的json数据转化成json数据
data = {"key1": {"key2": {"key3": {"key4": {"key5": {"key6": 'python'}}}}}}
# 方法(非常不优雅):
print(data['key1']['key2']['key3']['key4']['key5']['key6'])

# 使用jsonpath提取,结果为列表
# 1
# print(jsonpath(data, '$.key1.key2.key3.key4.key5.key6')[0])
# 2 终极方法-优雅
print(jsonpath(data, '$..key6')[0])
