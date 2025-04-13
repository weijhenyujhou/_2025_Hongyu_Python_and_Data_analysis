# 使用request模組
import requests #request 為第三方軟體需要在終端機先安裝 pip install requests
# request method: 資料交換：get, post, 刪除：delete, 更新：put, patch
url = 'https://www.ptt.cc/bbs/gossiping/index.html'

data = requests.get(url)
data = data.text
print(data)