import requests
from bs4 import BeautifulSoup
import data

with requests.session() as s:
    r = s.post(data.login_url, data=data.payload)
    # print(r.text)
    # print(r.url)

    r2 = s.get(data.client_url)

    soup = BeautifulSoup(r2.text, 'lxml')
    print(soup.text)

    # soup0 = BeautifulSoup(r2.content, 'html.parser')
    # print(soup0.text)

    # soup1 = BeautifulSoup(r2.content.decode('utf-8'), 'html.parser')
    # print(soup1.text)
    # print('*********************************************')
    # soup2 = BeautifulSoup(r2.read().decode('utf-8'), 'html')
    # print(soup2.text)


# проблема: происходит выход, потеря доступа
