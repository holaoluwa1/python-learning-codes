# # Collect two numbers as input from the user and assign as variables, a and b, write an if statement that prints 
# "a and b are both positive" if both a and b are positive, prints "Only one is positive" if one of them is 
# positive, and prints "Neither is positive" if neither is positive.
# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# if a > 0 and b > 0:
#     print("a and b are both positive")
# elif a > 0 and b <= 0 or a <= 0 and b > 0 :
#     print("Only one is positive")      
# else:
#     print("Neither is positive")     


# # Collect three numbers x, y and z as a comma separated string input from the user and print "Increasing order"
# # if they are in STRICTLY increasing order, "Decreasing order" if they are in STRICTLY decreasing order, and "Neither" otherwise.
# number = (input("enter three number and separeted by comma: ")).split(",")
# x,y,z = number
# if x > y > z :
#     print("Increasing order")
# elif x < y < z :
#     print("Decreasing order")
# else:
#     print("Neither")    

# # Write a program that reads a string called `palindrome` supplied through user input and checks if it is a 
# palindrome. Print "Is a palindrome" if it is, otherwise print "Not a palindrome".
# program = input("enter a word: ").lower().replace(" ","")
# if program == program[::-1] :
#     print("Is a palindrome")
# else:
#     print("Not a palindrome")    


# # You have three variables: x, y, and z collected as 3 separate inputs from the user. Write an if statement that
# checks if exactly two out of the three variables are equal and prints "Two are equal" if this is true. Otherwise,
# print "All different" or "All same" accordingly.
# x = input("enter a word: ")
# y = input("enter a word: ")
# z = input("enter a word: ")
# if x == y == z:
#     print('All the same')
# elif x == y or y == z or x == z :
#     print("Two are equal")
# else:
#     print("All different")    

# # Given three angles angle1, angle2, and angle3 collected as 3 separate inputs from the user, use if statements
# to check if they can form a valid triangle. Print "Valid triangle" if the sum of the angles is 180 degrees and
# all angles are greater than 0. Otherwise, print "Invalid triangle".
# angle1 = int(input("enter a angle of a triangle: "))
# angle2 = int(input("enter a angle of a triangle: "))
# angle3 = int(input("enter a angle of a triangle: "))
# if angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
#     print("Valid triangle")  
# else:
#     print("Invalid triangle")   

# OR
# if not (angle1 > 0 and angle2 > 0 and angle3 > 0):
#     print('invalid triangle')
#     exit()

# if angle1 + angle2 + angle3 == 180  :
#     print("Valid triangle")  
# else:
#     print("Invalid triangle")  

# # You have a single character variable `ch` supplied through user input. Write an if statement that prints
# "Vowel" if ch is a vowel (a, e, i, o, u, both uppercase and lowercase), and "Consonant" otherwise. Assume that
# the input is a single alphabet character.
# users_input = "ch"

# # Given a comma separated string input from the user of three colors color1, color2, and color3, write an if
# statement to check if all three colors are primary colors (red, blue, yellow). Print "All primary colors" if 
# they are, otherwise print "Not all primary colors".
color = input("enter three color separated with comma: ")
colors = color.split(',')
primary_colors = {'red', 'blue', 'yellow'}
if primary_colors == set(colors):
    print("All primary colors")
else:
    print("Not all primary colors")    

# # You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". Write an if
# statement that prints "Manual mode activated" if mode is "manual", "Automatic mode activated" if mode is
# "automatic", and "System is off" if mode is "off".
# mode = input("enter mode: ").lower()
# if mode == "manual":
#     print("Manual mode activated")
# elif mode == "automatic":
#     print("Automatic mode activated")
# elif mode == "off":
#     print("System is off")
# else:
#     print()    


# # Given a string `message` entered by the user, use if statements to check if the message contains any of
# the words "urgent", "important", or "immediate". If it contains any of these words, print "High priority message".
# Otherwise, print "Normal message"
# message = input("enter a message: ").lower().split()
# if any(word in ["urgent","important","immediate"] for word in message):
#     print("High priority message")
# else:
#     print("Normal message")    
# You have two variables, status1 and status2, provided through user input, each of 	which can be "active",
# “inactive", or "pending". Write an if statement to print 	"Both active" if both statuses are "active",
# "One active" if exactly one is "active",	and "None active" if neither is "active".
# status1 = input("enter your current status: ").lower()
# status2 = input("enter your current status: ").lower()
# if status1 == 'active' and status2 == 'active':
#     print("Both active")
# elif status1 == 'active' or status2 == 'active' :
#     print("One active")
# else:
#     print("None active")       

# Given a string `filename` supplied by the user, write an if statement to check if the	filename ends with 
# “.jpg", ".png", or ".gif". Print "Image file" if it does, otherwise	print "Not an image file".
# filename = input("upload your file: ").lower()
# if filename.endswith(('.jpg','.png','.gif')):
#     print("Image file")
# else:
#     print("Not an image file")    

# You have a variable `access_level` provided through user input which can be "admin",	"user", or "guest".
# Write an if statement that prints "Full access" if access_level is "admin", "Limited access" if it is
# "user", and "No access" if it is "guest".
# access_level = input('enter your level: ')
# if access_level == "admin":
#     print("Full access")
# elif access_level == "user":
#     print("Limited access")
# elif access_level == "user":
#     print("No access")
# else:
#     exit()            
# Given a string `email` collected from the user, write an if statement to check if the	email contains both
# "@" and 	"." characters. Print "Valid email" if it does, otherwise	print "Invalid email".

# email = input('enter your email: ')
# if "@" in email and "." in email:
#     print("Valid email")
# else:
#     print("Invalid email")    
# You have a variable `day` provided by user input which can be any day of the week 	(e.g., "Monday", "Tuesday", 	
# etc.). Write an if statement that prints "Weekend" if the	day is "Saturday" or "Sunday", and "Weekday" if
# it is any other day. 
# day = input('enter a day of the week: ').lower()
# if day in ["Saturday","Sunday"]:
#     print("Weekend")
# else:
#     print("Weekday")    

# Write a program that takes three numbers (num1, num2, num3) as a comma-separated string 	input from the
# user and prints the greatest number. Use conditional statements	to determine which number is the greatest.
# Bonus point if you can do it without `else` 	statements.
# number = (input("enter three numbers separated with comma: ")).split(',')
# num1,num2,num3 = number
# print(num1)




# login verification ask the user to enter a username and password if both match the expected values print "login successful"
# from getpass import getpass
# otherwise print "invalid credentials"
# username = input("enter your username: ").lower()
# password = getpass("enter your password: ")
# user_detail = {'username': "tobi", 'password': 20000}

# if username == user_detail['username'] and password == user_detail['password']:
#     print("login successful")
# else:
#     print("invalid credentials")  

# Atm withdrawal conditions ask the user how much they want to withdraw if the amount is more than 100000 print "limit exceeded"
# if the amount is not a multiple of 100 print "amount must be multiple of 100" if amount is valid print "processing withdrawal of [amount]"
# amount = int(input("enter amount: "))
# if amount > 100000:
#     print("limit exceeded")       
# elif amount % 100 != 0:
#     print("Amount must be multiple of 100")  
# else:
#     print(f"Processing withdrawal of {amount}")   

# Check two string have the same last character write a program that takes two strings and checks if they end in the same 
# # character
# input1 = input("enter a word: ")
# input2 = input("enter a word: ")
# if input1[-1] == input2[-1]:
#     print("same last character")
# else:
#     print("different last character")    

