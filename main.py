import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://github.com/eeroshkin/bot'
url_winelab_vodka = 'https://www.winelab.ru/catalog/krepkiy-alkogol-vodka/cp_0.5?sort=price-asc'
response = requests.get(url_winelab_vodka)

content = response.text

soup = BeautifulSoup(content, 'html.parser')

info = soup.find('div', class_='Details-content--hidden-not-important '
                                   'js-navigation-container js-active-navigation-container d-md-block')

info2 = soup.find_all('div', class_='Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item')
info3 = soup.find_all('div', class_='flex-auto min-width-0 col-md-2 mr-3')
soup_find = soup.find_all('div', class_=' col-12 col-sm-6 col-md-6 col-lg-4')


if response.status_code == 200:
    print(f'Подключение в норме и установлено с кодом {response.status_code}')
else:
    print(f'Подключение НЕ установлено. Код: {response.status_code}')
#print(soup)
print(soup_find)

# for item in info3:
#     print(item.text.strip())