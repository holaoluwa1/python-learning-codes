# Create a simple phone book manager where users can add, view, update, and delete contactsin a file named `phone_book.py`


contact_list = []

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
        add_contact()
    elif option == 2:
        view_contact()
    elif option == 3:
        phone = input('Enter phone no: ')
        update_contact(phone)
    elif option == 4:
        phone = input('Enter phone no: ')
        delete_contact(phone)
    elif option == 5:
        print("Exiting the program...")
        exit()


def add_contact():
    while True:
        name = input("Enter contact name: ")
        phone = input("Enter contact number: ")

        contact_dict = {"name": name, "phone": phone}

        contact_list.append(contact_dict)

        add_more_contact = input('Do you want to add another contact? y/n: ')

        if add_more_contact != 'y':
            break
    selection_options()


def view_contact():
    if contact_list == []:
        print('Your contact list is empty')
    else:
        for contact in contact_list:
            print(f"Name: {contact['name']}\t\tPhone No: {contact['phone']}")
        selection_options()
  



def update_contact(phone):

    user = None

    for contact in contact_list:
        if contact['phone'] == phone:
            user = contact
    
    if user is None:
        print('Contact not found!!')
        selection_options()
    
    name = input('Enter new name for contact (Leave empty if you dont want to change it): ')
    phone = input('Enter new phone number for contact (Leave empty if you dont want to change it ): ')

    if name.strip() != '':
        user['name'] = name
    
    if phone.strip() != '':
        user['phone'] = phone

    print("Contact updated!")
    
    selection_options()


def delete_contact(phone):
    for i in range(len(contact_list)):
        if contact_list[i]['phone'] == phone:
            delete_confirmation = input('Are you sure you want to delete this contain?  yes/no: ')
            if delete_confirmation == 'yes':
                del contact_list[i]
                print('Contact deleted')
                selection_options()            



    
























selection_options()
