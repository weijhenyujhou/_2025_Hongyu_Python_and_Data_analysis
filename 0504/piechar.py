import matplotlib.pyplot as plt

plt.rc('font',family='LIHEI PRO')

datas = [20,66,88]
labels = ['國中','高中','大專院校']
#
plt.pie(
    datas,
    labels=labels
)

plt.legend()
plt.show()