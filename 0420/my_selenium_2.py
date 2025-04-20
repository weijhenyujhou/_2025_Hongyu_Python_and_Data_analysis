from time import process_time_ns
from traceback import print_tb

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Safari()
url='https://www.uniqlo.com/tw/zh_TW/c/all_men-outer-casual.html'
time.sleep(3)
driver.get(url)


titles = driver.find_elements(By.CLASS_NAME,'ec-font-sub-title mt-4')
for title in titles:
    print(title)