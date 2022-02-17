# message = input('Tell me something, and I will repeat it back to you:')
# print(message)

# name = input('Please enter your name:')
# print(f'Hello, {name.title()}!')

# prompt = 'If tell us who you are, we can personalize the message you see.'
# prompt += '\nWhat is your first name?'
# name = input(prompt)
# print(f'\nHello, {name.title()}!')

# age = int(input('How old are you?'))
# print(type(age))

# height = input('How old are you, in inches? ')
# height = int(height)
#
# if height >= 48:
#     print('\nYou are tall enough to ride! ')
# else:
#     print('\nYou will be able to ride when you are a little older.')

# number = input('Please enter a number, and I will tell you even or odd: ')
# number = int(number)
#
# if number % 2 == 0:
#     print("It's even! ")
# else:
#     print("It's odd! ")
# car = input('What cars do you want to buy? ')
# print(f'Let me see if I can find you a {car.title()}')

# numbers = int(input('How many people? '))
# if numbers > 8:
#     print('There is no space here! ')
# else:
#     print('ok')

# info = 'Please enter a number, ' \
#        'and I can judge whether it is multiple of 10. '
# info += '\nPlease enter the number: '
# numbers = int(input(info))
# if numbers % 10 == 0:
#     print('Yes')
# else:
#     print('No')

# current_number = 1
# while current_number <= 10:
#     print(current_number)
#     current_number += 1

# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter the 'quit' to end the program"
# message = ""
# while True:
#     message = input(prompt)
#     if message == 'quit':
#         break
#     else:
#         print(message)

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# x = 1
# while x <= 5:
#     print(x)
#     x += 1

# ingredients = ['mushroom', 'extra cheese', 'green pepper',
#                'eggs', 'tomato']
# active = True
# while active:
#     message = input('\nEnter "quit" to end the program'
#                     '\nPlease enter food you want to add: ')
#     if message != 'quit':
#         if message in ingredients:
#             print(f'Adding {message}')
#         elif message not in ingredients:
#             print(f'Sorry, don\'t have {message}')
#     elif message == 'quit':
#         active = False

# while True:
#     message = input('\nEnter "quit" to end the program'
#                     '\nPlease enter your age: ')
#     if message != 'quit':
#         message = int(message)
#         if message < 3:
#             print(f'Hello baby, you are free. ')
#         elif 3 <= message <= 12:
#             print(f'Hi boy, you are 10 dollars')
#         else:
#             print('15 dollars')
#     else:
#         break
# info = 0
# while info <= 5:
#     print(info)
#     info += 1

# unconfirmed_user = ['alice', 'brian', 'CanDance']
# confirmed_users = []
#
# while unconfirmed_user:
#     current_user = unconfirmed_user.pop()
#     print(f'Verifying user: {current_user.title()}')
#     confirmed_users.append(current_user)
# print('\nThe following users have been confirmed:')
# for confirmed_user in confirmed_users:
#     print(confirmed_user)

# pets = ['cat', 'cat', 'dog']
# print(pets)
#
# while 'cat' in pets:
#     pets.remove('cat')
#
# print(pets)

# responses = {}
# polling_active = True
# while polling_active:
#     name = input('\nWhat is your name:')
#     response = input('Which mountain would you like to climb someday?')
#     responses[name] = response
#     repeat = input('would you like to let another person respond?'
#                    '(yes or no)')
#     if repeat.lower() == 'no':
#         polling_active = False
# print('Result:')
# for name, response in responses.items():
#     print(f'{name} like {response}')

# sandwich_order = ['ham sandwich', 'orange sandwich', 'pastrami', 'pastrami',
#                   'pastrami']
# finished_sandwich = []
# print('pastrami is over')
#
# while 'pastrami' in sandwich_order:
#     sandwich_order.remove('pastrami')
#
# while sandwich_order:
#     sandwich = sandwich_order.pop()
#     print(f'I made your {sandwich}')
#     finished_sandwich.append(sandwich)
# print('\nFinished sandwich:\n')
# for sandwich in finished_sandwich:
#     print(sandwich)

users = {}
active = True
while active:
    name = input('\nWhat is your name:')
    place = input('\nwhere would you go?')
    users[name] = place
    again = input('\nAgain?(yes or no)')
    if again.lower() == 'no':
        active = False
for name, place in users.items():
    print(f'\n{name} want to go to {place}')