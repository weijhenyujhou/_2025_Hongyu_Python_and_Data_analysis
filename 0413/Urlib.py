import urllib.request as req
import ssl
import json
ssl._create_default_https_context = ssl._create_unverified_context
def Urllib_get(url,pages):
    for i in range(pages):

        #url =f'https://www.kkday.com/zh-tw/category/ajax_product_list?keyword=&currency=TWD&sort=prec&page={str(i+1)}&start=0&count=10&destination=&availstartdate=&availenddate=&prodcat=CATEGORY_020%2CCATEGORY_023%2CCATEGORY_022%2CCATEGORY_025%2CCATEGORY_030%2CCATEGORY_028%2CCATEGORY_021%2CCATEGORY_026%2CCATEGORY_029%2CCATEGORY_024%2CCATEGORY_027&ave_score_from=&locations=&time=&glang=&row=10&fprice=*&eprice=*&immediately_use=0&sale_status=0&departure=&arrival=&travel_type=&rewrite=1&csrf_token_name=14faccbd1ae923f392b3d9dac1572866'
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
        }

        request = req.Request(url, headers=header)

        with req.urlopen(request) as response:
            result = response.read().decode('utf-8')

        data_json = json.loads(result)

        with open('Urllib_get.txt','a',encoding='utf-8')as file:
            file.write(f'---------第{i+1}頁開始---------\n')
            for data in data_json['data']:
                # print(d['name'])
                file.write(f"{data['name']}:{data['price']}\n")
            file.write(f'---------第{i+1}頁結束-----------\n')