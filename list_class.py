players = ['saka', 'rashford', 'raya', 'timber', 'saliba', ]

shopping_list = ["Bournvita", "Buredi Oyo", "Noodles", 'Eva soap', 'Toothpaste']
shopping_list_quantity = [30, 120, 3, 10, 12]

print('********************* SHOPPING LIST ******************')
print('******************************************************')

print(f"{shopping_list[0]} ---> {shopping_list_quantity[0]}")
print(f"{shopping_list[1]} ---> {shopping_list_quantity[1]}")

shopping_list[2] = "meatpie"
print(f"{shopping_list[2]} ---> {shopping_list_quantity[2]}")
print(f"{shopping_list[3]} ---> {shopping_list_quantity[3]}")
print(f"{shopping_list[4]} ---> {shopping_list_quantity[4]}")


print(shopping_list)

print(f"it is {'meatpie' in shopping_list } meatpie is in {shopping_list} " )


# Create a list called fruits with items "apple", "banana", and "orange". Print the first item.
list_of_fruit = ['apple', 'banana', 'orange', ]
print(list_of_fruit[0])
# Create a list called colors with items "red", "green", "blue". Print the last item using negative indexing.
colour = ['red', 'green', 'blue' ]
print(colour[-1])
# Create a list called numbers with items from 1 to 10. Print items from index 3 to index 7.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3:8])
# Create a list called alphabets with items "a", "b", "c", ..., "z". Print a slice from index -3 to the end.
import string
alphabets = list(string.ascii_lowercase)
print(alphabets[-3:])

# Create a list called ages with items 20, 30, 40. Change the value of the second item to 35.
ages = [20, 30, 40]
ages[1] = 35
print(ages)
# Create a list called grades with items "A", "B", "C", "D". Change the values of items from index 1 to index 3 to "X".
grades = ['A', 'B', 'C', 'D']
grades[1 : 3] = ['x', 'x'] 
print(grades)
# Create a list called cities with items "New York", "London", "Paris". Insert "Tokyo" at the beginning of the list.
cities = ["New York", "London", "Paris"]
cities.insert(0, 'Tokyo')
print(cities)
# Create a list called fruits with items "apple", "banana", "cherry". Print the number of items in the list.
fruits = ["apple", "banana", "cherry"]
print(len(fruits) )
# Create a list called prices with items 10.5, 20.0, 15.75. Print the data type of the list.
prices = [10.5, 20.0, 15.75]
print(type(prices) )
# Create a list called mixed with items 10, "apple", True. Print the list.
mixed = [10, 'apple', True]
print(mixed)
# Create a tuple called tuple_data with items "a", "b", "c". Convert the tuple into a list.

# Create a list called books with items "Python", "Java". Append "JavaScript" to the end of the list.
books = ["Python", "Java"]
books.append('JavaScript') 
print(books)
# Create a list called names with items "Alice", "Bob", "Eve". Insert "Charlie" at index 1.
names = ["Alice", "Bob", "Eve"]
names.insert(1,"Charlie" )
print(names)
# Create two lists called list1 and list2 with items 1, 2, 3 and 4, 5, 6 respectively. Extend list1 with list2.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)
# Create a list called students with items "Alice", "Bob". Add items from a tuple ("Charlie", "David") to students.
students = ["Alice", "Bob"]
# Create a list called colors with items "red", "green", "blue". Remove "green" from the list.
colors = ["red", "green", "blue"]
colors.remove('green')
print(colors)
# Create a list called numbers with items 10, 20, 30, 40. Use the del keyword to remove the item at index 2.
numbers = [10, 20, 30, 40]
del numbers[2]
print(numbers)

# Create a list called fruits with items "apple", "banana", "cherry". Clear the list.
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)
# Create a list called names with items "Zoe", "Alice", "Bob". Sort the list alphabetically.
names= ["Zoe", "Alice", "Bob"]
names.sort()
print(names)
#  Create a list called ages with items 25, 35, 20. Sort the list in descending order.
ages = [25, 35, 20]
ages.sort(reverse=True)
print(ages)
#  Sorting lists is CASE-SENSITIVE by default. Create a list called words with items 
# "Apple", "banana", "Orange". Sort the list in CASE-INSENSITIVE alphabetical order.
words = ["Apple", "banana", "Orange"]
words.sort(key=str.lower)
print(words)
#  Create a list called numbers with items 1, 2, 3, 4. Print the list in reverse order.
items = [1, 2, 3, 4]
items.reverse()
print(items)
#  Create a list called letters with items "a", "b", "c", "d". Print the list in reverse order using slicing.
items = ["a", "b", "c", "d"]
# reserve_items = items[::-1]
# print(reserve_items)
print(items[::-1])


#  Create a list called original with items "one", "two", "three". Create a copy of the list.
items = ["one", "two", "three"]
new_items = items.copy()
print(new_items)
#  Create two lists called list1 with items "a", "b" and list2 with items "c", "d". Join list1 and  list2 together.
list1 = ["a", "b"]
list2 = ["c", "d"]
list1.extend(list2)
print(list1)



