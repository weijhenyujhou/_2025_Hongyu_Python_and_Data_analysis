import pandas as pd
import matplotlib.pyplot as plt

plt.rc('font',family='LIHEI PRO')

Credit_data = pd.read_csv('CreditCard.csv')

#print(Credit_data.columns.tolist())
# 區域對照表
region_map = {
    '63000000': '臺北市', '64000000': '高雄市', '65000000': '新北市', '66000000': '臺中市',
    '67000000': '臺南市', '68000000': '桃園市', '10002000': '宜蘭縣', '10004000': '新竹縣',
    '10005000': '苗栗縣', '10007000': '彰化縣', '10008000': '南投縣', '10009000': '雲林縣',
    '10010000': '嘉義縣', '10020000': '嘉義市', '10013000': '屏東縣', '10014000': '臺東縣',
    '10015000': '花蓮縣', '10016000': '澎湖縣', '10017000': '基隆市', '10018000': '新竹市',
    '09020000': '金門縣', '09007000': '連江縣'
}

# 性別代碼對照
gender_map = {
    1: 'M',
    2: 'F'
}

# 轉換代碼為文字
Credit_data['region_name'] = Credit_data['地區'].astype(str).map(region_map)
Credit_data['gender'] = Credit_data['性別'].map(gender_map)

New_data = Credit_data.drop(['地區','性別'], axis=1)
#result.to_csv("CreditCard.xlsx", index=False)

print(New_data.shape)

# 產生一個圖表 桃園市 男女生刷卡在食的消費比率 2024年

condition = (New_data['region_name']=='桃園市') & (New_data['gender']=='M') & (New_data['年月'] >= 202309)
filtered = New_data[condition]

gender_counts = filtered.groupby('信用卡產業別')['信用卡交易金額[新臺幣]'].sum()
print(gender_counts)
plt.pie(

    gender_counts,labels=gender_counts.index, autopct='%1.1F%%'
)
plt.title('202309-202409 桃園市男性刷卡產業別百分比') #表格主旨
plt.show()