#python 顯示變數的方式
# %
'''
# % + s 表示顯示時後面要插入的數值型態
%s=str
%d=int(10進位Decimal）
%x=16進位
%o=8進位
%f=float (Python最初顯示方式）
'''


a = 'Hello %s' # % + s 表示顯示時後面要插入的數值型態 s=str d=int(10進位Decimal） f=float (Python最初顯示方式）
b = 'Hello %d'
c = 'Hello %f'
d = 'Hello %x'

print(a % 'John')
print(b % 123)
print(c % 123.4)
print(d % 17)


e = 'Hello %10s' # % + s 表示顯示時後面要插入的數值型態 s=str d=int(10進位Decimal） f=float (Python最初顯示方式）
f = 'Hello %d'
g = 'Hello %.3f'
h = 'Hello %x'

print(e % 'John')
#print(b % 123)
print(g % 123.456789)
#print(d % 17)

#字串插補法
# f '顯示文字'+{變數}
my_name = 999
print(f"Hello {my_name:*^10}")


#Practic

msg = 'Hello %s ! 今日天氣溫度 %.1f'

print(msg %('John',23))

