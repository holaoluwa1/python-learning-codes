import re

with open('reviews.txt', 'r') as file:
    content = file.read()
#  format: username@domain.tld
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'


    email_list = re.findall(pattern, content)

    pattern_phone_number = r'\+234\s\d{3}\s\d{3}\s\d{4}'
    phonenumber_list = re.findall(pattern_phone_number, content)

    with open('emails.txt', 'w') as emails_file:
        for email in email_list:
            emails_file.write(f'{email} \n')

    with open('phonenumbers.txt', 'w') as phonenumber_file:
        for phone in phonenumber_list:
            phonenumber_file.write(f'{phone} \n')   


