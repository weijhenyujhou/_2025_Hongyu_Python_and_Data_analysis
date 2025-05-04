from selenium import webdriver  #登入網頁
import os #開啟資料夾
import requests #取得圖片
from bs4 import BeautifulSoup #取得元素 可以實際看到網頁元素,使用driver.find.elementes 較不易閱讀

url_nike = 'https://www.nike.com/tw/'
url_books = 'https://www.books.com.tw'
url_momo ='https://www.momoshop.com.tw/main/Main.jsp'
url_uniqlo = 'https://www.uniqlo.com/tw/zh_TW/c/all_men-tops.html'
drive = webdriver.Safari()

drive.get(url_nike)
htmlfile = drive.page_source

soup = BeautifulSoup(htmlfile,'html.parser')
#data-landscape-url
imgs = soup.find_all('img')

print(imgs)
i=1
for img in imgs:
    path = img['data-landscape-url']
    # name =img['alt']
    source = requests.get(path)
    img_source = source.content
    os.makedirs('images',exist_ok=True)

    with open(f'images/{i}.jpg','wb') as f:
        f.write(img_source)
    i +=1

    #git push test by terminal