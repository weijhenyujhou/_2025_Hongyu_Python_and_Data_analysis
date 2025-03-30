import urllib.request as req

url = 'https://www.ptt.cc/bbs/movie/index10546.html'
#如果遇到無法爬蟲的網頁確認 進入網頁程式原始碼底下的網路底下的index 增加header= user-agent資訊目的模擬人類在瀏覽網頁
request =req.Request(url,headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'})

with req.urlopen(request) as response:
    data = response.read().decode('utf-8')

#print(data)
#使用beautifulsoup4 package
import bs4
root =bs4.BeautifulSoup(data, 'html.parser')
#print(root)
#找出所有
print('=====爬出第一個標題====')
title = root.find('div',class_='title')
print(title.a.string)

# for a_tag in root.find_all('a', class_='right small'):
#     print(a_tag.string)

print('=====爬出所有標題====')
titles = root.find_all('div',class_='title')
for title in titles:
    print(title.a.string)

print('=====爬出所有日期====')
dates = root.find_all('div',class_='date')
for date in dates:
    print(date.a.string)

print('=====爬出所有評論值====')
spans = root.find_all('span',class_='hl')
for span in spans:
    print(span.string)
