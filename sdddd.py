def selection_options():
    print("""
    1. Add Contact
    2. View Contact
    3. Update contact
    4. Delete contact
    5. Exit

    Choose an option:
    """)

    option = int(input())

    if option not in [1, 2, 3, 4, 5]:
        print("Invalid option")
        exit()
    
    if option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    elif option == 5:
        print("Exiting the program...")
        exit()