
import  requests
def getdata(url):
    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    }

    url = 'https://www.kkday.com/zh-tw/theme/ajax_get_vtag_prod_info?prodcat=CATEGORY_079&sort=prec&page=2&apiKey=food'

    data = requests.get(url,headers= header)
    data = data.json()

    # import bs4
    #
    # root = bs4.BeautifulSoup(data, 'html.parser')
    # items = root.find_all('div', class_='product-detail')

    print(data)

url = 'https://www.kkday.com/zh-tw/theme/ajax_get_vtag_prod_info?prodcat=CATEGORY_079&sort=prec&page=2&apiKey=food'

count = 0
while count < 4:
    print(f"以下為第{count+1}頁得內容")
    pageURL = 'https://www.kkday.com' + getdata(url)
    count += 1
print("--------網頁爬蟲結束--------")