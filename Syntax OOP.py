#Thêm dòng hehehehhehehehhehehehhe

class Car():
    def __init__(self, color, engine):
        self.num = 4
        self.__engine = engine #private
        self.color = color

    def run(self):
        print('Beep')

    def get_info_engine(self):
        print(self.__engine) #Phải có hàm can thiệp từ bên trong
    
    #Hàm cũng có thể private và cũng có thể can thiệp từ bên trong

#Tính kế thừa
class Mercedes(Car):
    def __init__(self, color, engine, have_AI):
        super().__init__(color, engine) #Kế thừa color, engine từ Car
        self.have_AI = have_AI #Tạo thêm thuộc tính

    def run(self):
        print('Pro pro pro') #Đè phương thức

car1 = Car('red', 'v12')
car1.run()
print(car1.num)
car1.get_info_engine()

mer = Mercedes('Trắng', 'v8', True)
print(mer.num)

mer.run()

