#
import math
from contextlib import nullcontext
from time import process_time_ns

x = 3.6
y = -34
# print(round(x))
# print(abs(x))
print(max(2,3,1))

print(math.floor(x)) # 無條件捨去
print(math.ceil(x)) # 無條件進位


print(abs(x)) #絕對值
print(round(x)) # 四捨五入
print(pow(x,3)) #x 3次方
print(math.cos(45))

"""
運算子
"""

print(math.pi)

#運算子
a = 10
b = 6
# 數學
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
# 比較 ==, !=. >, >=, <, <=
print( a == b)
print( a != b)
print(a > b)
print(a >= 0)
print(b < 0)
print( b <= 0)

# not 以下Python特殊邏輯
print('=====邏輯運算======')
v = 0
print(not v)
v = None
print(not v)
v = [ ]
print(not v)
v = ""
print(not v)

# 指定
print('運算錢未指定A前',a)

a += b
print('運算後指定A後',a)


