#this function is used to save to crawler data.
def save_file(datas):
    with open('kkday_txt.txt', 'a', encoding='utf-8') as file:
        for data in datas['data']:
            file.write(f'{data['name']}--{data['introduction']}\t:NT${data['price']}\n')