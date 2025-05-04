import pandas as pd


data = pd.Series([10,20,22,7,68,55]) #一維資料為Series
data2 = pd.DataFrame( #二維資料為DataFrame
    [
        [1,2,3],
        [4,5,6]
    ]
    )

data3 = pd.DataFrame(
    {
        'name':['Zac','Andy','Tim'],
        'age':[30,32,26]
    }
)

# print(data3.size)
# #顯示 DataFrame 中所有元素的總數（列數 × 欄數）
#
# print(data3.shape)
# #顯示 DataFrame 的維度（列數, 欄數）
#
# print(data3.columns)
# #顯示欄位名稱（columns）
#
# print(data3.index)
# #顯示索引（index），也就是每列的標籤
#
# print(data3['name'])
# #取出 'name' 欄位的所有資料（Series）
#
# print(data3.iloc[0])
# #使用整數位置取出第 0 列的所有欄位資料
#
# print(data3.loc[2])
# #使用索引標籤取出 index 為 1 的那一列資料（若 index 是數字 1 的話）

data4 = pd.DataFrame(
    [
        {'name':'Zac','age':30,'gender':'M'},
        {'name':'Andy','age':32,'gender':'M'},
        {'name':'Tim','age':26,'gender':'M'},
        {'name':'Amy','age':22,'gender':'F'},
        {'name':'Laura','age':26,'gender':'F'}
    ]

)
#data4.index = ['a', 'b', 'c'] #自定義 index
#print(data4)
# print(data4)
# print(data4.iloc[0]) #
# print(data4.loc[2])

#數學相關篩選

condition = data4['age'] >=30

print(data4[condition])

condition1 = data4['gender'].str.contains('M')

print(data4[condition1])