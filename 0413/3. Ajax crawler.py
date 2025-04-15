
import requests
import urllib.request as req
import ssl
import json # 需要額外導入jason套件

# header = {
#         'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
#     }
#     data = requests.get(url, headers=header, verify=False)
#     datas = data.json()
#
#     # #第一步：抓取的資料存入json檔 開啟>寫入
#     # json_string = json.dumps(datas, ensure_ascii=False, indent=2)
#     # with open('kkday.json','w',encoding='utf-8') as file:
#     #     file.write(json_string)
#     #第二步：抓取需要的資料欄位名稱 旅遊名稱, 旅遊價格
#     # for data in datas['data']:
#     #     print(f'=={data['name']}:NT${data['price']}')
#     #第三步：將爬出的資料放入檔案內存檔 w:覆蓋寫入 a: 會寫入新資料
#     # with open('kkday_txt.txt', 'a', encoding='utf-8') as file:
#     #     for data in datas['data']:
#     #         file.write(f'{data['name']}--{data['introduction']}\t:NT${data['price']}\n')
#     save_file(datas)
#
#
# #url = 'https://www.kkday.com/zh-tw/theme/ajax_get_vtag_prod_info?prodcat=CATEGORY_079&sort=prec&page=3&apiKey=food'
# #request_get(url)
#
#
# #url = 'https://www.kkday.com/zh-tw/theme/ajax_get_vtag_prod_info?prodcat=CATEGORY_079&sort=prec&page=2&apiKey=food'
#
#
# def save_file(datas):
#     with open('kkday_txt.txt', 'a', encoding='utf-8') as file:
#         for data in datas['data']:
#             file.write(f'{data['name']}--{data['introduction']}\t:NT${data['price']}\n')
#
#
#
# #urllib 套件
#
# import urllib.request as req
# import ssl
# import json # 需要額外導入jason套件
# ssl._create_default_https_context = ssl._create_unverified_context
#
# #url ='https://www.kkday.com/zh-tw/category/ajax_product_list?keyword=&currency=TWD&sort=prec&page=1&start=0&count=10&destination=&availstartdate=&availenddate=&prodcat=CATEGORY_020%2CCATEGORY_023%2CCATEGORY_022%2CCATEGORY_025%2CCATEGORY_030%2CCATEGORY_028%2CCATEGORY_021%2CCATEGORY_026%2CCATEGORY_029%2CCATEGORY_024%2CCATEGORY_027&ave_score_from=&locations=&time=&glang=&row=10&fprice=*&eprice=*&immediately_use=0&sale_status=0&departure=&arrival=&travel_type=&rewrite=1&csrf_token_name=14faccbd1ae923f392b3d9dac1572866'
# # def llib_get(url):
# #     header = {
# #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
# #     }
# #
# #     request = req.Request(url, headers=header)
# #
# #     with req.urlopen(request) as response:
# #         result = response.read().decode('utf-8')
# #
# #     datas = json.loads(result)
# #     save_file(datas)

from Urlib import Urllib_get
from Reuqest import request_get

# for i in range(2):
#     url =('https://www.kkday.com/zh-tw/category/ajax_product_list?keyword=&currency=TWD&sort=prec&start=0&count=10&destination=&availstartdate=&availenddate=&prodcat=CATEGORY_020%2CCATEGORY_023%2CCATEGORY_022%2CCATEGORY_025%2CCATEGORY_030%2CCATEGORY_028%2CCATEGORY_021%2CCATEGORY_026%2CCATEGORY_029%2CCATEGORY_024%2CCATEGORY_027&ave_score_from=&locations=&time=&glang=&row=10&fprice=*&eprice=*&immediately_use=0&sale_status=0&departure=&arrival=&travel_type=&rewrite=1&csrf_token_name=6febb77a6695c7dba8e9892287bfed1d&page=')
#     url = url + str(i+1)

url = ('https://www.kkday.com/zh-tw/category/ajax_product_list?keyword=&currency=TWD&sort=prec&start=0&count=10&destination=&availstartdate=&availenddate=&prodcat=CATEGORY_020%2CCATEGORY_023%2CCATEGORY_022%2CCATEGORY_025%2CCATEGORY_030%2CCATEGORY_028%2CCATEGORY_021%2CCATEGORY_026%2CCATEGORY_029%2CCATEGORY_024%2CCATEGORY_027&ave_score_from=&locations=&time=&glang=&row=10&fprice=*&eprice=*&immediately_use=0&sale_status=0&departure=&arrival=&travel_type=&rewrite=1&csrf_token_name=6febb77a6695c7dba8e9892287bfed1d&page=')
#Urllib_get(url,2)
request_get(url,2)

