import re

# with open('reviews.txt', 'r') as file:
#     content = file.read()
# #  format: username@domain.tld
#     pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'


#     email_list = re.findall(pattern, content)

#     pattern_phone_number = r'\+234\s\d{3}\s\d{3}\s\d{4}'
#     phonenumber_list = re.findall(pattern_phone_number, content)

#     with open('emails.txt', 'w') as emails_file:
#         for email in email_list:
#             emails_file.write(f'{email} \n')

#     with open('phonenumbers.txt', 'w') as phonenumber_file:
#         for phone in phonenumber_list:
#             phonenumber_file.write(f'{phone} \n')   


# verve_card = input("enter your digits: ")
# pattern = r'(506|650)\d{12,15}'
# if re.match(pattern, verve_card):
#     print("Your card is valid")
# else:
#     print("You enter an invalid card")  




# mastercard = input("enter your card digits: ")
# pattern = r'(51|52|53|54|55|221|2720)\d{12,15}'
# if re.match(pattern, mastercard):
#     print("your card is valid")
# else:
#     print("you enter an invlid card")


# visacard = input("enter your card digits: ")
# pattern = r'4\d{12}(\d{3})?'
# if re.match(pattern, visacard):
#     print("your card in valid")
# else:
#     print("you enter an invlid card")    


# phone_number = input("emter your phone number: ")
# pattern = r'\+?\d{1,3}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}'
# if re.match(pattern, phone_number):
#     print('your phone number is valid')
# else:
#     print("you enter as wrong number")  

      

# password = input("enter your password: ")
# pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}'
# if re.match(pattern, password):
#     print('valid password')
# else:
#     print("invalid password")          






