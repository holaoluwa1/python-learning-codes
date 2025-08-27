# i = 0
# while i < 6:
#     i += 1
#     if i ==3:
#         break
#      print(i)

# # list_of_cities = []
# cities = ['ado', 'osogbo', 'akure', 'ibadan', 'ikeja']
# for index, city in enumerate(cities):
#     print(index,city)

# capitals = {'USA': 'Washington, D.C.', 'France': 'Paris', 'Japan': 'Tokyo', 'Australia': 'Canberra', 'Egypt': 'Cairo'}

# for capital in capitals.items():
#     print(capital)

# my_string = "Python is fun!"
# for char in my_string:    
#     print(f"Character: {char}")

# for x in range(6):
#   if x == 3: break
#   print(x)
# else:
#   print("Finally finished!")
# adjectives = ["fierce", "majestic", "playful"]
# animals = ["lion", "eagle", "dolphin"]

# for adj in adjectives:
#     for animal in animals:
#         print(adj, animal)

# cities = ["Lagos", "Abuja", "Kano", "Ibadan", "Benin City"]
# newlist = [city for city in cities if "a" in city]
# print(newlist)

# newlist = [expression for item in iterable if condition == True]
# print(newlist)

# newlist = [x for x in range(10) if x < 5]
# print(newlist)

# i = 0
# while i in range(5):
#     i += 1
#     print(i)



# Write a program that simulates an ATM withdrawal process. The user should enter their balance and then enter withdrawal amounts until they decide to stop. Ensure the user does not withdraw more than their balance.Sample Input and Output:
# Enter your balance: 500
# Enter withdrawal amount: 100
# Remaining balance: 400
# Do you want to make another withdrawal? (yes/no): yes
# Enter withdrawal amount: 50
# Remaining balance: 350
# Do you want to make another withdrawal? (yes/no): no
# Final balance: 350



# balance = float(input('enter your balance: '))
# while True:
#     withdraw_amount = float(input("enter amout your want to withdraw: "))

#     if withdraw_amount <= balance:
#         print('withdrawal succecful')
#     if withdraw_amount > balance:
#         print("insuffient fund")
#     else:
#         balance -= withdraw_amount
#         print(f"remaining balance: {balance:.2f}")    

#         respond = input("do you still want to withdraw ? (yes/no): ") 
#     if respond != 'yes':
#         break


# Write a program that simulates a grocery store checkout. The user should enter the prices of items until they decide to stop. The program should calculate and display the total cost.
# Sample Input and Output:
# Enter item price: 2.99
# Enter another item? (yes/no): yes
# Enter item price: 5.49
# Enter another item? (yes/no): no
# Total cost: 8.48
# total = 0.0
# while True:
#     items_price = float(input('enter item price: '))
#     total += items_price
#     respond = input("another item? (yes/no):")
#     if respond != "yes":
#         break
# print(total)



# Write a program that continuously prompts the user to enter a password until they enter a valid one. A valid password must be at least 8 characters long and have a maximum of 25 characters.

# while True:
#     password = input("enter password: ")
#     if len(password) >= 8 and len(password) <= 25 :
#         print("succecful login")
#     else: 
#         print("invalid password")    

# Write a program that asks for the user's age and keeps prompting them until they 	enter a valid age (greater than or equal to 0)	Sample Input and Output:
# Enter your age: -5	Invalid age. Please enter a valid age.
# Enter your age: 25 Age accepted.


# while True:
#     age = int(input("enter your age: "))
#     if age <= 1:
#         print("invalid age")
#     else:
#         print(f"your age is {age}")  



# Write a program that takes an integer input from the user and uses a loop to calculate the sum of its digits. Print the sum. Example:
# Input: 1234
# Output: 10 (1+2+3+4)
# total = 0
# digit_cal = []
# digits = input("enter numbers: ")
# for digit in digits:
#     digit_cal.append(digit)
#     total += int(digit)
#     print(f"{"+".join(digit_cal)} {total}")





# Task: Write a program in a file named `password_strength_checker.py` that takes a string called `password` and prints `True` if the password is strong and `False` otherwise. A strong password:

# Is at least 8 characters long.
# Contains both uppercase and lowercase characters.
# Contains at least one digit.
# # Contains at least one special character (e.g., !@#$%^&*()).
from string import punctuation
while True:

    password = input("enter password: ")

    has_at_least_8_chars = len(password) >= 8

    contains_uppercase = any([char.isupper() for char in password])

    contains_lowercase = any([char.islower() for char in password])

    contains_digit = any([char.isdigit() for char in password])

    contains_special_char = any([char in punctuation for char in password])
    
    if all([has_at_least_8_chars, contains_uppercase, contains_lowercase, contains_digit, contains_special_char]):
        print("You enter a strong")
    else:
        print("""Enter a strong pass: Password must contain a digit,uppercase,lowercase and a special character""")    




    



# =====================================ASSIGNMENT==========================================
# 1. Are all numbers odd?
# Input: [1, 3, 5, 7, 9]
# Expected Output: True
values = [1, 3, 5, 7, 9]
value = all([value for value in values if value % 2 == 0])
print(value)


# 2. Are all words longer than 2 characters?
# Input: ["hi", "dog", "go", "sun"]
# Expected Output: False
words = ["hi", "dog", "go", "sun"]
word = all([len(word) > 2 for word in words])
print(word)

# 3. Create a list of triple the value of each number
# Input: [2, 4, 6, 8]
# Expected Output: [6, 12, 18, 24]
nums = [2, 4, 6, 8]
num = [num * 3 for num in nums]
print(num)


# 4. Are all temperatures above 0°C?
# Input: [12, 7, 3, -1, 5]
# Expected Output: False
temperatures = [12, 7, 3, -1, 5]
temperature = all([x >= 0 for x in temperatures])
print(temperature)

# 5. Do all words end with a vowel?
# Input: ["banana", "mango", "kiwi", "grape"]
# Expected Output: True
vowel = 'a','e','i','u','o'
fruits = ["banana", "mango", "kiwi", "grape"]
fruit = all([fruit.endswith(vowel) for fruit in fruits])
print(fruit)


# 6. Create a list of words in lowercase
# Input: ["HELLO", "WORLD", "PYTHON"]
# Expected Output: ["hello", "world", "python"]
greetings = ["HELLO", "WORLD", "PYTHON"]
greeting = [greeting.lower() for greeting in greetings]
print(greeting)


# 7. Is there any number less than 0?
# Input: [5, -2, 3, 0, 8]
# Expected Output: True
numbers = [5, -2, 3, 0, 8]
number = any([number < 0 for number in numbers])
print(number)


# 8. Create a list of words that contain the letter 'e'
# Input: ["sky", "tree", "rock", "stone"]
# Expected Output: ["tree", "stone"]
items = ["sky", "tree", "rock", "stone"]
item = [item for item in items if "e" in item ]
print(item)


# 9. Are all names starting with uppercase letters?
# Input: ["Alice", "Bob", "charlie", "David"]
# Expected Output: False
names = ["Alice", "Bob", "charlie", "David"]
name = all([name[0].isupper() for name in names])
print(name)



# 10. Is there any sentence longer than 20 characters?
# Input: ["Short one", "This is a much longer sentence", "Okay"]
# Expected Output: True
sentences = ["Short one", "This is a much longer sentence", "Okay"]
sentence = any([len(sentence) > 20 for sentence in sentences])
print(sentence)
# =====================================ASSIGNMENT==========================================




