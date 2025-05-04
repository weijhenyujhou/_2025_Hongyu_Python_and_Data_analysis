

import matplotlib.pyplot as plt
import pandas as pd
plt.rc('font',family='Microsoft Jhenghei')
datas = pd.read_csv('outbound.csv')

print(datas)

total = datas.iloc[1]['亞洲地區']
subtotal = datas.iloc[-1]['小計']
other = int(total) - int(subtotal)



labels = list(datas.columns[2:-1])
labels.append('其他')

data = list(datas.iloc[1][2:-1])
data.append(other)

print(labels)

plt.pie(
    data,
    labels=labels,
    radius=1,
    labeldistance=1.1,
    textprops={'size':10, 'weight':'bold'},
    autopct='%.1f%%'
)
plt.legend()
plt.show()
