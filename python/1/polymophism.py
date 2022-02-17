#-----polymorphism-----
# case:
# class Animal:
#     """
#     father (Base class)
#     """
#     def say_who(self):
#         print('I\'m an animal')
#         pass
#     pass
# class Duck(Animal):
#     """
#     son (Derived class)
#     """
#     def say_who(self):
#         print("I'm a beautiful duck") # the method of rewrite Base class reflects polymorphism
#         pass
#     pass
# duck1=Duck()
# duck1.say_who()

# Advantages of polymorphism
# def commonInvoke(obj): # set common ground
#     """
#     Transfer methods uniformly
#     :param obj:
#     :return:
#     """
#     obj.say_who()
#     pass
# listobj=[Duck(),] # you can add more methods behind the Duck
# for item in listobj:
#     commonInvoke(item)

#__________ privatization attribute__________

# class Animal:
#     __name='animal'
#     quantity="a lot"
#     def __init__(self):
#         self.name='animal one'
#         self.__features='can run fast'
#     def Transfer(self):
#         print(self.__features)
#         print(Animal.__name)
#         pass
#     pass
# duck=Animal()
# # print(Animal.name) # Unable to transfer private attribute out of class directly
# print(Animal.quantity) # Transfer class attribute
# print(duck.quantity) # Transfer class attribute by instance object
# print(duck.name) # Transfer instance attribute
# duck.Transfer() # Transfer private attributes that belong class and instance object by transfer method created

#___________privatization method______________

# class Vehicle:
#     def __Lamborghini(self): # create a instance method
#         return "Lamborghini runs fast"
#
#     def Benz(self):
#         return "Benz is cheaper than Lamborghini"
#
#     @classmethod
#     def Ferrari(cls): # create a class method
#         print('ferrari is expensive')
#         pass
#
#     @classmethod
#     def __RollsRoyce(cls):
#         print('RollsRoyce is expensive too')
#         pass
#
#     def Transfer(self):
#         print(self.__Lamborghini())
#         print(self.__RollsRoyce())
#         pass
#     pass
# car=Vehicle()
# Vehicle.Ferrari()
# print(car.Benz())
# car.Transfer()

#--------------property attribute--------------

# class Animal(object):
#     __name='animal'
#     quantity="a lot"
#     def __init__(self):
#         self.name='animal one'
#         self.__features='can run fast'
#     # def Transfer(self):
#     #     print(self._features)
#     #     print(Animal._name)
#     def get__name(self):
#         return Animal.__name
#         pass
#     def set__name(self,Name):
#         Animal.__name=Name
#     Name=property(get__name,set__name)
#     pass
# animal=Animal()
# print(animal.Name)
# animal.Name=123154
# print(animal.Name)

#----------------method two--------------
# class Animal(object):
#     def __init__(self):
#         self.__name='can run fast'
#     @property
#     def name(self):
#         return self.__name
#         pass
#     @name.setter
#     def name(self,Name):
#         self.__name=Name
#         pass
#     pass
# animal=Animal()
# print(animal.name)
# animal.name='1.1'
# print(animal.name)


# ---------------__new__-----------------
# class Animal:
#     def __init__(self):
#         self.color='red'
#      # it's the default sructure of __new__ in the python , if don't write repeatly
#     def __new__(cls, *args, **kwargs):
#         return super().__new__(cls, *args, **kwargs)
#         pass
#     pass
# duck=Animal()

#--------- singleton mode-----------

# class DateBaseclass(object):
#     def __new__(cls, *args, **kwargs):
#         # cls.instance =cls.__new__(cls)  # Can't use method of __new__ itself
#         # It causes deep recursion easily and should use method of father's __new__
#         if not hasattr(cls,'_instance'):
#             cls._instance=super().__new__(cls, *args, **kwargs) #Use method of father's __new__
#         return cls._instance
#     pass
#
# db1=DateBaseclass()
# print(id(db1))
# db2=DateBaseclass()
# print(id(db2))
# db3=DateBaseclass()
# print(id(db3))
# # they are the same object


#------- Error and ecception handing ------------


#----- NameError
# try:
#     print(a) # capture logic code
#     pass
# except NameError as message: # It will be carried out when code is incorrect
#     print(message)
#
# print('I can still be carried out')

#----- IndexError
# try:
#     li=[1,2,3]
#     print(li[10]) # Visit list by subscriot
#     pass
# except IndexError as message:
#     print(message)

