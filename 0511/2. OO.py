# 汽車類別
class Car:
    #設定汽車屬性的def
    def __init__(self,color,brand,door):
        # self.color = 'red'
        # self.brand = 'Tesla'
        # self.door = 4
        self.color = color
        self.brand = brand
        self.door = door
    #設定汽車可以做的動作
    def run(self):
        print('run')

#如果沒有預設值 在建立類別時再填入要建立物件的屬性
c1 = Car('red','Tesla','4')

# print(c1)
print(c1.__dict__) #用字典格式去強迫 顯示類別內有什麼預設值

c2 = Car('white','Toyata',5)

# c2.color ='white'
# c2.brand ='Toyata'
# c2.door = 5
print(c2.__dict__)