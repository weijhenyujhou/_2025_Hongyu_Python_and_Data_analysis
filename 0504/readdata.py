from time import process_time_ns

import pandas as pd

EV_data =pd.read_csv('chargepods.csv')

EV_data.columns = EV_data.columns.str.strip()
# Credit_data = pd.read_csv('CreditCard.csv')
# region_map = {
#     '63000000': '臺北市', '64000000': '高雄市', '65000000': '新北市', '66000000': '臺中市',
#     '67000000': '臺南市', '68000000': '桃園市', '10002000': '宜蘭縣', '10004000': '新竹縣',
#     '10005000': '苗栗縣', '10007000': '彰化縣', '10008000': '南投縣', '10009000': '雲林縣',
#     '10010000': '嘉義縣', '10020000': '嘉義市', '10013000': '屏東縣', '10014000': '臺東縣',
#     '10015000': '花蓮縣', '10016000': '澎湖縣', '10017000': '基隆市', '10018000': '新竹市',
#     '09020000': '金門縣', '09007000': '連江縣'
# }
#
# # 性別代碼對照表
# gender_map = {
#     1: 'M',
#     2: 'F'
# }
# Credit_data['region_name'] = Credit_data[' region_code'].map(region_map)
# Credit_data['gender'] = Credit_data['gender_code'].map(gender_map)
#
# print(Credit_data)
#
# condition = EV_data["國道別"].str.contains("1號")
# #print(EV_data[condition])
# #篩出TPC充電規格
# condition_TPCType = EV_data['充電設備規格'].str.contains("TPC")
#
# print(EV_data[condition_TPCType])
#
# resutlEV= condition_TPCType.drop('車位數量', axis=1)
#
# print(resutlEV)
#
# resutlEV.to_csv("TPC_chargePod.xlsx")
#


condition_TPCType = EV_data['充電設備規格'].str.contains("TPC", na=False)

tpc_df = EV_data[condition_TPCType]
resultEV = tpc_df.drop('車位數量', axis=1)

print(resultEV)
resultEV.to_csv("TPC_chargePod.csv", index=False)
