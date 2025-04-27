from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 開啟網站
driver = webdriver.Chrome()
driver.get("https://www.uniqlo.com/tw/zh_TW/men.html")

# 點擊搜尋 icon（右上放大鏡）
search_icon = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon.icon-search-grey"))
)
search_icon.click()

# 等待輸入框出現
search_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"][placeholder="請輸入關鍵字"]'))
)

# 輸入關鍵字並送出
search_input.send_keys("airism")
search_input.submit()  # 或用 Keys.ENTER