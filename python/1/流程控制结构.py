
#print('a%b')
# '''
# 开始复习
# 23333
# '''
# #开始咯
# print("1.print的使用")
# print('2.变量')
# a,b,c,d=1,2,3,4
# print(a)
# print('3.查看数据类型')
# print(type(a))
# print("4.基本运算符")
# print(a/b)
# print(a**c)
# print(a==b)
# print(a==b and a<b)
# print(a==b or a<b)
# print(not(a==b and a<b))
# print(a==b and a<b or c>b)
# print('赋值运算符')
# a+=c
# print(a)
# print(a==d)
# print(a**c)

# print('5.输入与输出')

# # 我叫风铃儿，今年12岁
# # 来自兰溪镇，我的电话号码是1433223
# Name='风铃儿'
# Age=12
# addr='兰溪镇'
# phone=1433223
# # print('我叫',Name,'今年',Age,"岁"
# #       ,"来自",addr,'我的电话号码是',phone)
# print('我的名字是:%s  今年:%d岁 来自:%s 我的电话号码是:%d'%(Name,Age,addr,phone))

# print('另一种格式化输出:')

# print('我的名字是:{} 今年:{}岁  来自:{} 我的电话号码是:{}'.format(Name,Age,addr,phone) )
# print('input输入:')
# hh=input('请输入你的名字:')
# print('我叫',hh)
# ee=int(input('请输入你的年龄:'))
# print('今年',ee,"岁")

#---       流程控制结构           ---

# 选择流程
#单分支

# a=int(input('请输入你的成绩:'))
# if a>=60:
#     print('不错哦，竟然及格了')


#双分支

# a=int(input('请输入你的成绩:'))
# if a>=60:
#     print('不错哦，竟然及格了')
# else:
#     print('糟糕没得及格，可以回去修理地球了。')


#-----多分支-------

# score=int(input('请输入你的成绩:'))
#
# if score>=60 and score<80:
#     print('不错哦，竟然及格了')
#
# elif score>=80:
#     print("不赖嘛，很强，给你爱吃的大嘴巴子")
#     pass
# else:
#     print("回家种地吧")


#----------- 和电脑猜拳小游戏-----------

# 石头,剪刀,布=(0,1,2)
# computer  人
# import random
# person=int(input('石头：0 剪刀：1 布：2----来吧，出拳吧：'))
# computer=random.randint(0,2)
# print('电脑:%s'%(computer))
# if person==0 and computer==1:
#     print("哇哦，你赢了欸")
# elif person==1 and computer==2:
#     print("哇哦，你赢了欸")
# elif person==2 and computer==0:
#     print("哇哦，你赢了欸")
# elif person==computer:
#     print('打平了呢')
# else:
#     print('嘿嘿，输了吧')

 #--------------if 和 else 的 嵌套使用。-----------

 #--------升班系统，首先至少要十学分，其次，成绩不能低于60--------------

# xuefen=int(input('请输入你的学分:'))
# if xuefen>=10:
#     score=int(input('请输入你的成绩:'))
#     if score>=60:
#         print('恭喜升班，继续努力哈')
#         pass
#     else:
#         print("学分是够了，但分数也太低了吧")
# else:
#       print('学分这么低还想升班？')

#  -----------------while 的使用--——------------

#用 while打出1到100.
# hh=1
# while hh<=100:
#     print(hh)
#     hh+=1
#     pass

# ---------------登录系统--------------
# a=298
# b=2233
# for i in range(3):
#     zh=input('请输入你的账号:')
#     mm=input('请输入你的密码:')
#     if a==zh and b==mm:
#         print('登入成功')
#         break
#         pass
#     pass
# else:
#     print('账号已被锁定')


#  ---------- 加循环  (无限循环)------------

# import random
# while True:
#     person=int(input('石头：0 剪刀：1 布：2----来吧，出拳吧：'))
#     computer=random.randint(0,2)
#     print('电脑:%s'%(computer))
#     if person==0 and computer==1:
#          print("哇哦，你赢了欸")
#     elif person==1 and computer==2:
#          print("哇哦，你赢了欸")
#     elif person==2 and computer==0:
#          print("哇哦，你赢了欸")
#     elif person==computer:
#         print('打平了呢')
#     else:
#         print('嘿嘿，输了吧')

#   --------- 控制次数循环,示例三次---------

