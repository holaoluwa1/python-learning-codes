# Write a function sum_numbers(a, b) that returns the sum of two numbers.

# def sum_numbers(a, b):
#     return a + b

# print(sum_numbers(4,5))


# Write a function is_even(n) that returns True if n is even and False if n is odd.

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     return False

# print(is_even(5))  

# def is_even(n):
#     return n % 2 == 0


# Write a function is_prime(n) that returns True if n is a prime number and False otherwise.

def is_prime(n):
    if n < 2:
        return(f'False')
    elif n % 2 != 0:
        return(f'True')
    else:
        return(f'False')
print(is_prime(9)) 

# Using the is_prime(n) function from number 3, write a function that asks a user for an input n and returns all the prime numbers up to n.
# def is_prime(n):
#     if n < 2:
#         return(f'False')
#     elif n % 2 != 0:
#         return(f'True')
#     else:
#         return(f'False') 
# number = int(input("Enter a number: ")) 
# print(is_prime(number))              

# Write a function lesser_of_two_evens(a, b) that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd.

# def lesser_of_two_evens(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         return min(a, b)
#     else:
#         return max(a, b)  
# print(lesser_of_two_evens(5,9)) 


# Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if both words begin with the same letter.
# is_alliteration(‘Levelheaded llama’) —> True
# is_alliteration(‘Crazy Kangaroo’) –> False

# def is_alliteration(two_word_string):
#     split_two_word_string = two_word_string.lower().split(" ")
#     if split_two_word_string[0][0] == split_two_word_string[1][0]:
#         return True
#     else:
#         return False
# print(is_alliteration('book tall')) 

# Write a function old_macdonald(name) that capitalizes the first and fourth letters of a name
# old_macdonald(‘macdonald’) —> MacDonald
# Note: ‘macdonald’.capitalize() returns Macdonald, not MacDonald.

# def old_macdonald(name):
#     return name.capitalize() + name[3].upper()
# print(old_macdonald('macdonald'))    


# Write a function spy_game(list_of_ints) that takes in a list of integers and returns True if it contains 007 in order.
# spy_game([1, 2, 4, 0, 0, 7, 5]) —> True
# spy_game([1, 0, 2, 4, 0, 5, 7]) —> True
# spy_game([1, 7, 2, 0, 4, 5, 0]) —> False
# contains = [0,0,7]
# def spy_game(list_of_ints):

#     if contains in  list_of_ints:
#         return True
#     else:
#         return False   

# print(spy_game([1, 2,  4, 0, 0, 7, 5]))         

# def spy_game(list_of_ints):
#     contains = [0, 0, 7]

#     for num in list_of_ints:
#         if contains[0] == num:
#             del contains[0]
        
    
#     if contains == []:
#         return True
#     return False






# Write a function vol(radius) that computes the volume of a sphere given its radius.



# Write a function range_check(num, low, high) that checks whether a number is in a given range (inclusive of high and low).
# def range_check(num, low, high): 
    # return low <= num <= high

#     if num in range(0,9):
#         return(f'range: 0-9')
#     elif     



# Write a function upper_lower(text) that accepts a string and calculates the number of uppercase letters and lowercase letters.

# def upper_lower(text):
#     uppercase_count = sum(1 for char in text if char.isupper())
#     lowercase_count = sum(1 for char in text if char.islower())
#     return uppercase_count, lowercase_count

# print(upper_lower('myname'))

# def upper_lower(text):
#     count_upper = 0
#     count_lower = 0

#     for char in text:
#         if char.islower():
#             count_lower += 1
#         elif char.isupper():
#             count_upper += 1    
#     return count_lower, count_upper    
# print(upper_lower('my name olaolWA'))         



# Write a function unique_list(list_items) that takes in a list and returns a new list with unique elements of the first list. Do not use the set() constructor.
def unique_list(list_items):
    uniques = []
    
    for item in list_items:
        if item not in uniques:
            uniques.append(item)
        
    return uniques


# Write a function multiply(list_items) to multiply all the numbers in a list.
# Sample List: [1, 2, 3, -4]
# Expected output: -24

# def multiply(list_items):
#     result = 1
#     for num in list_items:
#         result *= num
#     return result

# sample_list = [1,2,3,-4]  
# print(multiply(sample_list))        


# Write a function is_pangram(text) to check whether a string is a pangram or not. 
# Note: A pangram is a word or sentence that contains every letter of the alphabet at  
# least once. For example: “The quick brown fox jumps over the lazy dog”.
# Hint: Import and use the string module.

# def is_pangram(text):
#     alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,s,y,z'
      for letter in alphabet:
        if letter not in text:
            break
      else:
        print("the word is a pangram")
#     if alphabet in text:
#         return('pangram')
#     # else:
#         return('not pangram')    
# print(is_pangram('abcdefghijklmnopqrstuvwsyz')) 


# Write a function are_anagrams(s1, s2) that checks if two strings are anagrams of each
# other. a word, phrase, or name formed by rearranging the letters of another, such as
# spar, formed from rasp.



# Write a function calculate_bmi(weight, height) that calculates the Body Mass Index 
# (BMI) given weight in kilograms and height in meters.

def calculate_bmi(weight, height):
    return weight / (height **2)   

print(calculate_bmi(23,5.2))

# Write a function calculate_simple_interest(principal, rate, time) that calculates the 
# simple interest given principal amount, interest rate, and time (in years).
