from cProfile import label

import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

list_x = [15,26,38,15,22,30]
list_y = [1,3,5,7,9,11]

plt.plot(list_x,list_y,marker="s",color='#00bfff',linestyle=':', linewidth=2,markersize=2,label ='May')
plt.rc('font',family='LIHEI PRO')
plt.title('test') #表格主旨
plt.xlabel("day") #x軸標籤
plt.ylabel("degree") #y軸的標籤
plt.xlim(1,100) # x軸 上下限
#plt.xticks([1,2,3,4,5,6,7,8,9,10])
plt.xticks([15,26,38,15,22,30]) #x軸 刻度設定
plt.yticks([1,3,5,7,9,11])
plt.legend() #標記線
plt.show()