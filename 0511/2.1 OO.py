# n = float(input('請輸入轉換數值'))
# m = input('模式確認：Oz單位轉換成ml請輸入“1”,ml單位轉換成Oz請輸入“2”')
# exc = 29.57
# if  m == '1':
#
#     result = round(n*exc,2)
#     print(f"輸入Oz:{m} 轉換成ml為:{result}")
#
# elif m == '2':
#     result = round(n/exc,2)
#     print(f"輸入ml:{m} 轉換成Oz為:{result}")
# else :
#     print('模式輸入錯誤請重新輸入')

class Ozexchange:
    def __init__(self,x,s):
        self.x = float(x)
        self.s = s
    #寫一個方法判斷數入要轉換的模式
    def result(self):
        if self.s =='O':
            self.oztoml()
        else:
            self.mltooz()
    #兩個方法分別計算轉換值結果
    def oztoml (self):
        result = round(self.x * 29.75, 2)
        print(f"輸入Oz:{self.x} 轉換成ml為:{result}")

    def mltooz (self):
        result = round(self.x / 29.75, 2)
        print(f"輸入Oz:{self.x} 轉換成ml為:{result}")

x = float(input('請輸入轉換數值'))
s = input('模式確認：單位轉換(Ｏ/M)')

r = Ozexchange(x,s)
r.result()


