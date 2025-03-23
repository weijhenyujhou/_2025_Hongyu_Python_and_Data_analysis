menu = [
    {
        'id':1,
        'name':'1.滷肉飯',
        'price':50

    },
    {
        'id':2,
        'name':'2.牛肉麵',
        'price':120
    },
    {
        'id':3,
        'name':'3.滷肉飯',
        'price':40
    }
]
cart=[]
total =0
print('------Menu--------')
for item in menu:
    print(item['name'],item['price'])
print('--------Menu-------')

while True:
    selected = input('請輸入編號(enter "q"完成輸入)').lower()
    if selected == 'q':
        break
    elif int(selected) > len(menu):
        print('請重新輸入編號')
        continue
    #print(menu[int(selected)-1])
    elif menu[int(selected)-1] in menu:
        cart.append(menu[int(selected)-1])
print(cart)

for item in cart:
    print(f'{item['name']}')
    total +=item['price']
print(f'總訂購金額:{total}')