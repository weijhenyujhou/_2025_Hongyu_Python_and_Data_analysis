import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

list_x = [15,26,38,15,22,30]
list_y = [1,3,5,7,9,11]

plt.plot(list_x,list_y,marker="s",color='#00bfff',linestyle=':', linewidth=2,markersize=10)
plt.title('test') #表格主旨
plt.xlabel("degree") #x軸標籤
plt.ylabel("day") #y軸的標籤

plt.show()