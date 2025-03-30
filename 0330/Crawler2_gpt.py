import urllib.request as req
import bs4

url = 'https://www.ptt.cc/bbs/movie/index10546.html'

# 設定 User-Agent 模擬真實瀏覽器
request = req.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
})

# 讀取網頁內容
with req.urlopen(request) as response:
    data = response.read().decode('utf-8')

# 解析 HTML
root = bs4.BeautifulSoup(data, 'html.parser')

print('===== 爬出第一個標題 =====')
first_title = root.find('div', class_='title')
if first_title and first_title.a:
    print(first_title.a.string.strip())
else:
    print("標題不存在")

print('===== 爬出所有標題 =====')
titles = root.find_all('div', class_='title')
for title in titles:
    if title.a:
        print(title.a.string.strip())
    else:
        print("標題不存在")

print('===== 爬出所有日期 =====')
dates = root.find_all('div', class_='date')
for date in dates:
    print(date.get_text(strip=True))  # 確保不會報錯

print('===== 爬出所有評論值 =====')
spans = root.find_all('span', class_='hl')
for span in spans:
    print(span.get_text(strip=True))  # 避免 None

#將爬蟲回來資料整列顯示 r-ent這個標籤內包含整個標題下的資料

items = root.find_all('div', class_='r-ent')
for item in items:
    title = item.find('div', class_='title')
    date = item.find('div', class_='date')
    span = item.find('span', class_='hl')
    author = item.find('div', class_='author')

    # 檢查標題是否存在
    if title.a:  # 確保 <a> 存在
        title_text = title.a.string.strip()
    else:
        title_text = "文章已被刪除"

    # 檢查人氣（推文數）是否存在
    span_text = span.string.strip() if span else "0"

    # 檢查日期是否存在
    date_text = date.get_text(strip=True) if date else "未知日期"

    # 檢查作者是否存在
    author_text = author.get_text(strip=True) if author else "未知作者"

    # 輸出結果
    print(f'人氣：{span_text} | 標題：{title_text} | 日期：{date_text} ----- 作者：{author_text}')