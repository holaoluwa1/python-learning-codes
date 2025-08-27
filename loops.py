
# while True:
#     password = input("Enter password: ")
#     if len(password) > 8:
#         break



# WRite a program that first asks you for your name and then infinitely prints "my name is ..."

# name = input("enter your name: ")

# while True: 
#     print("your name is ", name)
#     print()



# counter

i = 0

# while i <= 10:
#     print(i, 'hello world')
#     i += 1


# WRite a simple program that prints hello world 100 times
# j = 1

# while j <=100:
#     print(j, 'hello world')
#     j +=1

# Write a proram that asks a user's name once... and then prints that name 14 times..,. in this format: 1. name
# 2. name
# 3. name

# name = input("enter your name: ")
# j = 1
# while j <=14:
#     print(f"{j}. {name}" )
#     j += 1
    

# i = 0

# while i < 5:
#     print(i * 2)
#     i += 1



# multiplication table 2

# j = 1

# while j <= 30:
#     print(f"2 *  {j} = {2*j}")
#     j += 1




# Write a program that takes a number and gives us the multiplication table of that number
# 2 * i = 

# number = int(input("enter a number: "))
# j = 1
# while j <= 12:
#     print(f"{number} * {j} = {number*j}")
#     j += 1


# i = 50
# while i > 6:
#     print(i)
#     i -= 1

# Write a program that gives me 1 - 100 in decending order
# j = 100
# while j > 0:
#     print(j)
#     j -= 1


# countries = ['uk', 'germany', 'netherlands', 'usa', 'russia', 'nigeria', 'finland', 'belgium']

# print(countries[0][0])
# print(countries[1][0])
# print(countries[2][0])
# print(countries[3][0])
# print(countries[4][0])
# print(countries[5][0])



# j = 0
# while j < len(countries):
#     print(countries[j][0])
#     j += 1




# number = int(input("enter a number: "))
# if number % 2 == 0:
#     print("even number")
# else:
#     print("odd number")





# number = int(input("enter a number: "))
# if number % 2 != 0:
#     print(" odd number")
# else:
#     print("even number") 

# num = int(input("enter a number: "))
# i = 2
# while i < num :
#     if num % i == 0:
#         print("not prime number")
#         break
#     i += 1

# else:
#     print("prime number")





#  Go through the string below and if the length of a word is even, print that word.	st = ‘Print every word in this sentence that has an even number of letters’	Output: 	word	in	this	sentence	that	an	even	number	
# st = 'Print every word in this sentence that has an even number of letters'
# list_st = st.split(" ")

# i = 0

# while i < len(list_st):
#     if len(list_st[i]) % 2 == 0:
#         print(list_st[i])
#     i += 1



# WRITE A PROGRAM THAT PRINTS NUMBERS BETWEEN 18 AND 40 WITH WHILE LOOP
# i = 19

# while i <= 40:
#     if i % 2 == 0:

#         print(i)

#     i += 1



# i = 19

# while i <= 40:
#         print(i)
#     i += 2



# FOR LOOPS

# for i in range(91, 8, -1):
#     if i * 2 > 25:
#         print(i)
    

# for i in range( 5): # 
# #     print("Ayemi")


# # WRite a program that prints welcome to SQI 88 times
# # for i in range(88):
# #     print(" Welcome to SQI")


# # for i in range(1, 31):
# #     print(f'2 x {i} = {2 * i}')


# # 2 x 1 = 

# # for i in range(1, 31):
# #     print(f'10 x {i} = {10 * i}')

# # number = int(input("enter the multiplication table you want: "))
# # to_range = int(input("to what range? "))
# # for i in range(1, to_range + 1):
# #     print(f'{number} x {i} = {number * i}')    



# # *
# # **
# # ***
# # ****
# # *****
# # ******
# # *******

# # For loop to draw a right-angled triangle 

# # for i in range(1, 6):
# #     print("*" * i)

# # To draw a right-angled triangle upside-down

# # for i in range(6, 1, -1):
# #     print("*" * i)



# animals = ['Goat', 'Lion', 'Tiger', 'Chihuahua', 'Panther', 'Jaguar']


# # for i in range(len(animals)):
# #     print(animals[i] * 3)



# # # For each loop

# # for animal in animals[:3]:
# #     print(animal)



# places = ["Abu Dhabi", "Dubai", "Kuwait", "Saudi Arabia", "Washington DC", "Qatar", "Bahrain", "Jordan", "UAE"]
# # last_four = places[-4 :]
# # last_four.sort()

# # for place in last_four:
# #     print(place)




# # Show me all the places we have here
# for place in places:
#     print(place.upper())



# # Get me the first and last character of every place
# for place in places:
#     print(place[0], place[-1])






# input1 = int(input("enter a number: "))
# input2 = int(input("enter a number: "))
# input3 = int(input("enter a number: "))
# input4 = int(input("enter a number: "))
# input5 = int(input("enter a number: "))
# input6 = int(input("enter a number: "))
# print(input1 + input2 + input3 + input4 + input5 + input6)




# total = 0
# for i in range(10):
#     num = int(input("enter a number: "))
#     total += num
# print(total)



# employee_names = ['Amina Yusuf', 'Chinedu Okafor', 'Ngozi Nwosu', 'Bola Adebayo', 'Emeka Eze', 'Zainab Abdullahi', 'Tunde Balogun', 'Grace Umeh', 'Ibrahim Musa', 'Funke Adeyemi']
# print("emp_id\t\t\tfirstname\t\t\tlastname")
# for emp_id, employee in enumerate(employee_names, start= 1011):
#     # print(employee)
#     first_name = employee.split()[0]
#     last_name = employee.split()[1]

#     print(f"{emp_id}\t\t\t{first_name}\t\t\t\t{last_name}")

languages = ["Python", "Java", "C++", "JavaScript", "Ruby"]
newlist = [x if x != "JavaScript" else "TypeScript" for x in languages]
print(newlist)


