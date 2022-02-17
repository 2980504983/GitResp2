# def greet_user(user_name):
#     """Display simple greeting. """
#     print(f'Hello!{user_name.title()}')
#
#
# greet_user('ruby')
# greet_user('weiss')
#
# def display_message():
#     print('function')
#
#
# def favorite_book(title):
#     print(f'I like {title}')
#
#
# display_message()
# favorite_book('python')

# def describe_pet(pet_name, pet_type='dog'):
#     """Display info of pet"""
#     print(f'I have a {pet_type}.')
#     print(f'{pet_type}\'s name is {pet_name}')


# describe_pet('cat', 'weiss')
# describe_pet('dog', 'ruby')
# print('')
# describe_pet(pet_type='cat', pet_name='weiss')
# describe_pet(pet_type='dog', pet_name='ruby')

# describe_pet('flower')
# describe_pet(pet_name='glass')

# def make_shirt(size='big', picture='I love python'):
#     print(f'The shirt is {size} and the picture is {picture}')
#
#
# make_shirt()
# make_shirt('middle')
# make_shirt(picture='trying!')

# def describe_city(city_name, city_place='china'):
#     print(f'{city_name} in {city_place}')
#
#
# describe_city('ShangHai')
# describe_city('BeiJin')
# describe_city('JiangXi', city_place='china1')

# def get_formatted_name(first_name, last_name, middle_name=''):
#     if middle_name != '':
#         full_name = f'{first_name} {middle_name} {last_name}'
#     else:
#         full_name = f'{first_name} {last_name}'
#     return full_name.title()
#
#
# print(get_formatted_name('1', '34', 's'))

# def build_person(first_name, last_name, age=None):
#     """return a dict and it includes info of a person"""
#     person = {'first_name': first_name, 'last_name': last_name}
#     if age:
#         person['age'] = age
#     return person
#
#
# musician = build_person('ruby', 'weiss', 15)
# print(musician)

# def get_formatted_name(first_name, last_name):
#     full_name = f'{first_name} {last_name}'
#     return full_name.title()
#
#
# while True:
#     print('please enter your name and if you enter "q" quit')
#
#     f_name = input('please enter your first name:')
#     if f_name == 'q':
#         break
#
#     l_name = input('please enter your last name:')
#     if l_name == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name, l_name)
#
#     print(f'Hello {formatted_name.title()}')

# def city_country(name, place):
#     return f'{name},{place}'
#
#
# print(city_country('JiangXi', place='China'))

# def make_album(singer_name, album_name,song_number=None):
#     album_info = {'singer_name': singer_name.title(),
#                   'album_name': album_name}
#     if song_number:
#         album_info['song_number'] = song_number
#     return album_info
#
#
# zhang = make_album('zhang jie', 'tian xia', 213)
# print(zhang)


# def make_album(singer_name, album_name, song_number=None):
#     album_info = {'singer_name': singer_name.title(),
#                   'album_name': album_name}
#     if song_number:
#         album_info['song_number'] = song_number
#     return album_info
#
#
# while True:
#     print('please enter your name and enter "q" quit')
#     singer = input('name:')
#     if singer == 'q':
#         break
#     album = input('name:')
#     if album == 'q':
#         break
#     info = make_album(singer, album)
#     print(info)

# def greet_users(names):
#     for name in names:
#         msg = f'Hello {name.title()}'
#         print(msg)
#
#
# users = ['ruby', 'weiss', 'yang', 'black']
# greet_users(users)

# unprinted_design = ['phone case', 'robot', 'plane']
# printed_designs = list()
#
# while unprinted_design:
#     current_design = unprinted_design.pop()
#     print(f'{current_design} is printing')
#     printed_designs.append(current_design)
#
# print('\nPrinted:')
# for printed_design in printed_designs:
#     print(printed_design)

# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f'{current_design} is printing')
#         completed_models.append(current_design)
#
#
# def show_completed_models(completed_models):
#     print('\nPrinted:')
#     for completed_model in completed_models:
#         print(completed_model)
#
#
# unprinted_designs_list = ['phone case', 'robot', 'plane']
# unprinted_designs_list_1 = unprinted_designs_list[:]
# completed_models_list = []
#
# print_models(unprinted_designs_list_1, completed_models_list)
# show_completed_models(completed_models_list)

# def sent_message(message_1, message_list):
#     while message_1:
#         message = message_1.pop()
#         message_list.append(message)
#
#
# def show_message(message_1):
#     print('don\'send messages:')
#     for message in message_1:
#         print(message)
#
#
# messages = ['hello', 'hi', 'ei']
# messages_1 = messages[:]
# messages_new = []
# show_message(messages_1)
# sent_message(messages_1, messages_new)
# print(messages)
# print(messages_new)

# def make_pizza(size, *toppings):
#     print(f'\nMake a {size} inch pizza with the following topping:')
#     for topping in toppings:
#         print(f'-{topping}')
#
#
# make_pizza(20, 'pepperoni')
# make_pizza(10, 'mushrooms', 'green peppers', 'extra cheese')

# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
#
#
# print(build_profile('ruby', 'weiss', location='asd', field='physics'))

# def sandwich(*stuffings):
#     print('\nThere are your stuffings:')
#     for stuffing in stuffings:
#         print(stuffing)
#
#
# sandwich('beef', 'pork', 'lettuce')
# sandwich('cucumber', 'lamb')
# sandwich()

# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
#
#
# user_msg = build_profile('Wu', 'ZaiDong', location='China', age=18)
# print(user_msg)

# def make_car(manufacturer, size, **kwargs):
# #     kwargs['manufacturer'] = manufacturer
# #     kwargs['size'] = size
# #     return kwargs
# #
# # $
# # print(make_car('ruby', 'big', production_data='2013', color='red'))
