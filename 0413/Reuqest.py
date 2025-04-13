# 使用request模組
import requests #request 為第三方軟體需要在終端機先安裝 pip install requests
# # request method: 資料交換：get, post, 刪除：delete, 更新：put, patch
# url = 'https://www.ptt.cc/bbs/gossiping/index.html'
#
# data = requests.get(url)
# data = data.text
# print(data)

from Save_file import save_file
def request_get(url,pages):
    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    }
    data = requests.get(url, headers=header, verify=False)
    datas = data.json()
    for i in range(pages):
        url = (
            'https://www.kkday.com/zh-tw/category/ajax_product_list?keyword=&currency=TWD&sort=prec&start=0&count=10&destination=&availstartdate=&availenddate=&prodcat=CATEGORY_020%2CCATEGORY_023%2CCATEGORY_022%2CCATEGORY_025%2CCATEGORY_030%2CCATEGORY_028%2CCATEGORY_021%2CCATEGORY_026%2CCATEGORY_029%2CCATEGORY_024%2CCATEGORY_027&ave_score_from=&locations=&time=&glang=&row=10&fprice=*&eprice=*&immediately_use=0&sale_status=0&departure=&arrival=&travel_type=&rewrite=1&csrf_token_name=6febb77a6695c7dba8e9892287bfed1d&page=')
        url = url + str(i + 1)
        with open('request_gettxt.txt', 'a', encoding='utf-8') as file:
            file.write(f'---------第{i + 1}頁開始---------\n')
            for data in datas['data']:
                file.write(f'{data['name']}--{data['introduction']}\t:NT${data['price']}\n')
            file.write(f'---------第{i + 1}頁結束-----------\n')