# import random
# hh=1
# while hh<=3:
#     person=int(input('石头：0 剪刀：1 布：2----来吧，出拳吧：'))
#     computer=random.randint(0,2)
#     print('电脑:%s'%(computer))
#     if person==0 and computer==1:
#          print("哇哦，你赢了欸")
#     elif person==1 and computer==2:
#          print("哇哦，你赢了欸")
#     elif person==2 and computer==0:
#          print("哇哦，你赢了欸")
#     elif person==computer:
#         print('打平了呢')
#     else:
#         print('嘿嘿，输了吧')
#         pass
#     hh+=1

#-----------打印九九乘法表-------------

# row=1
# while row<=9:
#     col=1
#     while col<=row:
#         print("%d*%d=%d"%(row,col,row*col),end=" ")#起不换行作用
#         col+=1
#         pass
#     print()#  起换行作用
#     row+=1

# row=9  #   倒过来
# while row>=1:
#     col=1
#     while col<=row:
#         print("{}*{}={}".format(col,row,row*col),end=" ")#起不换行作用
#         col+=1
#         pass
#     print()#  起换行作用
#     row-=1

#--------打印直角三角型----------

# row=1
# while row<=20:
#     col=1
#     while col<=row:
#         print("*",end='')
#         col+=1
#         pass
#     print()
#     row+=1

#-------打印等腰三角型------------

row=1
while row<=5:
    j=1
    while j<=9-row:
        print("$",end='')
        j+=1
        k=1
    while k<=2*row-1:
        print("*",end='')
        k+=1
        pass
    print()
    row+=1

#-------for in 和 range 的组合使用,打印1到一百的累积和--------

# hh=0
# for i in range(1,101):  #左包含又右不包含
#     hh+=i   #求累加和
#     #print(i)   #打印数字一到一百
# print("hh={}".format(hh))

#-----打印过程中的全部加值---------

# hh=0
# for i in range(1,101):  #左包含又右不包含
#     hh+=i   #求累加和
#     #print(i)   #打印数字一到一百
#     print("hh={}".format(hh))

#-------for的使用,打印1到200中的全部偶数----------

# for j in range(1,201):
#     if j%2==0:
#         print(j)

#---------区分1到200中所有的奇数和偶数-----------

# for j in range(1,201):
#     if j%2==0:
#         print("%d是偶数"%j)
#         pass
#     else:
#         print("{}是奇数".format(j))

#----------break 和 continue的使用-----------

#-------break--------

# hh=0
# for j in range(1,61):
#     if hh>=100:
#         print("循环执行到%d就退出来了"%j)
#         print(hh)
#         break # 退出循环
#         pass
#     hh+=j

#--------continue-------

# for j in 'i love python':
#     if j=="v":
#         continue
#     print(j, end="")

#---------break--------
#
# for j in 'i love python':
#     if j== 'v':
#         break
#         pass
#     print(j,end="")

#------用for实现九九乘法表------

# for j in range(1,10):
#     for h in range(1,j+1):
#         print("%d*%d=%d"%(j,h,j*h),end='  ')#end=''中''加空格可显示
#         pass
#     print()

#--------账号锁定提示-------
#
# a='298'
# b='2233'
# for i in range(3):
#     zh=input('请输入账号:')
#     mm=input('请输入密码:')
#     if zh==a and mm==b:
#         print('登陆成功')
#         break#成功后就不用在次循环了
# else:
#     print('账号已被锁定')
#     pass
#
# ---------第一节作业，流程控制，if 和 while 的综合使用-------------
#
#作业一：
#猜年龄小游戏，三点要求：
#1  用户最多尝试三次
#2  猜对了，直接退出
#3  每尝试三次，如果还没猜对，询问是否继续，如果回答y就再给三次机会，以此往复，回答n就退出。

# times=0
# while times<=3:
#     age=int(input('猜猜我多少岁:'))
#     if age==18:
#         print('哇，猜对了欸')
#         break
#         pass
#     elif age>=18:
#         print('我没那么老吧.')
#         pass
#     else:
#         print('我可没那么小，我超大的')
#         pass
#     times+=1
#     if times==3:
#        a=input('呀，三次都没猜出来呢，还要再猜嘛，y/n:')
#        if a== "y" or a=="Y":
#            print("游戏继续咯")
#            times=0
#            pass
#        elif a== "n" or a=="N":
#            print("游戏结束了啦")
#            times=5
#        else:
#            print("拜托，你在搞什么啦")
#            a = input('赶紧的，玩还是不玩，y/n:')














