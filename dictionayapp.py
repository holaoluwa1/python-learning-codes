import requests as req
from bs4 import BeautifulSoup




# response = req.get("https://gooogle.com")
# print(response.content)

# response = req.get("https://jsonplaceholder.typicode.com/users").json()
# for user in response:   
#     print(user["username"])



response = req.get("https://books.toscrap.com")
print(response)