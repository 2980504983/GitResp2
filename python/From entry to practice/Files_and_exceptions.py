# import json
# import unittest
# from name_function import receive
# from name_function import Employee

# file_name = 'pi_digits'
#
# with open(file_name) as file_object:
#     lines = file_object.read()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
#
# print(pi_string)
# message = 'i dog.'
# print(message.replace('dog', 'cat'))
# print(pi_string.replace('3', '#'))

# print(pi_string)
# print(message)

# file_name = 'programming.txt'
#
# with open(file_name, 'w') as f:
#     f.write('I love programming. \n')
#     f.write('You love coding')
#
# with open(file_name, 'a') as f:
#     f.write('\ning')

# user_name = input('please enter your name:')
#
# with open('guest.txt', 'w') as f:
#     f.write(user_name)

# while True:
#     reasons = input('enter:')
#     with open('guest.txt', 'a') as f:
#         f.write(reasons)

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print('1222')
#
# print(5/0)

# while True:
#     first_number = input('first:')
#     if first_number == 'q':
#         break
#         pass
#     second_number = input('second:')
#     if second_number == 'q':
#         break
#
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print('zero can\'be division')
#     else:
#         print(answer)

# filename = 'alice.txt'
# try:
#     with open(filename, encoding='utf-8') as f:
#         contexts = f.read()
# except FileNotFoundError:
#     print(f"Sorry, the file {filename} does not exist")

# def count_words(filename):
#     try:
#         with open(filename, encoding='utf-8') as f:
#             contexts = f.read()
#     except FileNotFoundError:
#         pass
#     else:
#         words = contexts.split()
#         num_word = len(words)
#         print(f"The file {filename} has about {num_word} words")
#
#
# filenames = ['pizza.py', 'function.py', 'main.py', 'ajd']
# for filename1 in filenames:
#     count_words(filename1)


# def sum1():
#     while True:
#         try:
#             a = int(input('please enter number1:'))
#             b = int(input('please enter number2:'))
#         except ValueError:
#             print('please enter number!!!')
#         else:
#             print(a + b)
#             break


# def read1(filename):
#     try:
#         with open(filename) as f:
#             contexts = f.read()
#             print(contexts)
#     except FileNotFoundError:
#         # print(f"File {filename} does not find")
#         pass
#
#
# filenames = ['function.py', 'main.py', 'abc']
# for filename1 in filenames:
#     print(f'------------------------------------------------{filename1}:')
#     read1(filename1)


# def count_word(filename, word):
#     try:
#         with open(filename) as f:
#             contexts = f.read()
#
#             print(contexts.count(word.lower()))
#     except FileNotFoundError:
#         print(f"File {filename} does not find")
#
#
# filenames = ['function.py', 'main.py', 'abc']
# for filename1 in filenames:
#     count_word(filename1, 'R')

# numbers = [2, 3, 5, 7, 11, 13]
# filename = 'number.json'
# with open(filename) as f:
#     numbers = json.load(f)
#
# print(numbers)

# def get_shored_username():
#     try:
#         filename = 'username.json'
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return username
#
#
# def get_new():
#     username = input("what's your name :")
#     filename = 'username.json'
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#     return username
#
#
# def greet_user():
#     username = get_shored_username()
#     if username:
#         print(f"welcome {username}")
#     else:
#         username = get_new()
#
#         print(f"welcome{username}")

#
# filename = 'numbers.json'


# def read_old_user():
#     try:
#         with open(filename) as f:
#             number1 = json.load(f)
#         return number1
#     except FileNotFoundError:
#         return None
#
#
# def get_new_user():
#     number1 = input("what's your number :")
#     with open(filename, 'w') as f:
#         json.dump(number1, f)
#         print('ok I remember')
#     return number1
#
#
# def greet():
#     numbers = read_old_user()
#     if numbers:
#         print(f'Your favorite number is {numbers}')
#     else:
#         numbers = get_new_user()
#         print(f"i remember {numbers}")
#
#
# greet()


