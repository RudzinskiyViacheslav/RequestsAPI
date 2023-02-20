import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options


#age_verification_banner = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "age-verification-banner")]')))
#age_verification_banner.find_element_by_xpath('//button[contains(text(), "ПОДТВЕРДИТЬ И ВОЙТИ")]').click()

url = 'https://github.com/eeroshkin/bot'
url_winelab_vodka = 'https://krasnoeibeloe.ru/'

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')

browser = webdriver.Chrome(options=chrome_options)
browser.get(url_winelab_vodka)

time.sleep(5)
try:
    age_confirm_btn = browser.find_element(By.CLASS_NAME, 'age_popup_btn--agree')
    age_confirm_btn.click()
    print(age_confirm_btn)
except Exception:
    print('Ну проверки на возраст нет. Збс')
time.sleep(5)
browser.get('https://krasnoeibeloe.ru/catalog/?q=Tundra')

tundras = browser.find_elements(By.CLASS_NAME, 'i_price')

for item in tundras:
    print(item.text)

browser.quit()

# response = requests.get(url_winelab_vodka)
#
# content = response.text
#
# soup = BeautifulSoup(content, 'html.parser')
#
# info = soup.find('div', class_='Details-content--hidden-not-important '
#                                'js-navigation-container js-active-navigation-container d-md-block')
#
# info2 = soup.find_all('div', class_='Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item')
# info3 = soup.find_all('div', class_='flex-auto min-width-0 col-md-2 mr-3')
# soup_find = soup.find_all('div', class_=' col-12 col-sm-6 col-md-6 col-lg-4')
#
# if response.status_code == 200:
#     print(f'Подключение в норме и установлено с кодом {response.status_code}')
# else:
#     print(f'Подключение НЕ установлено. Код: {response.status_code}')
# # print(soup)
# print(soup_find)
#
# # for item in info3:
# #     print(item.text.strip())
