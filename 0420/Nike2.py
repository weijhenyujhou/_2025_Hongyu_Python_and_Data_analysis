import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
title = ['產品名稱', '價格']
ws.append(title)

url_nike='https://www.nike.com/tw/'
driver = webdriver.Safari()
driver.get(url_nike)
# 機器人自動選取進入男款>鞋款頁面抓取資料
#將機器人開啟網頁時對大化畫面，避免要點選的資料名有顯示造成程式錯誤
driver.maximize_window()
time.sleep(3)
link = driver.find_element(By.LINK_TEXT,'男款')
link.click()

link2 = driver.find_element(By.LINK_TEXT,'鞋款')
link2.click()

time.sleep(3)

info = driver.find_elements(By.CLASS_NAME,'product-card__info')

time.sleep(4)
for item in info:
    title = item.find_element(By.CLASS_NAME,'product-card__titles').text
    price = item.find_element(By.CLASS_NAME,'product-card__price').text
    items = title,price
    ws.append(items)
    #print(f'{title}:{price}')
wb.save('Nikeproducts.xlsx')