# def get_formatted_name(first, last):
#     """create simple name"""
#     full_name = f"{first} {last}"
#     return full_name.title()
#
#
# print("Enter 'q' at any time to quit.")
# while True:
#     first1 = input('what\'your first name?')
#     if first1 == 'q':
#         break
#     last1 = input('what\'your last name?')
#     if last1 == 'q':
#         break
#     formatted_name = get_formatted_name(first1, last1)
#     print(f"\nFormatted_name: {formatted_name}")


# import unittest
#
# from name_function import get_formatted_name
#
#
# class NamesTestCase(unittest.TestCase):
#     """Test name_function.py"""
#
#     def test_first_last_name(self):
#         """Is it possible to handle names like Janis Joplin"""
#         formatted_name = get_formatted_name('janis', 'joplin')
#         self.assertEqual(formatted_name, 'Janis Joplin')
#
#     def test_first_last_middle_name(self):
#         """Is it possible to handle names like Gang Amadeus Mozart"""
#         formatted_name = get_formatted_name('wolfgang',
#                                             'mozart', 'amadeus')
#         self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
#
#
# if __name__ == '__main__':
#     unittest.main()

# class CityTestCase(unittest.TestCase):
#     """Test name_function.py"""
#     def test_city_country(self):
#         city_country = receive('santiago', 'chile')
#         self.assertEqual(city_country, 'Chile,Santiago')
#
#     def test_city_country_population(self):
#         city_country_population = receive('santiago', 'chile', '2000')
#         self.assertEqual(city_country_population, 'Chile,Santiago '
#                                                   '- population 2000')
#
#
# if __name__ == '__main__':
#     unittest.main()

# class AnonymousSurvey:
#     """Collect answer of anonymous survey"""
#
#     def __init__(self, question):
#         """Store a question and prepare for storing the answer"""
#         self.question = question
#         self.responses = []
#
#     def show_question(self):
#         """Display questionnaire"""
#         print(self.question)
#
#     def store_responses(self, new_responses):
#         self.responses.append(new_responses)
#
#     def show_results(self):
#         print("Survey results:")
#         for response in self.responses:
#             print(f"-{response}")

# question = "what language did you first learn to speak?"
# my_survey = AnonymousSurvey(question)
#
# my_survey.show_question()
# print("Enter 'q' at any time to quit.\n")
# while True:
#     response = input("language: ")
#     if response == 'q':
#         break
#     my_survey.store_responses(response)
#
# print("\nThank you to everyone who participated in the survey!")
# my_survey.show_results()


# class TestAnonymousSurvey(unittest.TestCase):
#     """Test for AnonymousSurvey"""
#
#     def setUp(self):
#         """
#         create a object and one group answers for using of test
#         :return:
#         """
#         question = "what language did you first learn to speak?"
#         self.my_survey = AnonymousSurvey(question)
#         self.responses = ['English', 'Spanish', 'Mandarin']
#
#     def test_store_single_response(self):
#         """Test whether a single response will be stored"""
#         self.my_survey.store_responses(self.responses[0])
#         self.assertIn(self.responses[0], self.my_survey.responses)
#
#     def test_store_three_responses(self):
#         for response in self.my_survey.responses:
#             self.my_survey.store_responses(response)
#         for response in self.my_survey.responses:
#             self.assertIn(response, self.my_survey.responses)
#
#
# if __name__ == '__main__':
#     unittest.main()

# class Employee:
#     def __init__(self, first_name, last_name, annual_salary):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.annual_salary = annual_salary
#
#     def give_raise(self, raising=5000):
#         self.annual_salary += raising

# class TestEmployee(unittest.TestCase):
#     """Test for Employee"""
#
#     def setUp(self):
#         self.ruby = Employee('ruby', 'weiss', 100000)
#
#     def test_give_give_default_raise(self):
#         increased_salary = self.ruby.give_raise()
#         self.assertEqual(105000, increased_salary)
#
#     def test_give_custom_raise(self):
#
#         increased_salary = self.ruby.give_raise(10000)
#         self.assertEqual(110000, increased_salary)
#
#
# if __name__ == '__main__':
#     unittest.main()
