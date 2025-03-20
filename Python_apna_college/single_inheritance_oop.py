class Car:
    @staticmethod
    def start():
        print('car started...')
    
    @staticmethod
    def stop():
        print('Car stopped')
    
class Toyota_Car(Car):
    def __init__(self, name):
        self.name = name
        
car1 = Toyota_Car('Fortuner')
car2 = Toyota_Car('prius')
print(car1.start())