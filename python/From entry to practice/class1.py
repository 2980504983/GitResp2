from random import choice


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(f'{self.name} is sitting now.')
#
#     def roll_over(self):
#         print(f'{self.name} rolled over.')
#
#
# my_dog = Dog('willie', 6)
# your_dog = Dog('lucy', 3)
#
# my_dog.sit()
# my_dog.roll_over()
#
# print(f'My dog\'s name is {my_dog.name}')
# print(f'My dog is {my_dog.age}')

# class Restaurant:
#     def __init__(self, name, cuisine_type):
#         self.name = name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print(f'The restaurant\'s name is {self.name}')
#         print(f'It\'s {self.cuisine_type}')
#
#     def open(self):
#         print(f'The restaurant is {self.cuisine_type}')
#
#
# my_restaurant = Restaurant('R', 'open')
# print(my_restaurant.name)
# print(my_restaurant.cuisine_type)
# my_restaurant.describe_restaurant()
# my_restaurant.open()
#
# your_restaurant = Restaurant('W', 'open')
# your_restaurant.describe_restaurant()
#
# she_restaurant = Restaurant('YB', 'open')
# she_restaurant.describe_restaurant()

# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def describe_user(self):
#         print(f'Name: {self.first_name}{self.last_name}')
#
#     def greet(self):
#         print(f'Hello {self.first_name}{self.last_name}')
#
#
# user1 = User('ruby', 'weiss')
# user1.describe_user()
# user1.greet()
#
# user2 = User('Yang', 'black')
# user2.describe_user()
# user2.greet()

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.reading = 0
#
#     def get(self):
#         long_name = f"{self.make} {self.model} {self.year}"
#         return long_name.title()
#
#     def read(self):
#         print(f'This car has {self.reading} mikes on it.')
#
#     def update(self, mileage):
#         if mileage >= self.reading:
#             self.reading = mileage
#         else:
#             print('You can\'t roll back')
#
#     def increment(self, miles):
#         self.reading += miles and miles >= 0
#
#
# my_car = Car('audi', 'a4', 2019)
# # print(my_car.get())
# # my_car.read()
# # my_car.reading = 23
# # my_car.update(10)
# # my_car.read()
# my_car.update(23500)
# my_car.read()
#
# my_car.increment()
# my_car.read()

# class Restaurant:
#     def __init__(self, name, cuisine_type):
#         self.name = name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(f'The restaurant\'s name is {self.name}')
#         print(f'It\'s {self.cuisine_type}')
#
#     def open(self):
#         print(f'The restaurant is {self.cuisine_type}')
#
#     def read(self):
#         print(self.number_served)
#
#     def set(self, number):
#         self.number_served = number
#
#     def increment(self, numbers):
#         self.number_served += numbers
#
#
# re = Restaurant('r', 'open')
# re.read()
# re.set(10)
# re.read()
# re.increment(10)
# re.read()

# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.l_a = 0
#
#     def describe_user(self):
#         print(f'Name: {self.first_name}{self.last_name}')
#
#     def greet(self):
#         print(f'Hello {self.first_name}{self.last_name}')
#
#     def add(self):
#         self.l_a += 1
#
#     def reset(self):
#         self.l_a = 0
#
#
# user1 = User(1, 2)
# user1.add()
# user1.add()
# user1.add()
# print(user1.l_a)
# user1.reset()
# print(user1.l_a)

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.reading = 0
#
#     def get(self):
#         long_name = f"{self.make} {self.model} {self.year}"
#         return long_name.title()
#
#     def read(self):
#         print(f'This car has {self.reading} mikes on it.')
#
#     def update(self, mileage):
#         if mileage >= self.reading:
#             self.reading = mileage
#         else:
#             print('You can\'t roll back')
#
#     def increment(self, miles):
#         self.reading += miles and miles >= 0
#
#
# class Battery:
#     def __init__(self, battery_size=75):
#         self.battery_size = battery_size
#
#     def describe(self):
#         print(f'{self.battery_size}')
#
#     def get_range(self):
#         if self.battery_size == 75:
#             range1 = 260
#         elif self.battery_size == 100:
#             range1 = 100
#         else:
#             range1 = "I don't know"
#
#         print(f"This can can go about {range1} miles on full charge.")
#
#
# class EleCar(Car):
#     def __init__(self, model, make, year):
#         super().__init__(make, model, year)
#         self.battery = Battery()
#
#     def d_b(self):
#         print(f"This car has a {self.battery}")
#
#     def read(self):
#         print('1234')
#
#
# tesla = EleCar('teals', 'models', 2019)
# # print(tesla.get())
# # tesla.d_b()
# # tesla.read()
# tesla.battery.describe()
# tesla.battery.get_range()

# class Restaurant:
#     def __init__(self, name, cuisine_type):
#         self.name = name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(f'The restaurant\'s name is {self.name}')
#         print(f'It\'s {self.cuisine_type}')
#
#     def open(self):
#         print(f'The restaurant is {self.cuisine_type}')
#
#     def read(self):
#         print(self.number_served)
#
#     def set(self, number):
#         self.number_served = number
#
#     def increment(self, numbers):
#         self.number_served += numbers
#
#
# class IceCreamStand(Restaurant):
#     def __init__(self, name, cuisine_type):
#         super(IceCreamStand, self).__init__(name, cuisine_type)
#         flavors = ['r', 'w', 'b', 'y']
#         self.flavors = flavors
#         pass
#
#     def read(self):
#         for flavor in self.flavors:
#             print(flavor)
#
#
# i = IceCreamStand('hh', 'open')
# i.read()

# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.l_a = 0
#
#     def describe_user(self):
#         print(f'Name: {self.first_name}{self.last_name}')
#
#     def greet(self):
#         print(f'Hello {self.first_name}{self.last_name}')
#
#     def add(self):
#         self.l_a += 1
#
#     def reset(self):
#         self.l_a = 0

#
# class Privileges(object):
#     def __init__(self):
#         self.privileges = ['add', 'delete', 'ban']
#
#     def show_privileges(self):
#         print(self.privileges)
#
#
# class Admin(User):
#     def __init__(self, first_name, last_name):
#         super(Admin, self).__init__(first_name, last_name)
#         self.r = Privileges()


# w = Admin('r', 'w')
# w.r.show_privileges()

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.reading = 0
#
#     def get(self):
#         long_name = f"{self.make} {self.model} {self.year}"
#         return long_name.title()
#
#     def read(self):
#         print(f'This car has {self.reading} mikes on it.')
#
#     def update(self, mileage):
#         if mileage >= self.reading:
#             self.reading = mileage
#         else:
#             print('You can\'t roll back')
#
#     def increment(self, miles):
#         self.reading += miles and miles >= 0
#
# print(randint(3, 10))
#
# list_a = [1, 2, 2, 3, 7]
#
# print(choice(list_a))

list_A = [1, 2, 3, 4, 0, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']


class Die:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.full = 0

    def show(self):
        self.a = choice(list_A)
        self.b = choice(list_A)
        self.c = choice(list_A)
        self.d = choice(list_A)
        self.full = f'{self.a} {self.b} {self.c} {self.d}'
        if self.full == 'b 0 c e':
            print(self.full)
            print('go')
            return self.full
        else:
            print(self.full)
            print('true b 0 c e')


r = Die()
# r.show()
# r.show()
a = 0

while True:
    b = r.show()
    a += 1
    if b == 'b 0 c e':
        print(a)
        break
