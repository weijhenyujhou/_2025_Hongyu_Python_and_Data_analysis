import urllib.request as req

url = 'https://tw.yahoo.com'
#如果遇到無法爬蟲的網頁確認 進入網頁程式原始碼底下的網路底下的index 增加header= user-agent資訊
request =req.Request(url,headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'})

with req.urlopen(request) as response:
    data = response.read().decode('utf-8')

print(data)