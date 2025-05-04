import pandas as pd

EV_data =pd.read_csv('chargepods.csv')

EV_data.columns = EV_data.columns.str.strip()

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

# #先設定要刪選條件
# condition_TPCType = EV_data['充電設備規格'].str.contains("TPC", na=False)
# # 將篩選條件建立另一個資料表
# tpc_df = EV_data[condition_TPCType]
# # 丟掉資料表內的欄位'車位數量'
# resultEV = tpc_df.drop('車位數量', axis=1)
# #最後印出後產出檔案
# print(resultEV)
# resultEV.to_csv("TPC_chargePod.xlsx", index=False)
