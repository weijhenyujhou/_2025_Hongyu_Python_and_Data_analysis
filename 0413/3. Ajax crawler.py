
import  requests
def request_get(url):
    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    }

    # url = 'https://www.kkday.com/zh-tw/theme/ajax_get_vtag_prod_info?prodcat=CATEGORY_079&sort=prec&page=2&apiKey=food'

    data = requests.get(url,headers= header)
    data = data.json()

    # import bs4
    #
    # root = bs4.BeautifulSoup(data, 'html.parser')
    # items = root.find_all('div', class_='product-detail')

    print(data)


#url = 'https://www.kkday.com/zh-tw/theme/ajax_get_vtag_prod_info?prodcat=CATEGORY_079&sort=prec&page=3&apiKey=food'
#request_get(url)


#url = 'https://www.kkday.com/zh-tw/theme/ajax_get_vtag_prod_info?prodcat=CATEGORY_079&sort=prec&page=2&apiKey=food'



#urllib 套件

import urllib.request as req
import ssl
import json # 需要額外導入jason套件
ssl._create_default_https_context = ssl._create_unverified_context

#url ='https://www.kkday.com/zh-tw/category/ajax_product_list?keyword=&currency=TWD&sort=prec&page=1&start=0&count=10&destination=&availstartdate=&availenddate=&prodcat=CATEGORY_020%2CCATEGORY_023%2CCATEGORY_022%2CCATEGORY_025%2CCATEGORY_030%2CCATEGORY_028%2CCATEGORY_021%2CCATEGORY_026%2CCATEGORY_029%2CCATEGORY_024%2CCATEGORY_027&ave_score_from=&locations=&time=&glang=&row=10&fprice=*&eprice=*&immediately_use=0&sale_status=0&departure=&arrival=&travel_type=&rewrite=1&csrf_token_name=14faccbd1ae923f392b3d9dac1572866'
def llib_get(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    }

    request = req.Request(url, headers=header)

    with req.urlopen(request) as response:
        result = response.read().decode('utf-8')

    datas = json.loads(result)
    print(datas['data'])
    for data in datas['data']:
        print(f'{data['name']}:{data['price']}')

    with open('kkday.json','w',encoding='utf8') as file:
        file.write(datas)



url ='https://www.kkday.com/zh-tw/category/ajax_product_list?keyword=&currency=TWD&sort=prec&page=1&start=0&count=10&destination=&availstartdate=&availenddate=&prodcat=CATEGORY_020%2CCATEGORY_023%2CCATEGORY_022%2CCATEGORY_025%2CCATEGORY_030%2CCATEGORY_028%2CCATEGORY_021%2CCATEGORY_026%2CCATEGORY_029%2CCATEGORY_024%2CCATEGORY_027&ave_score_from=&locations=&time=&glang=&row=10&fprice=*&eprice=*&immediately_use=0&sale_status=0&departure=&arrival=&travel_type=&rewrite=1&csrf_token_name=14faccbd1ae923f392b3d9dac1572866'

#使用llib crawler
llib_get(url)
#使用request crawler
#request_get(url)