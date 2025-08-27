import requests as req
from bs4 import BeautifulSoup

word = input('Enter word to search: ')

response = req.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}").json()


for line in response:
    for meaning in line['meanings']:
        for definition in meaning['definitions']:
            for partOfSpeech in meaning['partOfSpeech']:
                for definition in meaning['definitions']:
                     print(f"part of speech: {meaning['partOfSpeech']}  {definition['definition']}")




        

# Your assignment will be 

# interjection -> meaning
# E.g. example


# verb ->  


# url = 'https://www.example.com'  # You can change this to a URL of your choice
# response = req.get(url)

# if response.status_code == 200:
#     # Parse the content using Beautiful Soup
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Extract the header
#     header = soup.find('h1')
#     # print('Header is: ', header.get_text())

#     if header:
#         print('Header:', header.get_text())
        

# #     # Extract the main content (assuming main content is within <main> tag or similar)
#     main_content = soup.find('main')
    
# #     if main_content:
#         print('Main Content:', main_content.get_text())
#     else:
#         # Fallback: Extract all paragraphs as main content
#         paragraphs = soup.find_all('p')
#         for p in paragraphs:
#             print('Paragraph:', p.get_text())
# else:
#     print('Failed to retrieve the webpage. Status code:', response.status_code)

