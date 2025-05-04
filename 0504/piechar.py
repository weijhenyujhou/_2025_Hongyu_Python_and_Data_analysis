import matplotlib.pyplot as plt

plt.rc('font',family='LIHEI PRO')

datas = [20,66,88]
labels = ['國中','高中','大專院校']
#
plt.pie(
    datas,
    labels=labels,
    #colors=['blue','darkblue','lightblue'] #顏色
    radius = .8,  #圖形比例大小
    labeldistance = 1.1, #label 位置
    textprops={'size':10,'weight':'bold'} ,#字型大小跟類型
    autopct='%.2f%%' #自動計算百分比 顯示至小數點第二位
)

plt.legend()
plt.show()
#計算百分比

data = [20,30,50]
total = sum(data)

data_2 = [str(100* d / sum(data)) + '%' for d in data ]
print(data_2)
