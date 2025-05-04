import pandas as pd
import matplotlib.pyplot as plt

plt.rc('font',family='LIHEI PRO')
travel_data = pd.read_csv('Travel_Data.csv')
#第二列開始才是資料
data = travel_data.iloc[1]

#年份跟歐洲地區還有小計欄位都丟掉
Pie_data = data.drop(["年別","歐洲地區","小計"])
print(Pie_data)

# plt.pie(Pie_data.values,
#         labels =Pie_data.index,
#         autopct='%.2f%%',
#
#
#
# )
# plt.show()
plt.pie(Pie_data.values,
        labels=Pie_data.index,
        autopct='%1.1f%%',
        explode=(0,0.1,0,0,0,0,1,1),
        textprops={'size':10, 'weight':'bold'},
        #labeldistance = 1.1, #label 位置
        )

plt.title("各歐洲國家旅遊人數比例")

plt.show()