#----- ZeroDivisionError ----------
# try:
#     # print(a)
#     #li=[1,2,3]
#     #print(li[10])
#     a=10/0
#     print(a)
#     pass
# except NameError as message:
#     print(message)
#     pass
# except IndexError as message:
#     print(message)
#     pass
# except ZeroDivisionError as message:
#     print(message)

#-------------'Exception' that Omnipotent but not completely omnipotent error type ----------

# try:
#     print(b)
#     pass
# except Exception as message:
#     print(message)

#------- try_except_else---------
# try:
#     print('a')
#     pass
# except Exception as message:
#     print(message)
#     pass
# else:
#     print('true')


#-------- try_except_finally-----------
# try:
#     aksjd
#     pass
# except Exception as message:
#     print(message)
#     pass
# finally:
#     print('I will be carried out anyway')

#------ Unified catch exception -----------
# def A(a):
#     return 10/int(a)
# def B(a):
#     return  A(a)*2
# def main(): # function exception
#     try:
#         B('0')
#         pass
#     except Exception as message1:
#         return message1
#         pass
#     pass
# print(main())


#----------- Custom exception ----------

# class TooLongMyExcept(Exception):
#     def __init__(self,long):
#         self.len=long
#         pass
#     def __str__(self):
#         return 'The length of your name is:' ' ' +str(self.len)+' ' 'exceeded'
#     pass
# def NameTest():
#     try:
#         name=input('please enter the name:')
#         if len(name)>4:
#             raise TooLongMyExcept(len(name))
#         else:
#             print(name)
#             pass
#         pass
#     except TooLongMyExcept as message:
#         print(message)
#     pass
# NameTest()

#--------- Dynamically bind properties and methods ------------

#------Add attribbutes dynamically----------
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return 'I\'m %r'% (self.name)
#     pass
# Duck=Animal('duck')
# Duck.feature='Webbed feed' # Add instance attributes dynamically by instance object
# print(Duck)
# print(Duck.feature)
# Animal.habby='eat' # Add class attributes dynamically by class name
# print(Duck.habby)


#----------------------Add methods dynamically-----------

#---------Add method of instance dynamically

# import types
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return 'I\'m %r'% (self.name)
#     pass
# def method(self):
#     print('I\'m a {}'.format(self.name))
#     pass
# Cat=Animal('cat')
# Cat.printInfo=types.MethodType(method,Cat) # Add method of instance dynamically
# Cat.printInfo()

#------- Add class and static method dynamically--------

# @classmethod
# def eat(cls): # must add cls
#     print('I like eat')
#     pass
# @staticmethod
# def run():
#     print('I can run')
#     pass
# class Animal:
#     pass
# Animal.eat=eat
# Animal.eat()
# Animal.run=run
# Animal.run()

# ----------method __slots__------------------  :
# class student(object):
#     __slots__ = ('name','pro','age') # limit added attributes
#     def __str__(self):
#         return ('{},,,,{}'.format(self.name,self.pro))
#     pass
# xw=student()
# xw.name='XiaoWang'
# xw.pro='student'
#print(xw.__dict__) # attribute dict and need to log off slots
# print(xw)

# When the __slots__ in subclass are not born,
# the subclass does not inherit the __slots__ of the parent class

# class Student1(student):
#     pass
# xh=Student1()
# xh.name='XiaoHua'
# xh.pro='student'
# xh.hair_color='orange' # the subclass don't inherit __slots__ of father class
# print(xh)




#------------------homework one----------------

# class Person():
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#     def __str__(self):
#         return '{} is {}'.format(self.__name,self.__age)
#     def getName(self):
#         return self.__name
#     def getAge(self):
#         return self.__age
#     def set(self,name):
#         self.__name=name
#     def setAge(self,age):
#         if self.__age>=0 and self.__age<=120:
#             self.__age=age
#             pass
#         else:
#             print('please enter the correct age')
#         pass
#     pass
# pass
# xh=Person('XiaoHua',18)
# print(xh.getName())


#-------------homework two---------------
# class DateBaseclass(object):
#     def __new__(cls, *args, **kwargs):
#         # cls.instance =cls.__new__(cls)  # Can't use method of __new__ itself
#         # It causes deep recursion easily and should use method of father's __new__
#         if not hasattr(cls,'_instance'):
#             cls._instance=super().__new__(cls, *args, **kwargs) #Use method of father's __new__
#         return cls._instance
#     pass
# pass
#




#----------------homework three------------------
class Person():
    def __init__(self):
        __name='xiaohua'
        __age=18
    def __name(self):
       return self.__name









