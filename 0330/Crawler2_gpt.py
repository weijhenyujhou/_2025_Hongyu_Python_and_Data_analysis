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

#抓出網頁內的值

for item in root.find_all('div', class_='r-ent'):
    title = item.find('div', class_='title')
    date = item.find('div', class_='date')
    span = item.find('span', class_='hl')
    author = item.find('div', class_='author')

    title_text = title.a.string.strip() if title.a else "本文已刪除"
    print(f'熱度：{span.string.strip() if span else "0":<4} | 標題：{title_text[:40]:40} | 日期：{date.get_text(strip=True) if date else "未知"} | 作者：{author.get_text(strip=True) if author else "未知"}')