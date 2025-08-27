# # sum, max, len, min, print, exit,


# # User-defined functions


# # A LIST that gives us back 10 random numbers


# from random import randint


# def generate_rand_nums():
#     random_numbers = []

#     for i in range(10):
#         num = randint(1, 40)
#         random_numbers.append(num)


#     print(random_numbers)


# # *****************************************************

# # random_numbers = []

# # for i in range(10):
# #     num = randint(1, 40)
# #     random_numbers.append(num)


# # print(random_numbers)

# generate_rand_nums()



# # *****************************************************


# # random_numbers = []

# # for i in range(10):
# #     num = randint(1, 40)
# #     random_numbers.append(num)


# # print(random_numbers)

# generate_rand_nums()


# from time import sleep
# from os import system

# def loader(num=4): 
    
#     for i in range(num):
#         print('Loading.  \r', end='')
#         sleep(1)
#         print('Loading.. \r', end='')
#         sleep(1)
#         print('Loading...\r', end='')
#         sleep(1)
        
#         system('cls')
    

# loader(1) # Run our loader feature just once



# # Arguments and parameters



# print("****************** ONLINE REGISTRATION ****************")

# loader(2) # Run our loader feature times

# option  = input("""
# CHOOSE AN OPTION

# 1. Register
# 2. Login
# 3. Exit

# """)


# loader()

# if option == "1":
#     uname = input('Enter your username: ')
#     password = input('Enter password: ')
    
#     print('Registered successfully!\n Logging in...')
#     loader()
    
#     print(f'Welcome to your dashboard, {uname}')
    
# elif option == "2":
#     uname = input('Enter your username: ')
#     password = input('Enter password: ')
    
#     print('Logging in...')
   
#     print(f'Welcome to your dashboard, {uname}')
    





# A list of 10 random numbers between a specified range

# import random

# random_numbers = []

# start_from = int(input('Enter where to start from: '))
# end_at = int(input('Enter where to end at: '))

# for i in range(10):
#     rand_number = random.randint(start_from, end_at)
#     random_numbers.append(rand_number)
    
 
# print(random_numbers)













# A list of 10 random numbers between a specified range using a user-defined function

# import random

# def get_rand_nums(start, end):
#     random_numbers = []

#     for i in range(10):
#         rand_number = random.randint(start, end)
#         random_numbers.append(rand_number)
        
#     # print(random_numbers)
    
#     return random_numbers
    

# myvar = get_rand_nums(4, 100)


# print(f"The value of myvar is: {myvar}")

# get_rand_nums(4, 28)







# Write a function sum_numbers(a, b) that returns the sum of two numbers.

# def sum_numbers(a, b):
#     sum_of_nums = a + b
    
#     return sum_of_nums

# def sum_numbers(a, b):
#     return a + b



# result = sum_numbers(76, 883)
# print(f'The result is: {result}')


# Write a function is_even(n) that returns True if n is even and False if n is odd.

# def is_even(n):
#    if n % 2 == 0:
#        return True
#    else:
#        return False
   
# print(is_even(8))  

# number = int(input('Enter something: '))
 
# print(is_even(number))   

# print(is_even(777))   



# Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if both words begin with the same letter.
# is_alliteration(‘Levelheaded llama’) —> True
# is_alliteration(‘Crazy Kangaroo’) –> False

# def is_alliteration(two_word_string):
#     splited_text =two_word_string.lower().split(" ")
#     if splited_text[0][0]== splited_text[1][0]:
#         return(f"It is true that they are an aliteration")
#     else:    
#         return(f"It is false that they are an aliteration")
    
    



# print(is_alliteration("mummy mighty"))



# def run(a, b, c):
#     pass


# run(3, 58)
    




def run(a, b, *args, **kwargs):
    
    print(args)
    print(kwargs)
    # return max(args)
    
    

run(23, 54, 4, 34, 56, 43, 65, 43, 6, 34, 65, 34, name="Tobi", course="CSC")

