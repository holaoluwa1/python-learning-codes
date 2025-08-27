# Scenario: You need to check if a user's password is strong enough.

# Task: Write a program in a file named `password_strength_checker.py` that takes a string called `password` and prints `True` if the password is strong and `False` otherwise. A strong password:

# Is at least 8 characters long.
# Contains both uppercase and lowercase characters.
# Contains at least one digit.
# Contains at least one special character (e.g., !@#$%^&*()).

# Tip: Check for True or False for each condition of a strong password and chain the boolean results of each of them. If they are all True, the boolean chaining will result to True and result to False if there is at least one False.DO NOT USE REGEX.

# from string import ascii_lowercase, ascii_uppercase, digits, punctuation

from string import punctuation
while True:
    password = input("Enter your password: ")

    has_at_least_8_chars = len(password) >= 8

    has_uppercase = any([char.isupper() for char in password])

    has_lowercase = any([char.islower() for char in password])

    has_digits = any([char.isdigit() for char in password])

    has_at_least_special_chars = any([char in punctuation for char in password])



    if all([has_at_least_8_chars, has_uppercase, has_lowercase, has_digits, has_at_least_special_chars]):
        print("that a valid password")
        break
    else:
        print("invalid password: your password must contain atleast eight characters a digist a special character and upper and lowercase")    




# if len(password > 8):
        