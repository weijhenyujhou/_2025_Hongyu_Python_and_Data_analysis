#變數
#命名規則
#1. 保留字不能使用
#2. 變數名稱開頭不能是數字

name='John' #string
age = 20  #int
weight = 78.8 # float
Female = False  #bool
print(name,age,weight,Female)

#型別轉換
'''
x = int(input('請輸入第一個數值'))
y = int(input('請輸入第二個數值'))
print(x+y)
'''

a = '100'
print(int(a))
print(float(a))
print(bool(a))

b = 3.6
print(int(b))
print(str(b))
print(bool(b))
print(bool(int(a)<int(b)))