#父類別
class Car:
    #設定汽車屬性的def
    def __init__(self,color,door):
        self.color = color
        self.door = door
    def run(self):
        print(f'你的汽車顏色：{self.color}')
#子類別
class Tesla(Car):
    def __init__(self, color, door):
        # 子類別呼叫父類別 super().方法名稱
        super().__init__(color, door)
        self.brand = 'Tesla'
        super().run()
class Toyata(Car):
    #子類別補上新的屬性
    def __init__(self,color, door):
        super().__init__(color,door)
        self.brand = 'Toyata'
        super().run()
c1 = Toyata('red',4)
print(c1.__dict__)
c2 = Tesla('white',5)
print(c2.__dict__)
