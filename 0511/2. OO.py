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
        print(f'你的車子品牌為：{self.brand},顏色為：{self.color}')

#如果沒有預設值 在建立類別時再填入要建立物件的屬性
c1 = Car('red','Tesla','4')
c1.run()
# print(c1)
#print(c1.__dict__) #用字典格式去強迫 顯示類別內有什麼預設值

c2 = Car('white','Toyata',5)
#print(c2.__dict__)
c2.run()