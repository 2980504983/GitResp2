#--------字符串常用函数————————------

# #---1----首字母变大写
# name="feng ling er"
# print(name.capitalize())

# #---2----判断是字母还是数字
# name="feng ling er"
# print(name.isalnum())#当是字母时输出false

# #---3----判断是否是小写
# name="feng ling er"
# print(name.islower())#全是才小写输出ture

# #---4----大写变小写，小写变大写
# name="feng ling er"
# print(name.swapcase())

# #---5----把每个单词的首字母变大写
# name="feng ling er"
# print(name.title())

# #---6----是否，结束/开始
# name="feng ling er"
# print(name.startswith("f"))#判断是否是以某个字符开头
# print(name.endswith("r"))#判断是否是以某个字符结尾

# #---7----判断是否是字母
# name="feng ling er"
# print(name.isalpha())#判断是否是字母是输出ture

# #---8----循环取出所有值用xx替代
# name="feng ling er"
# print(" ".join(name))#起隔开作用

# #---9----移除左，右，两侧空白
# name="      feng ling er       "
# print(name)
# print(name.lstrip())#左,右rstrip,两边strip


# #---11----检测x是否在字符中
# name="feng ling er"
# print(name.find("n"))#有几个就显示几

# #---12----判断是否是数字
# name="feng ling e1"
# print(name.isdigit())#有一个不是就是false

# #---13----大小写转换
# name="feng ling er"
# print(name.upper())#转换大写    lower 转换小写

# #---14----切割字符串
# name="feng ling er"
# print(name.split())

#---15----统计出现次数
# name="feng ling er"
# print(name.count('n',0,7))#数字是下标，从零开始


#------------------------------索引和下标-------------------------------

#-------通过索引获取某个数据中的一段-----------
# test="严清越 爱 杨紫婉啊"
# print('获取第一个字符:%s'%(test[0]))

#--------切片操作-------------
# text='重生之白眼狼，严清越爱杨紫婉'
# myslice=slice(0,6)   #定义slice的值
# print(text[myslice])   #将slice带入变量中
# print(text[7:14])    #直接切片
# print(text[::-1])    #倒叙操作

#-------------------------列表  list------------------------------
#列表是一种重要的数据结构，是一种有序的数据集合。

#-------list的常用方法-------
# listA=['.',1,True,1.2,223,'hhh']

# print(len(listA))  # len反应对象的长度

# print(listA*2)   # 复制操作

# listA.append(4.1515) #  .append函数只能追加一个对象
# print(listA)

# listA.insert(0,'替换值') #  .insert插入操作
# print(listA)

# listB=list(range(0,21))  # list转换对象格式
# print(listB)
# i=range(0,21)
# for l in i:
#     print((l),end='  ')

# tupleC=(0.1,545,'2333')  #  添加内容
# listA.extend(tupleC)
# print(listA)

# listA[0]=2  #  直接修改内容
# print(listA)

# del listA[0:3]   #   直接删除
# print(listA)

# listA.pop(0)
# print(listA)

# listA.remove('hhh')  #  移除指定元素
# print(listA)

# print(listA.index('hhh'))  #  查找具体数值的位置

#----------------tuple  元组-------------------
#------是一种不可变的序列，在创建后不能做任何修改---------

# tupleA=('a','b','c','d')
# print(tupleA[0:1])
# print(tupleA[-2:-1])  # 从右往左数，从-1开始。
# print(tupleA[0])  # 不同的格式输出效果也不一样

#---------------dict  字典-----------------------
#------不是序列，无下标，是键值对组成的集合---------

dictA={}
dictA['name' ]='宋若依'

# print(dictA)  # 打印键值对

# print(dictA['name'])  #  根据键，获取值

# dictA['name']='宋若依爱李木子'  #  重新赋值，即修改
# print(dictA)  ]

# print(dictA.keys())   #  获取所有键，同理可获所有 值 或 键值对


# for key,value in dictA . items():  #  用 for 遍历取值
#     print('%s=%s'%(key,value))

# dictA.update({'name':'宋若依爱李木子'})  #  添加 或 修改
# print(dictA)

# del dictA['name']  #删除操作
# dictA.pop('name')  #删除操作
# print(dictA)


# print(sorted(dictA.items(),key=lambda d:d[1]))  # 按照 值 排序，值 的类型要一致否者报错

# print(sorted(dictA.items(),key=lambda d:d[0])   # 按照 键 排序。


#---------------------------  共有方法  +  * in ------------------------


#  字符串合并
# a='风铃儿'
# e='爱'
# b='白钰袖'
# c=a+e+b
# print(c)

#  元组合并 +
# a=(1,'hhh')
# b=(2,"kkk")
# print(a+b)

# 复制 *
# a=(123,'464')
# print(a*2)


# 查找 in

# a=(133,'hhhh')
# print(133 in a)
