from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Safari()
url ='https://www.books.com.tw/?loc=tw_logo_001' # 博客來
driver.get(url)
time.sleep(2)
# driver.save_screenshot('screenshot.jpg')
search = driver.find_element(By.CLASS_NAME,'search_key')
search.send_keys('python')
# search.send_keys('餐')
# time.sleep(3)
search.send_keys(Keys.ENTER)
time.sleep(10)
