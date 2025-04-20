import requests
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
title = ['UBike站點名稱', '可還車數量']
ws.append(title)


url_Ubilke='https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
#url_airAQI = 'https://data.moenv.gov.tw/api/v2/aqf_p_01?api_key=9e565f9a-84dd-4e79-9097-d403cae1ea75&limit=1000&sort=publishtime%20desc&format=JSON'
results = requests.get(url_Ubilke,verify=False)

results =results.json()

for result in results:
    item = result['sna'],result['available_return_bikes']
    ws.append(item)
wb.save('UBikeData.xlsx')
