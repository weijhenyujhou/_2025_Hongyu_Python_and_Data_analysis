import requests
# import ssl

url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
# url = 'https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key=9b651a1b-0732-418e-b4e9-e784417cadef&limit=1000&sort=ImportDate%20desc&format=JSON'
# ssl._create_default_https_context = ssl._create_unverified_context

results = requests.get(url,verify=False)

results = results.json()

# for result in results['records']:
#     print(f'{result['sitename']}:AQI {result['aqi']}')

for result in results:
    print(f'{result['sna']}:可租借車輛{result['available_rent_bikes']}')