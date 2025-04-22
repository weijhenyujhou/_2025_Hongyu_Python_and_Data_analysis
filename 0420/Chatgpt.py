from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# 設定 Chrome 啟動選項
options = Options()
options.add_argument("--headless")  # 無頭模式
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# 這邊根據你的系統調整 chromedriver 路徑
service = Service("/usr/local/bin/chromedriver")

# 啟動 driver
driver = webdriver.Chrome(service=service, options=options)

# UNIQLO 男裝短踢頁面
url = "https://www.uniqlo.com/jp/ja/men/tops/t-shirts"
driver.get(url)

# 等 JavaScript 載入（可視情況調整等待時間）
time.sleep(5)

# 取得渲染後的 HTML
soup = BeautifulSoup(driver.page_source, "html.parser")

# 抓商品區塊
products = soup.select("a[data-test='product-card-link']")

# 印出商品名稱與連結
for product in products:
    title = product.get("aria-label") or product.get_text(strip=True)
    link = "https://www.uniqlo.com" + product.get("href")
    print(f"{title} - {link}")

driver.quit()
