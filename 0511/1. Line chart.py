import  matplotlib.pyplot as plt
import pandas as pd
from twstock.mock import stock_list

plt.rc('font',family='LIHEI PRO')
travel_data = pd.read_csv('Travel_Data.csv')

# x = ['A','B','C','D','E','F']
# h = [1,2,3,4,5,6]
#
# plt.bar(x,h)
#
# plt.show()

travel_data_x = travel_data.columns[2:-1]
print(travel_data_x)
h = [int(h) for h in travel_data.iloc[1][2:-1]]
print(h)

#color = ['red','blue','yellow','grey','purple','green','block']
#tick_label =['French','Germany','Italy','Neth','The UK','Span','Iceland','a']

plt.bar(
    travel_data_x,h,
    width=1.0,
    #tick_label=tick_label,

)
plt.show()