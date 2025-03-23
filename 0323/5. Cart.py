menu = {
    'apple':10,
    'banana': 100,
    'kiwi': 60
}

print('-------menu start-------')
for k,v in menu.items():
    print(f'{k:8}:{v:5}')
print('------menu end---------')

while True:
    selected = input('請輸入品項(enter "q"完成輸入)').lower()
    if selected == 'q':
        break
