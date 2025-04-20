import requests

url='https://odws.hccg.gov.tw/001/Upload/25/opendataback/9059/59/5776ed30-fa3c-48f4-9876-d8fb28df0501.json'

result = requests.get(url,verify=False)

print(result)