from time import process_time_ns
from traceback import print_tb

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Safari()
url_tenlogn='https://www.tenlong.com.tw'
url_momo= 'https://www.momoshop.com.tw/main/Main.jsp'
url_nike=''
time.sleep(3)
driver.get(url_momo)

#
titles = driver.find_elements(By.CSS_SELECTOR,'#menuList a') # 樹狀
#titles = driver.find_elements(By.CSS_SELECTOR,'.keywords-list a') # 樹狀
for title in titles:
    print(title.text)
#
# kw = driver.find_element(By.ID,'keyword')
# kw.send_keys('python')
# time.sleep(5)

# print(titles.text)

