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
from time import process_time_ns

a = 'Hello %s' # % + s 表示顯示時後面要插入的數值型態 s=str d=int(10進位Decimal） f=float (Python最初顯示方式）
b = 'Hello %d'
c = 'Hello %f'
d = 'Hello %x'

print(a % 'John')
print(b % 123)
print(c % 123.4)
print(d % 17)


e = '靠右對齊 Hello %+10s' # % + s 表示顯示時後面要插入的數值型態 s=str d=int(10進位Decimal） f=float (Python最初顯示方式）
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
msg = "1.百分比_顯示_Hello %s ! 今日天氣溫度 %.2f"


print(msg %('John',23))

# format()
msg_1='Hello {:*^10s} ! 今日溫度 {:.1f}'
msg_2=('11的8進位{:o}, 及6進位{:x}')
print(msg_1.format('John',23))
print(msg_2.format(11,11))

msg_3 = '2.format方式 Hello {name:=^10s} ! 今日天氣溫度 {deg:.2f}'
print(msg_3.format(name ='John',deg=23))


# f-string
name = 'John'
deg =23
email = "adfg@gmail.com"
print(f'3.f-string方式 Hello {name:=^10s} ! 今日天氣溫度 {deg:.2f}')

# \ 跳脫字元 用途
#a = 'Hello "John"'
#a = "Hello 'John'"

#\n 換行 \t tab 空格定位

print(f'Hello\t{name:=^10s}!\ne-mail:\t{email}')