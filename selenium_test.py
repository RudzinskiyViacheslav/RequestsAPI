from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
import time

ua = UserAgent()
user_agent = ua.chrome

options = Options()
options.add_argument('--window-size=1400,1200')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--disable-extensions")
options.add_argument('--remote-debugging-port=9222')
options.add_argument('--enable-javascript')
options.add_argument('--no-sandbox')
options.add_argument("--allow-running-insecure-content")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-insecure-localhost')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; "
                     "x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'")
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

chrome_driver = webdriver.Chrome(options=options)
#chrome_driver.delete_cookie()
# chrome_driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
time.sleep(5)

chrome_driver.get('https://edadeal.ru/moskva/offers?q=%D0%B2%D0%BE%'
                  'D0%B4%D0%BA%D0%B0%200%2C5%20%D0%BB&retailer=winelab&sort=aprice')
time.sleep(5)

try:
    age_confirm_btn = chrome_driver.find_element(By.XPATH, "//div[@class='b-button b-button_disabled_false b-button_theme_default b-button_shape_default b-button_size_m b-button_justify_start b-button_selected_false b-offer__alco-action']")
    age_confirm_btn.click()
    print(age_confirm_btn)
except Exception as exp:
    print(exp)

vodka_names = chrome_driver.find_elements(By.XPATH, '//div[@class="b-offer__description"]')

# try:
#     vodka_names = chrome_driver.find_element(By.CLASS_NAME, "p-offers__header")
#     print(vodka_names)
# except Exception as exc:
#     print(exc)

vodka_prices_sale = chrome_driver.find_elements(By.XPATH, '//div[@class="b-offer__price-new"]')
print(vodka_prices_sale)

vodka_prices_normal = chrome_driver.find_elements(By.XPATH, '//div[@class="b-offer__price-old"]')
print(vodka_prices_normal)

list_vodkas_to_send_Bot = []

for i in range(len(vodka_names)):
    list_vodkas_to_send_Bot.append(f'{vodka_names[i].text} нынче по цене {vodka_prices_sale[i].text}, '
                                   f'а была {vodka_prices_normal[i].text}')
for item in list_vodkas_to_send_Bot:
    print(item)

# for item in vodka_names:
#     print(item.text)

chrome_driver.quit()