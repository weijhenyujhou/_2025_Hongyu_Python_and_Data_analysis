from openpyxl.styles.builtins import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
title = ['產品名稱', '價格']
ws.append(title)

driver = webdriver.Safari()
url_nike='https://www.nike.com/tw/w/mens-shoes-nik1zy7ok'
#url_uniqlo='https://www.uniqlo.com/tw/zh_TW/c/all_men-ut-contents.html'
driver.get(url_nike)

#模擬人員滾動網頁
# n = 0
# while n <3: #設定滾動次數
#     #網頁滾動
#     driver.execute_script('window.scrollTo(0,document.body.scrollHeight - 1000)') # 每次滾動距離設定
#     time.sleep(3) #滾動後等待一段時間產品資料載出
#     n +=1
#     #等待資料三秒後資料載入
#
#     #資料寫入
#     titles = driver.find_elements(By.CLASS_NAME,'product-card__title') # 樹狀
        #titles = driver.find_elements(By.CSS_SELECTOR,'.roduct-card__title')
#titles = driver.find_elements(By.CLASS_NAME,'product-content product-content-V') # 樹狀
info = driver.find_elements(By.CLASS_NAME,'product-card__info')

time.sleep(3)

for item in info:
    title = item.find_element(By.CLASS_NAME,'product-card__titles').text
    price = item.find_element(By.CLASS_NAME,'product-card__price').text
    items = title,price
    ws.append(items)
    #print(f'{title}:{price}')
wb.save('Nikeproducts.xlsx')