# num1 = 234
# num2 = 456
# year = 2025
# print("The first number,"+ str(num1) + "will be replaced by"+ str(num2)+ "at the end of the year"+ str(year))

# A program that takes number of seconds and then tell us how many minutes are there.
# seconds = int(input("enter the number in seconds: "))
# print(seconds // 60 )

# A pogram that takes seconds and tells us how many minutes and seconds are there.
# seconds = int(input("enter a the number in seconds: ") )
# seconds // 60
# print(seconds % 60)
print(f"{seconds//60} minutes, {seconds % 60} seconds.")

# Write a program that takes a number and tells us if the number is an even number. For example, if you enter 16, it will say "It is True that 16 is even"
# num = int(input("enter a number: ") )
# print(f"it is {num % 2 == 0} that {num} is even")

# Write a program to print the square of 102. [Hint: use the exponent operator]
# num = 120
# square = num ** 2
# print(square)

# Write a program that checks whether the last digit in the variable x = 4732 is actually 6 [Hint: remember that doing x % 10 will give us back the last digit in x.]
# x = 4732
# last_digit = x % 10
# print(last_digit == 6)


# A program that takes the last three characters of a string, replicates it 4 times and checks whether that pattern is palindromic, not minding the case of the original string.
text = input("Enter text: ")
last_three = text[-3:]
replicate = last_three * 4
is_palindrome = replicate == text[::-1]
print(is_palindrome)