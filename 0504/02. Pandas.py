import pandas as pd


data = pd.Series([10,20,22,7,68,55]) #一維資料為Series
data2 = pd.DataFrame( #二維資料為DataFrame
    [
        [1,2,3],
        [4,5,6]
    ]
    )

print(data)
print(data2)