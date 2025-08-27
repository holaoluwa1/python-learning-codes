# Create a dictionary called `student` with keys "name", "age", and "grade", and 
# corresponding values "John", 20, and "A". Access and print the value of "name".

# student = {"name": "john",
#             "age":  20,
#           "grade":  "A"    
# }
# print(student["name"])
# Create a dictionary called `product` with keys "name", "price", and "stock", and 
# corresponding values "Laptop", 999.99, and 50. Change the value of "price" to 899.99.

# product = {"name": "laptop",
#            "price": 999.99,
#            "stock": 50

# }
# product['price'] = 899.99
# print(product["price"])
# Create a dictionary called `employee` with keys "name" and "position", and corresponding values "Alice" and "Manager". Add a new key "salary" with the value 50000.
# employee ={"name": "alice",
#           "position": "manager", 'salary' : 59000
# }
# employee["salary"] = 5000
# print('The updated employee data is: ', employee)
# Create a dictionary called `inventory` with keys "apple", "banana", and "orange", and values 10, 5, and 8 respectively. Remove the key "banana".
# inventory = {"apple": 10,
# "banana": 5,
# "orange": 8

# }
# del inventory["banana"]
# print(inventory)
# Create a dictionary called person with keys "name", "age", and "city", and corresponding values "Bob", 25, and "New York". Use the copy() method to make a copy of the dictionary and call it person_copy.
# person = {"name": "bob",
# "age": 25,
# "city": "new york"
# }
# person_copy = person.copy()
# print(person_copy)
# Create a nested dictionary called `family` with keys "child1", "child2", and "child3", each containing a dictionary with keys "name" and "age" with appropriate values. Access and print the age of "child2".
# family = {"child1": 

# }
# Create a dictionary called `car` with keys "brand", "model", and "year", and corresponding values "Toyota", "Corolla", and 2020. Access and print the value of "model".
# car = {"brand": "toyota",
# "model": "corolla",
# "year": 2020

# }
# print(car['model'])
# Create a dictionary called `settings` with keys "volume", "brightness", and "language", and corresponding values 50, 75, and "English". Change the "language" to "Spanish".
# settings = {"volume": 50,
# "brightness": 75,
# "language": "english"

# }
# settings["language"] = "spanish"
# print(settings)
# Create a dictionary called `scores` with keys "math", "science", and "english", and corresponding values 90, 85, and 88. Remove the key "science".
# scores = {"math": 90,
# "science": 85,
# "english": 88

# }
# del scores['science']
# print(scores)
# Create a dictionary called `menu` with keys "starter", "main_course", and "dessert", and corresponding values "Soup", "Steak", and "Ice Cream". Check if the key "appetizer"
# menu = {"starter": "soup",
# "main_course": "steak",
# "dessert": "ice cream"

# }
# key = "appetizer"
# print(f'it is {key in menu} {key} is present in the dictionary. ')

# Create a dictionary called `config` with keys "theme", "language", and "timezone", and corresponding values "dark", "English", and "UTC". Clear the dictionary.
# config = {"theme": "dark",
# "language": "english",
# "timezone": "utc"
# }
# config.clear()
# print(config)
# Create a dictionary called `phone_book` with keys "Alice", "Bob", and 
# "Charlie", and corresponding phone numbers as values. Print the number of 
# items in the dictionary.
# phone_book = {"alice": 234583844438,
# "bob": 23459784889,
# "charlie": 23457484843

# }
# print(len(phone_book))
#  13. Create a dictionary called `grades` with keys "math", "science", and "history", 
# and corresponding values "A", "B", and "C". Get a LIST of all the keys in the 
# dictionary.
# grade = {"math": "A",
# "science": "B",
# "history": "C"

# }
# print(grade.items())
#  14. 	Create a dictionary called `employee` with keys "name", "position", and 
# "salary", and corresponding values "David", "Engineer", and 70000. Get a LIST 
# of all the values in the dictionary
# employee = {"name": "david",
# "position": "engineer",
# "salary": 7000

# }
# print(list(employee.values()) )
#  15. 	Create a dictionary called `game` with keys "title", "genre", and "rating", and 
# corresponding values "Minecraft", "Sandbox", and 4.5. Get a LIST of all 
# key-value pairs in the dictionary.
# game = {"tittle": "minecraft",
# "genre": "sandbox",
# "rating": 4.5


# }
# print(game.keys())








