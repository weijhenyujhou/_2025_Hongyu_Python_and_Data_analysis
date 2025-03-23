

menu = {
    'apple':10,
    'banana': 100,
    'kiwi': 60
}
cart = {}
print('-------menu start-------')
for k,v in menu.items():
    print(f'{k:8}:{v:5}')
print('------menu end---------')

while True:
    selected = input('請輸入品項(enter "q"完成輸入)').lower()
    if selected == 'q':
        break
    elif selected not in menu:
        print('輸入項目有誤請從新選擇')
        continue
    quantity = input(f'輸入購買{selected}數量')
    if not quantity.isdigit() or int(quantity)<=0:
        print('輸入數量有誤')
        continue
    quantity = int(quantity)

    if selected in cart:
        quantity +=quantity
    else:
        cart[selected] = quantity

    print(f'已將{selected}已加入購物車x數量{quantity}')
print('/n cart 你的購物車內容:')
total_price =0
for item,qty in cart.items():
    price = menu[item]*qty
    total_price +=price
    print(f'{item:8} x {qty} = ${price}')

print('----------------------------')
print(f'🛒 總金額：${total_price}')
print('🎉 感謝購買！')
