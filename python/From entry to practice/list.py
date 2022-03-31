# listA=['YIYunXi','DuWanQing','SuYiRan']
# print(listA[-1])
# print(len(listA))
# for item in listA:
#     print('Hi,I\'m %s'%(item))
#     print(f'Hope you are happy in your world,{item.title()}\n')
# a=3
# for lista in listA:
#     a-=1 and a>=0
#     print(f'{lista},{listA[a]}')

# listPizzas=['Supreme Durian Pizza','Fruity Pizza','Seafood pizza']
# for Pizza in listPizzas:
#     print('I like {}'.format(Pizza))
#     pass
# print('\nI really like Pizza')
#
# listAnimal=['owl','cat','dog']
# for animal in listAnimal:
#     print('\n{} is good friend of mankind'.format(animal))
#     pass
# print('They are cute')

# numbers=list(range(0,6,2))
# print(numbers)

# squares=[]
# for value in range(1,11):
#     squares.append(value**2)
#     pass
# print(squares)
#
#
# listA=list(range(6))
# print(min(listA))
# print(max(listA))
# print(sum(listA))


# listsQuare=[value**2 for value in range(1,11)]   # List comprehension
# print(listsQuare)

# for item in range(1,1000_001):
#     # print(item)
#     pass
# item1=list(range(1,1000_001))
# print(min(item1))
# print(max(item1))
# print(sum(item1))

# listOdd_number=list(range(1,21,2))
# for odd_number in listOdd_number:
#     print(odd_number)

# listM_three=list(range(3,31,3))
# for M_three in listM_three:
#     print(M_three)

# print(list(value**3 for value in range(1,11)))
#
# for value in range(1,11):
#     print(value**3)

# listNumber=list(range(11))
# print(listNumber[::5])
# print(listNumber[0:5])
# print(listNumber[:5])
# print(listNumber[5])
# print(listNumber[:])
# print(listNumber[:5:])

# listAnimal=['cat','dog','owl','tiger','fox','wolf']
# print('The first three items in the list are:')
# print(listAnimal[:3])
#
# print(listAnimal[2:5])
#
# print(listAnimal[-3:])

# listNewAnimal=listAnimal[:]
# listAnimal.append('fish')
# print(listAnimal)
# listNewAnimal.append('spider')
# print(listNewAnimal)
# for animal in listAnimal:
#     print(animal)
#     pass
# for NewAnimal in listNewAnimal:
#     print(NewAnimal)
#     pass

# print(list(a for a in listAnimal))
# print(list(b for b in listNewAnimal))

# BuffetFoods=('Scrambled eggs with tomatoes','Steamed Abalone',
# 'Original Sunflower seeds')
# for BuffetFood in BuffetFoods:
#     print(BuffetFood)
#     pass
# print(BuffetFoods[0])
# # BuffetFoods[0]='23333'
#
# BuffetFoods=('Steamed Crab','Fried Chicken')
# for BuffetFood in BuffetFoods:
#     print(BuffetFood)

# CarList=['audi','bmw','subaru','toyota']
# for car in CarList:
#     if car=='bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# car='bmw'
# print(id(car))
# print(bool(car==''))
# car='Audi'
# print(car=='audi')
# print(bool(car.lower()=='audi'))
# print(id(car))
# print(bool(car!='mmp'))

# if 1==1 and 2>0:
#     print('And means both are established')
# if 1!=1 or 1!=0:
#     print('Or indicates that one or more of the two are established')

# List=[1,2,3,4]
# print(1 in List)
# print(5 not in List)

# Banned_User=['Jia','Yi']
# user='Bing'
# if user not in Banned_User:
#     print(f'Dear {user.title()},you can post a response if you wish.')

# ListCars=['AUDI','BWM','TOYOTA']
# print('I guess it\'s True')
# print('AUDI'in ListCars)

# car='toyota'
# print(car=='bwm')
# print(car.title()=='Toyota')
# print(car=='Toyota')
#
# car='BWM'
# print(car=='bwm')
# print(car.lower()=='bwm')

# a=(input('please enter your old:'))
# if a>='18':
#     print('Ok,you are old enough to vote')
#     b=(input('Have you registered to vote yet?:'))
#     if b=='yes' or b=='Yes' or b=='YES':
#         print('All right')
#         pass
#     else:
#         print('Sorry,you have not registered')
# else:
#     print('You are too young')


# a=4
# if a<4:
#     print('free')
# elif a<18:
#     print('25 dollar')
# else:
#     print('40 dollar')

# age=12
# if age<4:
#     price=0
# elif age<18:
#     price=25
# else:
#     price=40
# print(f'The price is {price}')

# requested_toppings=['mushrooms','extra cheese']
# if 'mushrooms' in requested_toppings:
#     print('Adding mushrooms')
# if 'pepperoni' in requested_toppings:
#     print('Adding pepperoni')
# if 'extra cheese' in requested_toppings:
#     print('Adding extra cheese')
# print('finish')

# AlienColor=['red','yellow']
# for alienColor in AlienColor:
#     if alienColor=='green':
#         print('Get five points')

# alien='green'
# if alien=='green':
#     print('Get 5')
# elif alien=='red':
#     print('Get 15')
# else:
#     print('Get 10')

# age = 10
# if age < 2:
#     print('baby')
# elif age < 4:
#     print('toddler')
# elif age < 13:
#     print('children')
# elif age < 20:
#     print('teens')
# elif age < 65:
#     print('adult')
# else:
#     print('old man')


# Favorite_food=['apple','peach','orange']
# if 'apple'in Favorite_food:
#     print('You really like apple')
# if 'peach'in Favorite_food:
#     print('You really like peach')
# if 'orange'in Favorite_food:
#     print('You really like orange')

# requested_toppings=['mushrooms','green peppers','extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print('Sorry,we are out of green peppers right now.')
#     else:
#         print(f'Adding {requested_topping}')
# print(f'\nFinished making your pizza')

# requested_toppings = []
#
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f'Adding {requested_topping}')
# else:
#     print('Are you sure you want a plain pizza?')

# available_toppings=['mushrooms','green peppers','pepperoni'
#                     ,'pineapple','extra cheese']
#
# requested_toppings=['mushrooms','french fries','extra cheese']
#
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f'Adding {requested_topping}')
#     else:
#         print(f'Sorry, we don\' have {requested_topping}')
# print('\nFinished making pizza.')

# names = []
# if names:
#     for name in names:
#         if name == 'Ruby':
#             print(f'Hello {name} , would you like to see status report?')
#         else:
#             print(f'Hello {name}')
# else:
#     print('You need to find users!')

# Current_Users = ['ruby', 'weiss', 'yang', 'black', 'raven']
# New_Users = ['YunXi', 'WanQing', 'YiRan', 'rAven']
#
# for New_User in New_Users:
#     if New_User in Current_Users or New_User.lower() in Current_Users:
#         print(f'Sorry {New_User}, the name already taken.')
#     else:
#         print('The name is created.')

# Numbers = list(range(1,10))
# for Number in Numbers:
#     if Number == 1:
#         print(f'{Number}st')
#     elif Number == 2:
#         print(f'{Number}nd')
#     elif Number == 3:
#         print(f'{Number}rd')
#     else:
#         print(f'{Number}th')
