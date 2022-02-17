#---Recursive function------
#remark: The recursive function only calls itself.

#Find the factorial
#Circular way to achieve
# def factorial_function(n):
#     result=1 #storege
#     for item in range (1,n+1):
#         result*=item
#         pass
#     return result
# print(f"Factorial of five is {factorial_function(3)}")

#Doing it by recursive function
# def recursive_function(n):
#     if n==1:  #exit
#         return 1
#     else:
#         return n*recursive_function(n-1)
#     pass
# print("Factorial of five is %r"%recursive_function(3))

#Recursive case
# import os
# def findfile(file_path):
#     listRs=os.listdir(file_path) #find all folders under the current path
#     for fileItem in listRs:
#         full_path=os.path.join(file_path,fileItem) # get the full file path
#         if os.path.isdir(full_path): # determine whether it is a folder
#             findfile(full_path) # recursing it again,if it's a folder.
#         else:
#             print(fileItem)
#             pass
#         pass
#     else:
#         return
#     pass
# findfile('E://夏天的谎言')


# #------------Built_in function---------
#
# #first:arithmetic function
#
# #1:abs() #absolute value
# a=-24
# print(abs(a))
#
# #2:round() #approximation
# value=1.2356665
# print(round(value,3))
#
# #3:pow() #exponentiation
# print(pow(2,3))
#
# #4:divmod()

#type convertion function
#str() bool() ord()......

#squence operation function
#prompt:str int list are squence types

#1:all() #bool type ,opposite to below
# lista=[]
# listb=[1,2,'']
# listc=['',0,False]
# print(all(listb))

#2:any() #bool type ,one ture all ture
# lista=[]
# listb=[1,2,'']
# listc=['',0,False]
# print(any(listb))

#3:sorted() # sort the list
# listsort=[1,5,8,3,4]
# print(sorted(listsort))

#4:reversed() # sort all types
#prompt:generate new objects and it generally assigned to a new object
# tuplereverse=(1,5,8,3,4)
# new_object=list(reversed(tuplereverse))
# print(new_object)

#5:range() # generate a int list
#......

#6:zip() #packing and combination
# a=(1,2,3,'yyy')
# b=[4,5,'wiji']
# c={'yyy':'sjdkjak'}#only package key
# d=list(zip(a,b,c))
# print(d)

# zip case
# def printbookinfo():
#     books=[]
#     id=input('please enter the number:separate each item with a space')
#     bookname=input('please enter the bookmane: ')
#     bookpos=input('please enter the position:')
#     idlist=id.split(' ')
#     namelist=bookname.split(" ")
#     poslist= bookpos.split(' ')
#     bookinfo=zip(idlist,namelist,poslist) #packing
#     for bookitem in bookinfo: #traverse the stored book information
#         dictinfo={'number':bookitem[0],'bookname':bookitem[1],'bookpos':bookitem[2]}
#         books.append(dictinfo) #put the dict object in the list
#
#
#     for item in books :
#             print(item)
#             pass
# printbookinfo()

#7:enumerate(sequence,start[]) #print out the index value corresponding to the element
#remarks:enumerate generally used in for loops
# listorder=['a','b','c']
# for item in enumerate(listorder):
#     print(item)
#     pass
#and you can also set a variable to receive these indexes
# for index,item1 in enumerate(listorder):
#     print(index,item1)
#     pass
#then try to traverse dict
# dict1={}
# dict1['name']='lina'
# dict1['hobby']='singing'
# for item in enumerate(dict1):
#      print(item[0]) #0 means to get the key of the element
#      print(item[1]) #1 means to get the key of the element
#      pass
#remarks:enumerate(variable,[]) the square brackets can only be one or two .
# they represent the index and value respectively.
# in the dict 2 repersent keys.


#------------------set---------------
# remarks: is an unordered and non-repeating collection of elements

# # 1: add() add to
# set1=set() # create an empty collection
# set2={1,"2",True,1}
# print(set2) # Do not print repeated elements at this time
# set1.add(1) # only one element can be added
#
# # 2:clear()
# set3={1,2,3,4,5,6}
# print(set3)
# print(set3.clear()) # return none
#
# # 3:difference() #subtraction
# set4={1,2,3,4,5,6}
# set5={1,2,3,'jskjdk'}
# print(set4.difference(set5)) # Get a collection of elements that are included in set4 but don't be included in set5
#
# # 4:intersection()
# set6={1,2}
# set7={1,3,4}
# print(set6.intersection(set7)) #intersection method one
# print(set6 & set7) #intercetion method two
#
# # 5:union()
# set8=set()
# set9={'yayaya',1,True}
# print(set8.union(set9)) #boolean values are not displayed
#
# # 6:pop() #take out the data  in the collection and delete
# set10={1,2,3,4,5,6}
# set10.pop()
# print(set10)
#
# # 7:discard() #Designated delete
# set11={1,2,3}
# set11.discard(1)
# print(set11)
#
# # 8:update() #merge deduplication
# set12={1,2,3,4}
# set13={2,4,6,8}
# set14=set12.update(set13)
# print(set14)

