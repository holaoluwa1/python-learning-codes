# Handle Multiple Exceptions:Write a function safe_divide(a, b) that performs division.
# Handle ZeroDivisionError if the divisor is zero.
# Handle TypeError if the inputs are not numbers.
# Handle ValueError if the inputs are not convertible to floats.



# def safe_divide(a,b):
#     try:
#         a = float(a)
#         b = float(b)
#         # num1 = int(input("enter a number: "))
#         # num2 = int(input("enter a number: "))

#         return a / b 
#     except ZeroDivisionError:
#         print("you can not divide a number by zero")
#     except ValueError:
#         print("you enter a wrong value")
#     except TypeError:
#         print("error...input number")                

#     return 0

# num1 = (input("enter a number: "))
# num2 = (input("enter a number: "))
# print(safe_divide(num1,num2))



# Define a custom exception called NegativeNumberError.
# Write a function check_positive(number) that raises 
# NegativeNumberError if the input number is negative.
# Catch the exception when calling the function.

# age = 0
# try:
#     age = int(input("enter your age: "))
    
# except:
#     print("error....")         

# if age < 0 :
#     raise ValueError("age can not be less than zero")




