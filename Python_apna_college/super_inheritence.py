class Car:
    def __init__(self, type):
        self.type = type
    
    @staticmethod
    def start():
        print("car started...")
        
    @staticmethod
    def stop():
        print('Car stopped.....')
        
class Toyota_Car(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        
car1 = Toyota_Car('prius', 'electric')
print(car1.type)