# ------------------------homework----------------------

# 1:find sum of three consecution natural numbers groups:
# find the three sum from 1 to 10,20 to 30 and 35 to 45 respectively.
# result=0
# for item in range(10):
#     result+=item
#     pass
# print(result)


# def sum_of_consecution_natural_number():
#     result1=0
#     object1=int(input('please enter start number:'))
#     object2=int(input("please enter end number:"))
#     for item in range(object1,object2+1):
#         result1+=item
#         pass
#     print(result1)
# sum_of_consecution_natural_number()


# def sumrange(a,b):
#     return sum(range(a,b+1))
# print(sumrange(1,10))
# print(sumrange(10,20))







# 2:One hundred monks have one hundred steamed bread ,
# one big monk has three ,three little monks have one
# Ask the big monk and the little monk how many?


##dont'cotrol monk of numbels
# a=0
# while a<=100//3:
#     b=0
#     while b<=300:
#         if a*3+b/3==100:
#             print('there are %r big monks,there are %r little monks'%(a,b))
#             pass
#         b+=1
#         pass
#     a+=1
#     pass

# def sumob():
#     for a in range(1,100):
#         if a*3+(100-a)*(1/3)==100:
#             return (a,100-a)
#         pass
#     pass
# print(sumob())
# # or
# tuple1=sumob()
# print('there are {} big monks,{} little monks'.format(tuple1[0],tuple1[1]))


#3:Create a list ,the list includes a digital of appears only once,find the digital
# listA=[1,1,2,2,3,3,4,3,'hhh','hhh']
# for item in listA:
#     if listA.count(item)==1:
#         print(item)

#use set
# listA=[1,1,2,2,3,3,4,3,'hhh','hhh']
# set1=set(listA)
# for item in set1:
#     listA.remove(item)
#     pass
# for item1 in set1:
#     if item1 not in listA:
#         print(item1)

#----------oop [object oriented programming]------------
#......
# class people:
#     def eat(self):
#         """
#
#         :return:
#         """
#         print('like oringe')
#         pass
# L_er=people()
# L_er.eat()
# L_er.name='YunXing'#append instance attributes
# L_er.age=18 #append
# print(L_er.name,L_er.age)#input
#
# WanQing=people()
# WanQing.eat()
# WanQing.name='WanQing'#append instance attributes
# WanQing.age=18 #append
# print(L_er.name,L_er.age)#input
#
# class general():
#     def attributes(self):
#         name='laogou'
#         pro='doctor'
#         print('My name is {} ,Im a {}'.format(name,pro))
#         pass
#     pass
# i=general()
# i.attributes()
# #-----------------------
# class general():
#     def attributes(self,name,pro):
#         self.name=name
#         self.pro=pro
#         print('My name is {} ,Im a {}'.format(self.name,self.pro))
#         pass
#     pass
# i=general()
# i.attributes('laogou','doctor')
# y=general()
# y.attributes('hualing','driver')
#
# #--------------------------
# class general():
#     def __init__(self,name,pro):
#         self.name=name
#         self.pro=pro
#         print('My name is {} ,Im a {}'.format(self.name,self.pro))
#         pass
#     pass
# yi_yung_xi=general('yunxing','prime minister')
#
# du_wan_qing=general('wanqing',"empress dowager")
#
# su_yi_ran=general('yiran','imprial physician')


#----------- Case of the decisive battle on the top of the Forbidden City--------------

# The first step is to deine a role class
# import time # import time package
# class role:
#     def __init__(self,name,hp):
#         self.name=name
#         self.hp=hp
#         """create initialization function
#         name and hp
#         """
#         pass
#     def kiss(self,enemy):
#         enemy.hp-=10 #enemy loses 10 drops of blood
#         message='{} kissed {}'.format(self.name,enemy.name)
#         print(message)
#     def deep_kiss(self,enemy):
#         enemy.hp-=15
#         message=f'{self.name} deep kissed {enemy.name} '
#         print(message)
#         pass
#     def drug_abuse(self):
#         self.hp+=10
#         message='%s takes medicine and gets 10 drops of blood'%(self.name)
#         print(message)
#         pass
#     def __str__(self):
#         return "{} has {} drops of blood left".format(self.name,self.hp)
# # The secong step is to create two instantiate objects
# Ling_Er=role('玲儿',100)
# Yu_Xiu=role('钰袖',200)
# # Ling_Er.kiss(Yu_Xiu)
# # print(Yu_Xiu)
# # print(Ling_Er)
# while True:
#     if Ling_Er.hp<=0 or Yu_Xiu.hp<=0:
#         print('Yu Xiu: My LingEr is so cute')
#         break
#     Ling_Er.kiss(Yu_Xiu)
#     print(Ling_Er)
#     print(Yu_Xiu)
#     print('------------------------------------')
#     Yu_Xiu.kiss(Ling_Er)
#     print(Ling_Er)
#     print(Yu_Xiu)
#     print('------------------------------------')
#     Yu_Xiu.deep_kiss(Ling_Er)
#     print(Ling_Er)
#     print(Yu_Xiu)
#     print('------------------------------------')
#     Ling_Er.drug_abuse()
#     print(Ling_Er)
#     print(Yu_Xiu)
#     print('------------------------------------')
#     time.sleep(1) # sleep for one second
#
# print('Yu Xiu: hhh...')
#
#--------- homework-----------------

