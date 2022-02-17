
"""
封装
    数据角度：将多个变量封装到一个自定义类中。
            (符合人的思考方式，可将数据与对数据的操作封装到一起)
            
    功能角度：对外提供必要的功能，隐藏实现的细节
            -- 私有化：将名称命名为以双下划线开头
            
            -- 属性：self.name是什么，没法判断
                    有拦截对象时，self.name不是实例变量了，是属性或者类变量，此时实例变量
                    应该是方法中的self.__name
            
            -- __slots__ 限定类创建的对象只能有固定的实例变量
                优点：防止用户因错写属性名称而引发程序错误（也就是防止写错属性名称重新创建实例
                     变量）
                缺点：丧失了动态语言可以在运行时可以为对象添加变量的灵活性
        
    设计角度：
        分而治之：将大的需求分解为多个类，每个类负责一个职责
        变则疏之：遇到变化点单独封装为一个类
               ----------审查-----------------
        高内聚：一个类有且只有一个发生变化的原因，也就是只有一个变化点
        低耦合：类于类的关系松散
    
"""


class Student:
    # 只允许实例变量有name
    __slots__ = 'name'

    def __init__(self, name):
        self.name = name


s01 = Student('wj')
# 添加了新的实例变量，上面允许的变量中没有age所以会报错
# s01.age = 18


class Student01:
    # __slots__是限制实例变量的，因此应该填__name,而不是name，因为有了拦截对象，name变成了
    # 属性，也就是类变量
    __slots__ = '__name'

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


