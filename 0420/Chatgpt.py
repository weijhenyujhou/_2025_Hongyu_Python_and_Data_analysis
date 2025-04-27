from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
import time

# 啟動瀏覽器
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')  # 視窗最大化
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 前往 UNIQLO 台灣網站（可改成你想爬的地區）
driver.get("https://www.uniqlo.com/tw/")

# 找到搜尋按鈕（通常在右上角）
search_icon = driver.find_element(By.CLASS_NAME, "header-search--icon")
search_icon.click()
time.sleep(1)

# 找到搜尋輸入框並輸入關鍵字 "airsim"
search_input = driver.find_element(By.NAME, "q")  # 通常搜尋欄會有 name="q"
search_input.send_keys("airsim")
search_input.send_keys(Keys.RETURN)
time.sleep(3)  # 等待網頁載入搜尋結果

# 抓取搜尋結果（根據實際網頁結構調整）
product_elements = driver.find_elements(By.CLASS_NAME, "product-item__name")

print("搜尋結果：")
for product in product_elements:
    try:
        title = product.text
        link = product.find_element(By.XPATH, "..").get_attribute("href")
        print(f"{title} - {link}")
    except:
        continue

# 關閉瀏覽器
driver.quit()