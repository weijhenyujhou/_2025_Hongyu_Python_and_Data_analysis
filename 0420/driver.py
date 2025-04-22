from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 手動指定 chromium binary 路徑（根據你實際安裝）
chrome_options.binary_location = "/opt/chromium/chrome"

service = Service("/usr/local/bin/chromedriver")  # 驅動程式路徑
driver = webdriver.Chrome(service=service, options=chrome_options)
