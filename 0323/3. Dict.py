# Dictionary
from time import process_time_ns

d1 = {
    'key':'value',
    '屬性':'值'
}

user =[
    {
        'name':'John',
        'email':'john@gmail.com',
        'gender':'male',
        'Skill':['Python','C#','Sql']
    },
    {
        'name':'Mary',
        'email':'mary@gmail.com',
        'gender':'female',
        'Skill':['Photoshop','python','Java']
    }
]
# print(user[0]['Skill'][0])

user1 = {
        'name':'John',
        'email':'john@gmail.com',
        'gender':'male',
        'Skill':['Python','C#','Sql']
}
# #取出dict內的資料
# print(user1.get('Skill'))
# print(user1['Skill'])
# #修改dict內資料
# print('修改dict內資料')
# user1['Skill'] = 'Photoshop'
# user1['name'] = 'Max'
# #新增屬性
# user1.setdefault('age',23)
# print(user1)

#刪除屬性
# user1.pop('gender')
# del user1['age']
# print(user1)

#清除所有資料
# print(user1.keys())
# print(user1.values())
# print(user1.items())

#使用巢狀迴圈列出dict內多比資料
for user in user:
    for key,value in user.items():
        print(f'{key}:{value}')