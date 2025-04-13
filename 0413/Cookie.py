#urllib method to crawler （不可以下載第三方套件的時候做法）

import urllib.request as req

url = 'https://www.ptt.cc/bbs/gossiping/index.html'

#模擬是一個成年(over18)人類在瀏覽網頁
header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'Cookie':'over18=1'
}

# data = req.Request(url, headers=header)
#
# with req.urlopen(data) as response:
#     data = response.read().decode('utf-8')
#
# import bs4
# root =bs4.BeautifulSoup(data, 'html.parser')
# items = root.find_all('div', class_='r-ent')
# print(items)


#request method to crawler

import  requests

data = requests.get(url,headers= header)
data = data.text
import bs4
root =bs4.BeautifulSoup(data, 'html.parser')
items = root.find_all('div', class_='r-ent')
for item in items:
    title = item.find('div', class_='title')
    date = item.find('div', class_='date')
    span = item.find('span', class_='hl')
    author = item.find('div', class_='author')
    # 加入判斷條件文章已被刪除
    if title.a is None:
        title = '本文已刪除'
    else:
        title = title.a.string
    # 避免遇到文章熱度為空值
    if span is None:
        span = '0'

    else:
        span = span.string
    print(f'熱度：{span:<4}/標題：{title:40}/日期：{date.string:20}------作者：{author.string:20}')
# print(items)