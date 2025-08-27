# Assignment 1:
# # Assignment
# # 1. Create a list of the square of each number
# # Input: [1, 2, 3, 4, 5]
# # Expected Output: [1, 4, 9, 16, 25]
# digits = [1, 2, 3, 4, 5]
# numbers = [1, 2, 3, 4, 5]
# square_list = []
# for number in numbers:
#     square = number ** 2
#     square_list.append(square)
# print(square_list)


# # 2. Create a list of names that contain the letter 'a'
# # Input: ["John", "Sara", "Mike", "Amanda"]
# # Expected Output: ["Sara", "Amanda"]
# names = ["John", "Sara", "Mike", "Amanda"]
# names = ["John", "Sara", "Mike", "Amanda", 'Adele', 'Aluko']
# name_list = []
# for name in names:
#     if 'a' in name.lower():
#         name_list.append(name)
# print(name_list)




# # 3. Create a list of Booleans indicating if each number is greater than 10
# # Input: [5, 12, 3, 18, 7]
# # Expected Output: [False, True, False, True, False]
# list_num = []
# numbers = [5, 12, 3, 18, 7]
# for num in numbers:
#     list_num.append(num > 10)
# print(list_num)


# # 4. Create a list of the last characters of each word
# # Input: ["dog", "cat", "lion", "tiger"]
# # Expected Output: ["g", "t", "n", "r"]
# list_animals = []
# animals = ["dog", "cat", "lion", "tiger"]
# for animal in animals:
#     list_animals.append(animal[-1])
# print(list_animals)

# Write a program that takes an integer input from the user and uses a loop to calculate 
# the sum of its digits. Print the sum. Example:
# Input: 1234
# Output: 10 (1+2+3+4)
# total = 0
# string_cal = []
# digits = (input("enter numbers: "))
# for digit in digits:
#     string_cal.append(digit)
#     total += int(digit)
# print(f"{"+".join(string_cal)} = {total}")
    

# Collect a string from the user and use loops to count the number of vowels and consonants in the string. Print the counts. Example:
# Input: "hello world"
# Output: Vowels: 3, Consonants: 7

# string = input("enter a word: ")
# consonants_count = 0
# vowels_count = 0
# for char in string:
#     if char in "aeoui" :
#         vowels_count += 1
#     elif char not in "aeoui":
#         consonants_count += 1
# print(f"the number of vowels in {string} is: {vowels_count}")
# print(f"the number of consonants in {string} is: {consonants_count}")

        





# Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12. Example:
# Input: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 12 = 60
# num = int(input('enter the multiplication: '))
# for i in range(1, 13):
#     print(f"{num} x {i} = {num * i}")


# Collect a string from the user and use a loop to reverse the string. Print the reversed string. Do not reverse the string using [::-1] or reversed().
# Example:
# Input: "python"
# Output: "nohtyp"
# reverse_word_list = []
# words = input("enter word: ")
# for i in range(len(words) - 1, -1, -1):
#     reverse_word_list.append(words[i])
# print("".join(reverse_word_list))


# Collect a list of numbers from the user (entered as comma-separated values) and use a 
# loop to find and print the largest number in the list. Don’t use the built-in max 
# function or anything similar.
# Input: "10, 20, 5, 15"
# Output: 20
# list_of_numbers = []
# numbers = (input("enter a list of number seperated with comma: "))
# numbers = numbers.split(",")
# for number in numbers:
#     list_of_numbers.append(int(number))
# print(max(list_of_numbers))


# Write a program that takes an integer n from the user and calculates the sum of all 
# even numbers from 1 to n. Print the sum.
# Input: 10
# Output: 30 (2 + 4 + 6 + 8 + 10)
# all_even_numbers = []
# n = int(input("enter numbers: "))
# for i in range(1, n +1):
#    if i % 2 == 0:
#     all_even_numbers.append(i)

# print(sum(all_even_numbers))




























# Write a program that takes an integer n from the user and calculates the sum of 
# squares of all numbers from 1 to n. Print the sum. Example:
# Input: 3
# Output: 14 (1^2 + 2^2 + 3^2)
# n = int(input("enter a number: "))
# for i in n:
#     square = n ** 2
#     print(square)

# Collect a phrase from the user and use a loop to generate an acronym by taking the first
# letter of each word. Print the acronym. Example:
# Input: "Portable Network Graphics"
# # Output: "PNG"
# phrase = input("enter word: ").split()
# for ph in phrase:
#     print(ph[0])

# Collect a string from the user and use a loop to count the number of words in the string. 
# Print the count. Example:
# Input: "Hello world from Python"
# Output: 4
# words = input("enter word: ")
# words = words.split()
# for word in len(words):
#     print(word_count)

# Collect a string from the user and only print put the words that start with the letter 
# ‘S’. Example:
# Input: “Print only the words that start with s in this sentence”
# Output: 
# start
# s
# Sentence
# words = input("enter word: ")
# words = words.lower().split()
# for word in words:
#     if word.startswith("s"):
#         print(word)

# Print all the even numbers from 1 to 20 using the range function and a loop.
# for i in range(1, 20):
#     if i % 2 == 0:
#         print(i)
# Go through the string below and if the length of a word is even, print that word.
# st = ‘Print every word in this sentence that has an even number of letters’
# Output: 
# word
# in
# this
# sentence
# that
# an
# even
# number
# of
# st = 'Print every word in this sentence that has an even number of letters'
# words = st.split()
# for word in words:
#     if len(word) % 2 == 0:
#         print(word)

# Write a program that prints the integers from 1 to 100. But for multiples of three, print 
# “Fizz” instead of the number, and for multiples of five, print “Buzz”. For numbers which 
# are multiples of both three and five, print “FizzBuzz”.
# num = int(input("enter number: "))
# for i in range(num, 100):
#     if num % 3 == 0:
#         print("fizz")
#         if num % 5 == 0:
#             print("buzz")
#             # elif num % 3 and 5 == 0:
#                 # print("fizzbuzz")
        

# You are given two lists, names and grades. Print them together
# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']
# Expected Output:
# Ken got grade A
# Mia got grade E
# Rose got grade F
# Henry got grade C
# Suzan got grade B
# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']
# for n, g in zip(names,grades):
#     print(f"{n} got grade {g}")


# Print only the items at even indexes
# items = ['shoe', 'stick', 'toy', 'fruit']
# Expected Output:
# 0: shoe
# 2: toy
# items = ['shoe', 'stick', 'toy', 'fruit']
# for i in range(len(items)):
#     if i % 2 == 0:
#         print(items[i])






