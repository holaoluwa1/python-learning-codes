import requests as req
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'  # You can change this to a URL of your choice
response = req.get(url)

if response.status_code == 200:
    # Parse the content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all("article")
    prices = soup.find_all('p', class_='price_color')
    
    print('Total number of books: ', len(articles))
    
    # print(prices)
    total = []
    for price in prices:
        total.append(float(price.get_text()[1:]))
    print(sum(total))
    # for article in articles:
    #     print(article.find(''))
    
    print('avarage price:', sum(total) / len(articles))
    print(max(total))
        
