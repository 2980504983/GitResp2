
#------------------函数的定义与调用

# def 函数名(name,height):  #函数的定义
#     print('{}身高是{}'.format(name,height))  #该函数的具体内容
#     pass
# 函数名('风铃儿',180)   #函数的调用


#----------------------------参数的分类与使用


#--------- 1 必选参数  # 调用时必须赋值

# def sum(a,b):  #  定义一个求和函数
#     print(a+b)
#     pass
# sum(10,1.3)


#-------- 2 默认参数（缺省参数） # 顾名思义有默认值的参数
# 形参中如果前面一个参数已经被赋值，那么在调用中后面的参数都不能在被赋值了。
# （形参中如果要添加默认值，最好保证被赋值的那个形参后面全部的形参都被赋了值）

# def sum1(a=1,b=2):
#     print(a+b)
#     pass
# sum1()


#------- 3 可变参数（不定长参数） # 一般用于参数不确定时，表现形式为元组

# def 累加和(*hhh):
#     result=0
#     for it in hhh:
#         result+=it
#         pass
#     print('结果为{}'.format(result))
#     pass
# # input('请输入想要计算累加和的最大数字:{}'.format())
# 累加和()


#------- 4 关键字参数  # 用**定义，表现形式为字典

# def hhh1(**ya):
#     print(ya)
#     pass
# # 两种调用方法
# dictA={'name':'hhh'}
# hhh1(**dictA)
# #     或
# hhh1(name='hhh')


#---------------  参数的混合使用 # 可变参数 要位于关键字参数之前

# def complexFunc(*args,**kwargs):
#     print(args)
#     print(kwargs)
#     pass
# complexFunc(1,2,3)
# print()
# complexFunc(1 ,name='hhh')
# print()
# complexFunc(name='hhhh')


#----------------  函数返回值

# def sum3(a,b):
#     c=a+b
#     return c  #  返回函数值
# print(sum3(1,2))   #  函数值被返回到调用的地方，并执行打印操作

# hh=sum3(3,4)  #  将返回值赋给其他的变量
# print(hh)

#---------- 计算累加和

# def calcomputer(num):
#     result=0
#     i=1
#     while i<=num:
#         result+=i
#         i+=1
#         pass
#     return result
# hhh=calcomputer(3)
# print(hhh)





#------------ 使返回值为元组

# def returntuple():
#     return 1,2,3
# a=returntuple()
# print(type(a))


# #---------- 使返回值为字典

# def returntuple():
#     return {'name':'好'}
# a=returntuple()
# print(type(a))


# ------------------函数的嵌套使用  # 运行流程

# def fun1():
#     print('2')
#     print('3')
#     print('4')
#
# def fun2():
#     print('1')
#     fun1()
#     print('5')
#
# fun2()


#---------------------------————————————————————————课后作业-----------------------


#-----------------1  写函数，接收n个数字，求这些参数数字的和。

# def sum(*args):
#     result = 0
#     for i in args:
#         result+=i
#         pass
#     return result
# result=sum(1,2,3)
# print(result)


#----------------2  写函数，找出传入列表或元组奇数位对应的元素，并返回一个新的列表。

# def 奇数位查找(*args):
#     a=(args[::2])
#     listA=[a]
#     print(listA)
#     pass
# 奇数位查找('好',1,'ya',True,)


#---------------3  写函数，检查传入字典的每一个value的长度，如果大于2，那么仅保留前两个长度的内容，并将新
#------------------内容返回给调用者。注：字典中value只能是字符串或列表。

# def hhh(kwargs):
#     dictA={}
#     for key,value in kwargs.items():
#         i=len(value)
#         if i>2:
#             dictA[key]=value[:2]
#             pass
#         else:
#             dictA[key]=value
#         pass
#     return dictA
#     pass
#
# dictB={'name':'风铃儿','年龄':'18','兴趣爱好':['吃饭','睡觉','打豆豆']}
# print(hhh(dictB))


#-----------------------匿名函数---------------

# 不能用常规方法，因为优先级
# test=(lambda a,b:a+b)(11,22)
# print(test)

#---------------------三元运算 代替 传统双分支-------
#  比较两数大小

# 传统双分支----------------------
# a=(int(input('请输入数字1:')))
# b=(int(input('请输入数字2:')))
# if a>b:
#     print(a)
#     pass
# else :
#     print(b)

#      三元运算-------------
# greater=(lambda a,b : a if a>b else b )(3,4)
# print(greater)


#  还可以-------------------
# a=(int(input('请输入数字1:')))
# b=(int(input('请输入数字2:')))
#
# print(a) if a>b else print(b)




