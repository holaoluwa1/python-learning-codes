# num1 = int(input('Enter number: '))
# num2 = int(input('Enter number: '))

# # sum_numbers = num1 + num2
# # print(sum_numbers)
# print(f'{num1} + {num2} = {num1 + num2} ')




data = {
    'name': "John Doe",
    'class': "Data Science",
    'dept': 'Computer Artificial Intelligence',
    'course': 'Intelligent Systems',
    'room': 'REC-123'
}

# you are to write a program that accepts a key from the user, and then try to delete that item from this our dict


print(""""section option
name:
class:
course:
room:    
""")

section = input("enter a option: ")


try:
    del data[section]
except:
    print("Key does not exist")
    exit()
print(data)
