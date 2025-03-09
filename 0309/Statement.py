# if else

# x =float(input('輸入數字'))
# if x > 0:
#     print('輸入是正數')
# elif x < 0:
#     print('輸入是負數')
# else:
#     print('輸入值為0')

# 使用者決定 台日幣匯入轉換

# m = input('模式確認：台幣轉日幣請輸入"1",日幣轉台幣請輸入“2”')
# exc = 0.219
# if  m =='1':
#     yendollers = float(input('請輸入日幣金額'))
#     trandollers = round(yendollers*exc,0)
#     print(f"日幣{yendollers}金額轉換成台幣金額為:{trandollers}")
#
# elif m == '2':
#     ntdollers = float(input('請輸入台幣金額'))
#     trandoller = round(ntdollers/exc,0)
#     print(f"台幣{ntdollers}金額轉換成日幣金額為:{trandoller}")
# else :
#     print('模式輸入錯誤請重新輸入')

n = float(input('請輸入數值'))
m = input('模式確認：Oz轉ml請輸入"1",ml轉Oz請輸入“2”')
exc = 29.57
if  m =='1':

    result = round(n*exc,2)
    print(f"輸入Oz:{m} 轉換成ml為:{result}")

elif m == '2':
    result = round(n/exc,2)
    print(f"輸入ml:{m} 轉換成Oz為:{result}")
else :
    print('模式輸入錯誤請重新輸入')