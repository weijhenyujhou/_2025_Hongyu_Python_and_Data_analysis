import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

# import openpyxl
#
# wb = openpyxl.Workbook()
# ws = wb.active
# title = ['產品名稱', '價格']
# ws.append(title)

url_nike='https://www.uniqlo.com/tw/zh_TW/'
driver = webdriver.Safari()
driver.get(url_nike)
time.sleep(3)

#點選搜尋按鈕
search_button = driver.find_element(By.CSS_SELECTOR,'.icon.icon-search')
search_button.click()
time.sleep(5)

search_input = driver.find_element(By.CLASS_NAME,'text')
search_input.send_keys('airism')
search_input.send_keys(Keys.ENTER)
time.sleep(5)

# info = driver.find_elements(By.CLASS_NAME,'product-card__info')
#
# time.sleep(4)
# for item in info:
#     title = item.find_element(By.CLASS_NAME,'product-card__titles').text
#     price = item.find_element(By.CLASS_NAME,'product-card__price').text
#     items = title,price
#     ws.append(items)
#     #print(f'{title}:{price}')
# wb.save('Nikeproducts.xlsx')

