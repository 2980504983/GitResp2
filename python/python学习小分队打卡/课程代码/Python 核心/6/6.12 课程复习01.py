"""
    程序的执行过程:
        (源代码) --编译--> (字节码) --解释--> (机器码)
        并不是所有代码都会编译成字节码，只有导入进来的代码才会编译，例如 main.py中的代码就
        不会编译，但是导入进main.py的代码是会编译的，因此 main.py中不应该放大量代码

    pycharm快捷键:


    各种容器:
        列表: 预留空间
        元组: 不预留空间

    各种容器转换:
        字符串转列表：
        list(str类型的变量)

        列表转字符串:
        str02 = "".join(列表)

        列表 += 列表 是累加
        元组 += 元组 是产生一个新的元组(因为元组不可变)

        注: 容器名称(可迭代对象)--加生成器也行


        生成器原理:
            class MyGenerator:
        生成器 = 可迭代对象 + 迭代器

        写了yield就会自动生成这些代码
    def __init__(self, stop_value):
        self.begin = 0
        self.stop_value = stop_value

    def __iter__(self):
        return self

    def __next__(self):
        if self.begin >= self.stop_value:
            raise StopIteration
        temp = self.begin
        self.begin += 1
        return temp
        pass

def my_range(stop_value):  # 生成器版本
    number = 0
    while number < stop_value:
        yield number
        number += 1

        面试题:
        简述生成器与迭代器:
            生成器的本质就是 迭代器 + 可迭代对象
            可迭代对象 就是为了可以 迭代(for)，而迭代的本质就是不断掉用 迭代器里的next方法
            生成器最重要的特点，就是调用一次next，计算一次结果，返回一次结果
            这个过程称之为惰性操作/延迟操作，在海量数据下，可以大量节省内存
            惰性操作 -》 立即操作 list(生成器)


        解释器会将函数定义到方法区(只存储一份)，连同默认参数一起创建，所以不指定参数时，使用的
        就是同一份列表对象(默认参数)
        总结: 默认参数，不要使用可变对象
        def fun01(x, list_target = []):
            for i in range(x):
                list_target.append(i)
            print(list_target)
        fun(3)  # [0,1,2]
        fun(3)  # [0,1,2,0,1,2]

"""


