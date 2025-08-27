# Write a program that asks the user for their name and then greets them with their name: Print a greeting message that includes the user's name in the format "Hello, {name}!".
# name = input('what is your name ?')
# print(f'Hello, {name}')

# Ask the user for their birth year and calculate their age. Print the user's age in the format “You are {age} years old.”.
# birth_year = int(input("what your birth year: ") )
# age = 2025 - birth_year
# print(f"birth_year {age} year old")

# Ask the user for their favourite color. Print a statement that includes the color in the format “Your favorite color is {favourite_color}.”
# favourite_color = input('What is your favorite color?  ')
# print(f'Your favorite color is {favourite_color}.')

# Ask the user to input some text and check if it is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. `madam` or `nurses run` or `121`.
# text = input("Enter a text: ").replace(" ","").lower()
# print(text[::-1] == text)



# Print a statement in the format “It is {is_palindrome} that {text} is a palindrome.”. `is_palindrome` is either `True` or `False`.
# text = input('enter a text: ')
# is_palindrome = text == text[::-1]
# print(f'It is {is_palindrome} that {text} is a palindrome.')

# Create a program that asks the user to input a password and checks if it meets certain criteria (at least 8 characters and not more than 30 characters).
# Print a statement in the format “It is {is_valid} that the password fulfils the criteria.”. `is_valid` is either `True` or `False`.
# Bonus point if you can hide the password input from displaying on the screen as clear text.
# from getpass import getpass
# password = getpass("Enter your password: ")
# is_valid = 8 <= len(password) <= 30
# print(f"It is {is_valid} that the password fulfils the criteria.")

# Write a program that asks the user for their weight (in kilograms) and height (in meters) and calculates their Body Mass Index (BMI).
#  Calculate the BMI using the formula BMI = weight / (height ** 2). Round the BMI to 2 decimal places. Print a statement in the format “Your BMI is {BMI}”..
# weight = float(input("what is your weight in kilograms ?") )
# height = float(input("what is your height in meters ?") )
# BMI = weight / (height **2)
# print(f"your BMI is {BMI:.2f}")










# person_in_room = input("Enter a name :") 
# number = input("Enter a number :")
# adjective = input("Enter a adjective :")
# colour = input("Enter a colour :")
# noun_1 = input("Enter a noun :") 
# types_of_food = input("Name a type of food :")
# noun_2 = input("Enter a noun :")
# verb_ending_ing = input("Enter a ver ending with 'ing' :")
# article_of_clothing = input("Enter a clothing article :")
# adjective_2 = input("Enter a adjective :")
# celebrity = input("Enter a celebrity name :")
# number_2 = input("Enter a number :")
# person_in_room_2 = input("Enter a name :")
# noun_3 = input("Enter a noun :")
# person_in_room_3 = input("Enter a person :")
# occupation = input("Enter an occupation :")


# story = (f"""
# my name is {person_in_room} and i am {number} years old. if i were president. i'd do a whole bunch of {adjective} things
# i would drive the biggest {colour} car in the country, and that car would go faster than any other {noun_1} in the world!
# everyone would eat pepperoni {types_of_food} for dinner
# i would live in the statue of {noun_2} and build a {verb_ending_ing} pool at her feet
# i would wear a/an {article_of_clothing} on my head, and everyone would say i look {adjective_2} like {celebrity}
# school would be open only {number_2} days a year 
# i would give my friends the best jobs, i would nominate {person_in_room_2} to be secretary of the {noun_3} and {person_in_room_3} could be vice {occupation}

# # """)
# print(story)



# term_of_endearment = 

# term_of_enderment = input("Enter a review :")
# first_name = input("Enter your first name :")
# first_name_and_last_name = input("Enter your first name and last name :")
# place = input("Name a place :")
# day_of_the_week = input("Enter a day in a week :")
# adjective = input("Enter a adjective :")
# color = input("Enter a color :")
# item_of_clothing = input("Enter a item of clothing :")
# number = input("enter a number :")
# verb_1 = input("Enter a verb :")
# verb_2 = input("Enter a verb :")
# verb_3 = input("Enter a verb :")
# verb_4 = input("Enter a verb :")

# story = (f'''
# # Hey {term_of_enderment}, it's me. what's up ? you know,
# {first_name} {first_name_and_last_name}. from the
#  {place} two {day_of_the_week}s ago. i was the {adjective} guy
#  in the {color} parachute {item_of_clothing} i paid the bus boy
#  {number} dollars to {verb_1} me your information. i was
#  wondering if maybe you'd like to {verb_2} out with me. please don't
#  call the {verb_3} department. alright, i'll {verb_4}. so, that's a no, right?
# ''')

# print(story)
