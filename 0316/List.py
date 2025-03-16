"""
List 串列
"""



#宣告一個空間給l1
#l1 =[]
#l1 = list()

l1=['apple',123,0.98,True,True,'banana',123]
#print(l1[:2])

#取出list資料方式1 for迴圈
for data in l1:
    print(data)

# while
# index 方式取出值 不會清空list
print('=========')
index = 0
while index < len(l1):
    print(l1[index])
    index +=1
# pop方式取出值 但是會清空list
print('========')
while l1:
    print(l1.pop(0))
# print(l1) 列出l1 list
print('======分隔線======')
l1=['apple',123,0.98,True,True,'banana',123]
# len()
print(len(l1))
# count()
print(l1.count('banana'))
# index()
print(l1.index('apple'))

#append() 串列放入串列
l1.append(['python','mysql'])
print(l1)
#extend() 拆開放入串列
l1.extend(['python']) # 中括號內的會直接放入
l1.extend('python') # 無加括號的會將引號內的可迭代的資料型態拆開放入串列中
print(l1)

print('================')
l1=['apple',123,0.98,True,True,'banana',123]
#insert()
l1.insert(2,'python')#index(索引, 插入數值)
print(l1)
#remove()
l1.remove(123) # 刪除值為123的
print(l1)
#pop()
l1.pop(2) #刪除index為2的0.98
print(l1)
#sort()

#clear()
l1.clear() # 清空串列內所有值
print(l1)


