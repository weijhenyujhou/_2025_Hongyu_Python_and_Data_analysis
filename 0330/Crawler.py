import urllib.request as req

url = 'https://tw.yahoo.com'
request =req.Request(url,headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'})

with req.urlopen(request) as response:
    data = response.read().decode('utf-8')

print(data)