# Access and print the second subject of the first person in the list.
# data = [
#     ["Alice", 25, ["Math", "Physics"]],
#     ["Bob", 30, ["Chemistry", "Biology"]],
#     ["Charlie", 35, ["History", "Geography"]]
# ]
# print(data[0][2][1])
# Access and print the first value in the list of numbers associated with "San Francisco".
# records = [
#     ["New York", [10, 20, 30]],
#     ["San Francisco", [40, 50, 60]],
#     ["Austin", [70, 80, 90]]
# ]
# print(records[1][1][0])
# Get the first e in Ayo’s gender and Get Ben’s age.
# group = [
#     ["Ayo", ["Female", 12]],
#     ["Ben", ["Male", 9]]
# ]
# ayo_gender = group[0][1]
# first_e = ayo_gender[0]
# print(first_e[1])
# print(group[1][1][1])
# Get the l in Nina’s gender and Get Tobi’s age
# records = [
#     ["Tobi", ["Male", [6]]],
#     ["Nina", ["Female", [7]]]
# ]
# Ninas_gender = records[1][1]
# first_l = Ninas_gender[0]
# print(first_l[-2])
# print(records[0][1][1])
# Get the two oo’s in X1’s 2nd mobility status (loose) together (slicing) and Get the battery percentage of R2
# robot_grid = [
#     ["R2", ["battery", [98]]],
#     ["R5", ["status", "active"]],
#     ["X1", [["joint", "loose"], "error"]]
# ]

# Get the Five in the Jazz song title and Get the duration of the Jazz song
# playlist = [
#     ["Jazz", ["Take Five", 5.24]],
#     ["Pop", ["Blinding Lights", 3.20]],
#     ["Rock", ["Bohemian Rhapsody", 5.55]]
# ]
# five_duration = playlist[0][1]
# print(five_duration[0][5:])
# print(five_duration[1])
# Get the letter v in Tiger’s category and Get the first letter of the Frog’s type
# animals = [
#     ["Elephant", ["Herbivore"]],
#     ["Tiger", ["Carnivore"]],
#     ["Frog", ["Amphibian"]]
# ]
# v_tiger = animals[1][1]
# print(v_tiger[0][-4])
# first_letter_of_frog = animals[2][1]
# print(first_letter_of_frog[0][0])


# Access and print the name of the teacher of "class2".
school = {
    "class1": {
        "students": ["Alice", "Bob"],
        "teacher": "Mr. Smith"
    },
    "class2": {
        "students": ["Charlie", "David"],
        "teacher": "Ms. Johnson"
    }
}
print(school['class2']['teacher'])
# Access and print the second employee in the "Engineering" department.
company = {
    "HR": ["Alice", "Bob"],
    "Engineering": ["Charlie", "David"]
}
Engineering = company['Engineering'][1]
print(Engineering)
# Access and print the name of the second assistant.
university = {
    "faculty": {
        "professors": ["Dr. Smith", "Dr. Brown"],
        "assistants": ["Ms. Green", "Mr. White"]
    },
    "students": ["John", "Jane", "Alice", "Bob"]
}
assistant = university["faculty"]["assistants"][1]
print(assistant)
# Access and print the price of the third fruit.
store = {
    "fruits": [
        {"name": "apple", "price": 0.5},
        {"name": "banana", "price": 0.2},
        {"name": "cherry", "price": 1.5}
    ],
    "vegetables": [
        {"name": "carrot", "price": 0.3},
        {"name": "lettuce", "price": 1.0},
        {"name": "onion", "price": 0.4}
    ]
}
price_of_third = store['fruits'][2]['price']
print(price_of_third)
# Access and print the second non-fiction book.
library = {
"fiction": ["1984", "To Kill a Mockingbird", "The Great Gatsby"],
"non_fiction": ["Sapiens", "Educated", "The Wright Brothers"]
}
print(library['non_fiction'][1])
# Access and print the age of the first child.
family = {
    "parents": ["John", "Jane"],
    "children": [
        {"name": "Tom", "age": 5},
        {"name": "Lucy", "age": 8}
    ]
}
print(family['children'][0]['age'])
# Access and print the name of the second main course.
restaurant = {
    "menu": {
        "appetizers": ["soup", "salad"],
        "main_courses": ["steak", "pasta"],
        "desserts": ["cake", "ice cream"]
    },
    "staff": ["Chef A", "Chef B", "Waiter X", "Waiter Y"]
}
print(restaurant['menu']['main_courses'][1])
# Access and print the department of the user of the first desk.
workspace = {
    "desks": [
        {"user": "Alice", "department": "HR"},
        {"user": "Bob", "department": "Engineering"}
    ],
    "equipment": {"computers": 20, "printers": 10}
}
print(workspace['desks'][1]['department'])
# Access and print the name of the second designer.
team = {
    "developers": ["Dev A", "Dev B"],
    "designers": ["Designer X", "Designer Y"],
    "projects": ["Project 1", "Project 2"]
}
print(team['designers'][1])
# Access and print the second international destination.
travel = {"domestic": ["Boston", "Chicago"], "international": ["Paris", "Tokyo"], "expenses": 
{"flights": 1500, "hotels": 2000}}
print(travel['international'][1])

