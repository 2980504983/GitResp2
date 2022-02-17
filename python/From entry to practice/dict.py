# alien_0 = {'color': 'orange', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# alien_0 = dict()
#
# alien_0['color'] = 'orange'
# alien_0['points'] = 5
# print(alien_0)

# alien_0 = {'color': 'red'}
# print(f"The alien is {alien_0['color']}")
# alien_0['color'] = 'orange'
# print(f"The alien is now {alien_0['color']}")

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original position {alien_0['x_position']}")
# alien_0['speed'] = 'fast'
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# alien_0['x_position'] += x_increment
# print(f"New position {alien_0['x_position']}")

# alien_0 = {'color': 'orange', 'points': 5}
# print(alien_0)
# del alien_0['points']
# print(alien_0)

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
#     }
#
# languages = favorite_languages['sarah'].title()
# print(f'Sarah\'s favorite languages is {languages}')

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# # print(alien_0['hp'])  # KeyError
# point_value = alien_0.get('hp', 'No hp value assigned')
# print(point_value)
# # print(alien_0['hp'])

# acquaintance_msg = {'first_name': 'Yi', 'last_name': 'YunXi', 'age': 18,
#                     'city': 'Ning'}
# print(acquaintance_msg)

# favorite_numbers = {'YiYunXi': 0, 'DuWanQing': 1, 'SuYiRan': 2}
# print(favorite_numbers['YiYunXi'])
# print(favorite_numbers['DuWanQing'])
# print(favorite_numbers['SuYiRan'])

# glossaries = dict()
# glossaries['list'] = 'Used to store data'
# glossaries['int'] = 'number'
# glossaries['index'] = 'Determine the location'
#
# print(f"list:\n{glossaries['list']} \n int:\n{glossaries['int']}"
#       f" \n index:\n{glossaries['index']}")

# user_0 = {
#     'userName': 'cheese',
#     'first': 'enrico',
#     'last': 'fermi'
#     }
# for k, v in user_0.items():
#     print(f"\n key: {k}")
#     print(f"value: {v}")

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
#     }
#
# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}")

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
#     }
#
# for name in favorite_languages:
#     print(name.title())

# friends = ['phil', 'sarah']
#
# for friend in favorite_languages.keys():
#     print(f'Hi,{friend.title()}')
#
#     if friend in friends:
#         language = favorite_languages[friend].title()
#         print(f'Hi,{friend.title()}.I see you love {language}')
#
# if 'erin' not in favorite_languages.keys():
#     print('Erin, please take our poll!')

# for name in sorted(favorite_languages.keys()):
#     print(f'{name.title()},thank you for taking the poll.')
# for languages in set(favorite_languages.values()):
#     print(languages)

# rivers = {'nile': 'egypt', 'yellow river': 'china'}
# for river in rivers.keys():
#     country = rivers[river].title()
#     print(river)
#     print(country)

# members = ['jen', 'ea']
# for member in members:
#     if member in favorite_languages:
#         language = favorite_languages[member].title()
#         print(f'Hi {member} \nI see you love {language} and thank you for'
#               f' take our poll!')
#     else:
#         print(f'Hi {member} \nPlease take our poll')

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

# aliens = []
#
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['speed'] = 'fast'
#         alien['points'] = 15
# for alien in aliens[:5]:
#     print(alien)
# print('...')
# aliens = []
# new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
# old_alien = {'color': 'red', 'points': 10, 'speed': 'fast'}
# aliens.append(new_alien)
# aliens.append(old_alien)
# for alien in aliens:
#     for item in alien.items():
#         item1 = list(item)
#         print(item1)

# pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese']}
# print(f"You ordered a {pizza['crust']}_crust pizza with the "
#       f"following topping:")
# for topping in pizza['toppings']:
#     print("\t" + topping)

# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell']
#     }
#
# for name, languages in favorite_languages.items():
#     if len(languages) > 1:
#         print(f'{name.title()}\' favorite languages are :')
#         for language in languages:
#             print(language.title())
#     else:
#         print(f'{name.title()}\' favorite language is :')
#         for language in languages:
#             print(language.title())

# user = {
#     'happy': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'paris',
#         },
#
#     'sad': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#         }
# }
#
# for name, info in user.items():
#     print('')
#     print(f'Name: {name.title()}')
#     print(f"Full Name: {info['first']} {info['last']}")
#     print(f"Location: {info['location'].title()}")

# people = list()
#
# ruby = {'name': 'ruby', 'age': 18, 'color': 'red'}
# weiss = {'name': 'weiss', 'age': 18, 'color': 'white'}
# people.append(ruby)
# people.append(weiss)
#
# for item in people:
#     print('')
#     print(f"Name: {item['name'].title()}"
#           f"\n age: {item['age']}"
#           f"\n color: {item['color']}")

# animals = {
#     'r': {'variety': 'dog',
#           'host': 'ruby',
#           'color': 'red',
#           },
#
#     'w': {'variety': 'cat',
#           'host': 'weiss',
#           'color': 'white',
#           },
# }
#
# for name, info in animals.items():
#     print('')
#     print(f"{name.title()}:\n{info}")

# favorite_places = {
#     'ruby': ['W', 'w'],
#     'weiss': ['R', 'r'],
#     'yang': ['B', 'b'],
#     'black': ['Y', 'y'],
# }
# for name, info in favorite_places.items():
#     print('')
#     print(f'{name.title()} like {info}')
#
# cities = {
#     'BeiJin': {'country': 'China',
#                'population': 'big',
#                'fact': 'strong',
#                },
#
#     'JiangXi': {'country': 'China',
#                 'population': 'small',
#                 'fact': 'slow',
#                 },
# }
# for name, info in cities.items():
#     print('')
#     print(f'{name.title()}:\n{info}')

