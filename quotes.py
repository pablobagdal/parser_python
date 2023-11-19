import requests
from bs4 import BeautifulSoup


url = 'https://quotes.toscrape.com/'
responce = requests.get(url)
soup = BeautifulSoup(responce.text, 'lxml')
quotes = soup.find_all(name='span', class_='text')
# print(quotes)

# tags = soup.find_all(name='a', class_='tag')
# print(tags)


# ls = []
# for quote in quotes:
#     ls.append(quote.text.replace("“", '').replace("”", ''))

# print(ls)
