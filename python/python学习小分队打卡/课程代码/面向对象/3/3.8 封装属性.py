class Enemy:
    def __init__(self, name, atk, hp):
        self.name = name
        self.atk = atk
        self.hp = hp

    @property  # 创建property对象，只负责拦截读取操作(方法名要是被拦截变量的名字)
    def atk(self):
        return self.__atk

    # 只负责拦截写入操作
    @atk.setter  # 上面创建的property对象给了类变量atk，因此有setter属性，
    def atk(self, atk):
        if 10 <= atk <= 50:
            self.__atk = atk
        else:
            raise ValueError('我不要')

    def set_hp(self, hp):
        if 100 <= hp <= 200:
            self.__hp = hp
        else:
            raise ValueError('我不要')
    # 这种写法和上面加property修饰器的写法是一样的只是，写法不同，内存图是一样的，都有类变量
    hp = property(None, set_hp)


"""
    属性 @property
        公开的实例变量，缺少逻辑验证。私有的实例变量与两个公开的方法相结合，可以让变量经理逻辑判断
        但是略显复杂。而属性可以将两个方法的使用方式像操作变量一样方便(也就是说，读取或修改变量，
        会自动被方法拦截，间接调用了方法)
        
        定义：
            @property
            def name(self):
                return self.__name
                
            @name.setter
            def name(self, name):
                self.__name = name
                
        调用：
            对象.属性名 = 数据
            变量 = 对象.属性名
            
        说明：
            --通常两个公开的属性，保护一个私有的变量。
            --@property 负责读取，@属性名.setter负责写入
            --只读，直接不写后面的@属性名.setter就行了
            --只写：因为读的操作包括了创建property对象，因此
                   只写要恢复上一个版本  属性名 = property(None, 写入方法名)
"""