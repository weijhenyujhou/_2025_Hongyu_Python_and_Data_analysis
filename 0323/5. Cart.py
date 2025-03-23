from time import process_time_ns

menu = {
    'apple':10,
    'banana': 100,
    'kiwi': 60
}
cart = []
total = 0
print('-------menu start-------')
for k,v in menu.items():
    print(f'{k:8}:{v:5}')
print('------menu end---------')

while True:
    selected = input('請輸入品項(enter "q"完成輸入)').lower()
    if selected == 'q':
        break
    elif selected in menu:
        cart.append(selected)
        continue


print('\n🛒 你的購物車內容：')
for p in cart:
    print(f'- {p}')
    #print(menu.get(p)) #取出menu內產品的價錢
    total += menu.get(p)

print(f'🎉 感謝購買！總共購金額:{total}')