#--Redo Case of decisive battle on the top of the forbidden city .
#-Create a role class
# class role:
#     def __init__(self,name,hp):
#         self.nickname=name
#         self.blood_volume=hp
#         """
#         initialization function
#         """
#         pass
#     def normal_attack(self,offensive_object):
#         offensive_object.blood_volume-=2
#         print(f'{offensive_object.nickname} is attacked and loses 2 drops of blood')
#         pass
#     def acting_cute(self,offensive_object):
#         offensive_object.blood_volume=5
#         print('{} used the cute-selling skill on {} \n {} loses {} drops of blood'
#         .format(self.nickname,offensive_object.nickname,offensive_object.nickname,5))
#         pass
#     def coquettish(other,offensive_object):
#         offensive_object.blood_volume-=10
#         print('%s used coquettish skill on %s and %s left %d drops of blood'%
#         (other.nickname,offensive_object.nickname,offensive_object.nickname,offensive_object.blood_volume))
#     pass
# #-creating instance object
# YunXi=role('YiYunXi',100)
# YiRan=role('SuYiRan',100)
# WanQing=role('DuWanQing',100)
#
# YunXi.acting_cute(YiRan)
# print('......................')
# YunXi.acting_cute(WanQing)
# print('......................')
# YiRan.coquettish(YunXi)
# print('......................')
# WanQing.coquettish(YunXi)


#-----------inherit----------------

#--single inheritance--
# class animal:
#     def __init__(self):
#         print('I can eat')
#         pass
#     def CanRun(self):
#         print('I can run')
#         pass
#     pass
# class duck(animal):
#     def quack(self):
#         print('quack')
# duck1=duck() #create a instance object
# duck1.quack()
# duck1.CanRun()

#--multiple inheritance--
# class animal:
#     def need(self):
#         return ('Need to eat')
#     pass
# class bird:
#     def fly(self):
#         print(('can fly'))
#     pass
# class crow(animal,bird):
#     def black(self):
#         print('Im black')
#         pass
#     pass
# crow=crow()
# print(crow.need())
# print(crow.fly()) # if print repeatedly ,it will display none
# crow.black()


# ----Method of the same name---
# class MotherCatOne:
#     def  agile(self):
#         return ('Can fly over the wall')
#     pass
# class MotherCatTwo:
#     def agile(self):
#         return ('Good at swimming')
#     pass
# class CatDaughter(MotherCatTwo,MotherCatOne):
#     def agile(self):
#         return ('run fast')
#     pass
# catdaughter=CatDaughter()
# print(catdaughter.agile()) #Behavior rewritten


# ---class attribute and instance attritube---
# class apple:
#     apple="RedApple"    # class attribute
#     def __init__(self,size):   # instance attribute
#         self.size=size
#         pass
#     pass
# apple=apple('VeriBig')
# print(apple.apple)  # access class attribute by instance object

# remarks: 1 class attribute can't be modified by instance object
#          2 class attribute can be modified by class object(class name)


# ---class method and static methods---


#--class method--

# class lily:
#     name='1' # class attribute
#     def __init__(self): # instance attribute
#         self.name='2'
#     @classmethod # class method
#     def bloom(cls):
#         print('See all ugliness in the world,see love and heaven in lilies')
#     @classmethod
#     def changing(cls): # creating a method changing class attribute
#         cls.name='3'
#         pass
#     pass
# lily.bloom() # Can transfer directly and don't need to create instance object
# lily.changing() # transfer class method to change class attribute
# print(lily.name)
# YunXi=lily()
# print(YunXi.name)

#--static method--

# class lily:
#     @staticmethod # It's independent and it can't use class attribute and instance attribute
#     def MostBeautiful():
#         print('lily is the flower most beautifil in the universe')
#         pass
#     pass
# lily.MostBeautiful()

# --case--
# return the current time
#---method one__________________
# import time
# class TimeTest:
#     def __init__(self,hour,min,second):
#         self.hour=hour
#         self.hour=min
#         self.hour=second
#     @staticmethod
#     def ShowTime():
#         return time.strftime("%H:%M:%S",time.localtime())
#     pass
# pass
# p=TimeTest(1,2,3)
# print(p.ShowTime())

# method two______________
# class TimeTest:
#     @staticmethod
#     def ShowTime():
#         return time.strftime("%H:%M:%S",time.localtime())
#     pass
# pass
# print(TimeTest.ShowTime())












