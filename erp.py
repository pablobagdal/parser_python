import requests
from bs4 import BeautifulSoup
import time
import data


r = requests.post(data.login_url, data=data.payload)

print(r.text)

# r2 = requests.get(client_url)

# print(r2.text)

# проблема: происходит выход, потеря доступа
