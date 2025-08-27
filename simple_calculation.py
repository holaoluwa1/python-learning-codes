# Project Overview:Create a simple calculator program that performs basic arithmetic operations in a file named `simple_calculator.py`.

# Objective: Build a calculator that can perform addition, subtraction, multiplication, and division operations on two numbers.

# Calculator Operations:Addition (+): Adds two numbers.Subtraction (-): Subtracts the second number from the first.Multiplication (*): Multiplies two numbers.Division (/): Divides the first number by the second (handling division by zero).

# User Interface:- Display a menu with options for each operation.- Prompt the user to enter two numbers and select an operation.- Perform the selected operation and display the result.- Handle division by zero scenarios.- Assume the user enters only valid data type inputs.



def selection_options():
    print("""
    1. Addition (+)
    2. Subtraction (-)
    3. Multiplication (*)
    4. Division (/)
    5. Exit

    Choose an option:
    """)
    try:
        option = int(input())
        

        if option not in [1, 2, 3, 4, 5]:
            print("Invalid option")
            exit()

        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
    except Exception:
        print("Erorr...invalid option")
        exit()    

    if option == 1:
        # num1 = float(input('Enter first number: '))
        # num2 = float(input('Enter second number: '))
        print(f'{num1} + {num2} = {addition(num1,num2)}')    
    elif option == 2:
        # num1 = float(input('Enter first number: '))
        # num2 = float(input('Enter second number: '))
        print(f'{num1} - {num2} = {subtraction(num1,num2)}')  
    elif option == 3:
        # num1 = float(input('Enter first number: '))
        # num2 = float(input('Enter second number: '))
        print(f'{num1} * {num2} = {multiplication(num1,num2)}')
    elif option == 4:
        # num1 = float(input('Enter first number: '))
        # num2 = float(input('Enter second number: '))
        print(f'{num1} / {num2} = {division(num1,num2)}')
    elif option == 5:
        print("Exiting the program...")
        exit()




def addition(a,b):
    return a + b

# selection_options()        

def subtraction(a,b):
    return a - b   
# selection_options()     

def multiplication(a,b):
    return a * b
# selection_options()        

def division(a,b):
    return a / b 

selection_options()       
