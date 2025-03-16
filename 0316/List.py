'''
List 串列
'''
from time import process_time_ns

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






