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
print(items)