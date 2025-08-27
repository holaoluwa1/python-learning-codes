# Scenario: You want to create a Pig Latin translator.

# Task: Write a program in a file called `pig_latin.py` that takes a string called `text` which is a single valid English word without spaces or special characters and translates the text to Pig Latin. In Pig Latin:

# If a word starts with a single consonant before the first vowel, move the first letter to the end and add "ay" to the end of the word.
# If a word starts with a consonant cluster i.e. more than one consonant before the first vowel, move the consonant cluster to the end and add “ay” to the end of the word.
# If the consonant cluster that starts the word ends with ‘y’, `y` is considered a vowel and therefore remains at the beginning with the rest of string, followed by the consonant or consonant cluster and then “ay” at the end of the word.
# If `y` however starts the word, it is considered a consonant and follows the first rule.
# If a word starts with a vowel, add "way" to the end of the word.


# vowels = tuple("aeuoi")
# consonants = tuple("bcdfghjklmnopqrstvwsyz")
# text = input("enter a word: ")
# if text.startswith(consonants):
#     print(f"{text[1:]}{text[0]}ay")
# elif text[0:2].startswith(consonants):
#     print(f"{text[2:]}{text[0]}ay")    





# Print only the items at even indexes
# items = ['shoe', 'stick', 'toy', 'fruit']

# # Expected Output:
# # 0: shoe
# # 2: toy

# count_item = 0
# for i in range(len(items)):
#     if i % 2 == 0:
#         print(f' {i}: {items[i]}')





# Given two lists of numbers of the same length, print the indices and values	of where they differ in a list.
list1 = [5, 8, 6, 7, 12, 4]
list2 = [5, 3, 6, 9, 12, 0]

# Expected output:
# [
#   'Index 1: 8 != 3',
#   'Index 3: 7 != 9',
#   'Index 5: 4 != 0',
# ]


# for index, (l1,l2) in enumerate(zip(list1,list2)):
#     if l1 != l2:
#         print(f"inddex{index}: {l1} != {l2}")



# for i in range(len(list1)):

#     if list1[i] != list2[i]:
#         print(f"index {i} {list1[i]} != {list2[i]}")




# for i in range(6):
#     for j in range(6):
#         for k in range(6):
#             for m in range(6):
#                 print(f"{i} {j} {k} {m}")




# year = '2003'


# numbers = [5, 38, 282, 29, 48, 2, 288, 28, 4823, 29]
# numbers_int = []

# numbers = ['5', '38', '282', '29', '48', '2', '288', '28', '4823', '29']


# for number in numbers:
#     numbers_int.append(int(number))
# sum_of_numbers = sum(numbers_int)
# print(sum_of_numbers)





numbers = [5, 38, 282, 29, 48, 2, 288, 28, 4823, 29]


# for num in numbers:
#     if num > 48:
#         print(f"i found a number greater than 48")
#         break



# any_num_greater_than_48 = any([ number > 48 for number in numbers])

# print(f"it is {any_num_greater_than_48} there is at atleast a number greater than 48")




# numbers = [15, 8, 82, 239, 484, 2, 88, 258, 23, 297]
# all_value_greater_10 = all([number > 10 for number in numbers])
# print(f"it is {all_value_greater_10} that all numbers are greater than 10")

# list_of_noun = []
# for i in range(5):
#     noun = input("enter noun:")
#     list_of_noun.append(noun)
# print(list_of_noun)   


# all_start_with_uppercase = all([noun[0].isupper() for noun in list_of_noun ]) 


# if all_start_with_uppercase:
#     print('all the noun starts with uppercase')
# else:
#     print('not all the noun starts with uppercase')








    






