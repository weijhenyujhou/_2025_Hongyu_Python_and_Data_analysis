'''宣告方式
def functionName():
    函式內容

回傳值類型
return 將計算後的值回傳函式
pass
'''
def foo():
    x = 100
    y = 1.2
    return x * y
print(foo())

# return 需要將結果回傳函式時使用return,如果只是要單傳顯示不要記錄功能的數值可以只用print
def area(w,h):
    #print(w * h)
    return w * h
#result = area(100,2)
print(area(100,2))
print(area(100,4))
print(area(200,2))

# Default Argument

def jp_to_tw(Doller,rate):
    return Doller * rate
print(f'不按照韓式變數宣告順序給變數(Rate,Doller)：{jp_to_tw(rate=0.23,Doller=10000)}')
print(f'按照函式變數宣告順序給變數(Doller, Rate)：{jp_to_tw(10000,0.23)}')

#倒數計時器功能
s = int(input('請輸入秒數'))
import time
def count(end,start=0,):#有預設值時該變數一率放最後面
    for x in range(end, start,-1): #range(5,1,-1) 由大到小顯示數值
        print(x)
        time.sleep(1)
    print('Finish')

count(s)