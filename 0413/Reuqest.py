# 使用request模組
import requests #request 為第三方軟體需要在終端機先安裝 pip install requests
# # request method: 資料交換：get, post, 刪除：delete, 更新：put, patch
# url = 'https://www.ptt.cc/bbs/gossiping/index.html'
#
# data = requests.get(url)
# data = data.text
# print(data)

from Save_file import save_file

def request_get(url):
    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    }

    # url = 'https://www.kkday.com/zh-tw/theme/ajax_get_vtag_prod_info?prodcat=CATEGORY_079&sort=prec&page=2&apiKey=food'

    data = requests.get(url,headers= header,verify=False)
    datas = data.json()
    save_file(datas)