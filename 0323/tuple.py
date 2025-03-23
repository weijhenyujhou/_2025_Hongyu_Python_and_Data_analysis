from time import process_time_ns

t1 = tuple()
# Tuple 不能更動資料

t2 = (1,2,3,4,5)
#t2[0] = 'A' #Tuple內的值不能變動

t3 = 123,True,'Apple',123.45

print(t3)

t4 = t2 + t3

print(t4)
# 當加入資料為字串後面需增加一個,
t4 +=('apple',)

print(t4)
