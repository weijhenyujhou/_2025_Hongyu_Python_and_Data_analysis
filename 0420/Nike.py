from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Safari()
url_nike='https://www.nike.com/tw/w/mens-apparel-6ymx6znik1'
url_uniqlo='https://www.uniqlo.com/tw/zh_TW/c/all_men-ut-contents.html'
time.sleep(3)
driver.get(url_uniqlo)


#titles = driver.find_elements(By.CLASS_NAME,'product-card__title') # 樹狀
titles = driver.find_elements(By.CLASS_NAME,'product-description') # 樹狀
for title in titles:
    print(title.text)