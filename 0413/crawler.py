import urllib.request as req

url = 'https://www.ptt.cc/bbs/gossiping/index.html'

header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'Cookie':'over18=1'
}

data = req.Request(url, headers=header)

with req.urlopen(data) as response:
    data = response.read().decode('utf-8')

import bs4
root =bs4.BeautifulSoup(data, 'html.parser')

print(root)