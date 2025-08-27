# Project Overview:
# Create a simple library management system where users can add, view, update, and delete 
# books in a file named `the_librarian.py`.


# Requirements:

# Data Storage: Use a list of dictionaries to store book information. Each book should have the following attributes:
# Title (string)
# Author (string)
# Year of publication (int)
# ISBN (string)
# Available (boolean)

# Functions/Actions:
# add_book(): Add a new book to the library.
# view_books(): Display all the books in the library.
# update_book(isbn): Update the information of a book given its ISBN.
# delete_book(isbn): Remove a book from the library using its ISBN.
# search_book(title): Search for a book by its exact title.
# borrow_book(isbn): Mark a book as borrowed (not available).
# return_book(isbn): Mark a book as returned (available).

# User Interface: Use a loop to display a menu and prompt the user for an action above until they choose to exit. Assume the user always inputs the correct data types.


book_list = []

def selection_options():
    print("""
    1. Add Book
    2. View Book
    3. Update Book
    4. Delete Book
    5. Search Book
    6. Borrow Book
    7. Return Book
    8. Exit

    Choose an option:
    """)

    option = int(input())

    if option not in [1, 2, 3, 4, 5, 6, 7, 8]:
        print("Invalid option")
        exit()
    
    if option == 1:
        add_book()
    elif option == 2:
        view_books()
    elif option == 3:
        isbn = input('Enter ISBN: ')
        update_book(isbn)
    elif option == 4:
        isbn = input('Enter ISBN: ')
        delete_book(isbn)
    elif option == 5:
        title = input("Enter book title: ")
        search_book(title)
    elif option == 6:
        print('Not available')
    elif option == 7:
        print('Available')            
    elif option == 8:
        print("Exiting the program...")
        exit()



def add_book():
    while True:
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = int(input("Enter year of pulication: "))
        isbn = input("Enter book ISBN:  ")


        book_dict = {"title": title, "author": author, "year": year, "isbn": isbn }

        book_list.append(book_dict)

        add_more_book = input('Do you want to add another book? yes/no: ')

        if add_more_book != 'yes':
            break
    selection_options() 


def view_books():
    if book_list == []:
        print(f'Sorry your library is empty ')
    else:
        for book in book_list:
            print(f"Title: {book['title']}\t\tAuthor: {book['author']}\t\tYear: {book['year']}\t\tISBN: {book['isbn']}")
        # selection_options()  

def update_book(isbn):

    user = None

    for book in book_list:
        if book['isbn'] == isbn:
            user = book
    
    if user is None:
        print('Book not found!!')
        selection_options()
    
    title = input('Enter the book title you would like to add(Leave empty if you dont want to change it): ')
    author = input("Enter the author's name (Leave empty if you dont want to change it ): ")
    year = input("Enter the year of  publication (Leave empty if you dont want to change it ): ")
    isbn = input("Enter ISBN (Leave empty if you dont want to change it ): ")


    if title.strip() != '':
        user['title'] = title
    
    if author.strip() != '':
        user['author'] = author

    if year.strip() != '':
        user['year'] = year

    if isbn.strip() != '':
        user['isbn'] = isbn        

    print("Book updated!")
    
    selection_options()   


def delete_book(isbn):
    for i in range(len(book_list)):
        if book_list[i]['isbn'] == isbn:
            delete_confirmation = input('Are you sure you want to delete this book?  yes/no: ')
            if delete_confirmation == 'yes':
                del book_list[i]
                print('Book deleted')
            selection_options()  


def search_book(title):
    for i in range(len(book_list)):
        if book_list[i]['title'] == title:
            print(book_list[i])
        else:
            print(f'Sorry book not found ')
    selection_options() 

# def borrow_book():
#     return ('Book not available') 
#     selection_options()

# def return_book():
#     return ('Available')
#     selection_options()                                                 





selection_options()