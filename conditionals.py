# # Let's write a program that takes a number and if that number is greater than 20, then it should print that the number is actually greater than 20... otherwise, just say that number is less than 20

# number = int(input('ENter a number; '))

# if number >= 20:
#     print(f'{number} is actually greater than or equal to 20')
# else:
    # print(f'{number} is less than 20')  



# # WRite a proram that takes a number and tells me if the number is even or odd
# number = int(input("Enter a number: "))
# if number  % 2 ==0:
#    print(f"{number} is an even number")
# else:
#    print(f"{number} is an odd number")

# WRite a program that tells if an accepted number is a multiple of 5
# number = int(input("Enter a number: "))
# if number  % 5 ==0:
#    print(f"{number} is a multiple of 5 ")

# else:
#    print(f"{number} is not a multiple of 5")


# print('Soft one.')


# WRite a program that a checks if a string starts with either letter a or e.
# string = input("enter a word: ").lower()
# if string.startswith(("a","e",)):
#     print(f"{string} start with a or e")
# else:
#     print(f"{string} does not start with a or e")


# WRite a program that checks if the string starts with a vowel... or a consonant
# string = input("enter a word: ").lower()
# if string.startswith(("a","e","o","i","u")):
#     print(f"{string} start vowel")
# else:
#     print(f"{string} does not start vowel")


# string = input("enter a word: ").lower()
# if string[0] in ("a","e","o","i","u"):
#     print(f"{string} start vowel")
# else:
#     print(f"{string} does not start vowel")



# string = input("enter a word: ").lower()
# if string[0] not in 'aeiou':
#     print(f"{string} does not start vowel")

# else:
#     print(f"{string} start vowel")




# Write a program that says "wow, youa re from the east" if the person is from saudi arabia, and if the person is from korea, say they're from Asia. What if the person is from Nigeria, say the person is from Africa... Otherwise, say they're from the Underworld.

# country = input('Enter your country: ')

# if country == 'saudi arabia':
#     print('Wow, you are from the east.')

# elif country in ['korea', 'china', 'khazakhstan', 'north korea', 'Bhutan', 'myanmar', 'japan', 'saudi arabia']:
#     print('You are from Asia')
# elif country == 'nigeria':
#     print('You are from Africa')
# else:
#     print('you are from the Underworld')




# name = 'Tobi'
# age = 24
# course = 'CSC'

# if name == 'Tobi' and 25 < age:
#     print('A')
# elif name == 'John' and 5 > age:
#     print('B')
# elif name == 'Tob' or (age and course=='CS'):
#     print('C')
# elif name== 'Tobi' and course == 'CS':
#     print('D')




# Build a guess game in python
# import random

# generated_num = random.randint(1, 1000)

# print(generated_num)
# users_quess = int(input("enter a number: "))

# if generated_num == users_quess:
#     print("correct")
# else:
#     print("guess not correct") 




# users_age = int(input("enter your age: "))

# if users_age >= 18:
#     print("you are eligible to vote")
# else:
#     print("you are in eligible to vote")       



users_age = int(input("enter your age: "))
users_city = input("enter a city")
users_gender = input("enter your your gender ")



