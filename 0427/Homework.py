from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 啟動 Chrome 瀏覽器
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # 打開 UNIQLO 官網
    driver.get("https://www.uniqlo.com/tw/zh_TW/")
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    print("✅ 網頁載入成功")

    # 點擊搜尋 icon
    search_icon = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon.icon-search"))
    )
    search_icon.click()
    print("✅ 搜尋 icon 點擊完成")

    # 等搜尋輸入欄位出現並可輸入（使用正確 class）
    search_box = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input.js-header-search-input"))
    )
    print("✅ 搜尋欄可輸入")

    # 輸入 airism 並送出
    search_box.send_keys("airism")
    search_box.send_keys(Keys.ENTER)
    print("✅ 已輸入並送出搜尋")

    # 等待搜尋結果出現
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-item")))
    print("✅ 搜尋結果已出現")

    # 擷取商品資訊
    products = driver.find_elements(By.CSS_SELECTOR, ".product-item")

    for i, item in enumerate(products, 1):
        try:
            title = item.find_element(By.CSS_SELECTOR, ".product-name").text
        except:
            title = "❌ 無法取得名稱"

        try:
            img = item.find_element(By.CSS_SELECTOR, "img").get_attribute("src")
        except:
            img = "❌ 無法取得圖片"

        print(f"{i}. {title}\n   圖片連結: {img}")

    time.sleep(3)

finally:
    driver.quit()