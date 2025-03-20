class Car:
    @staticmethod
    def start():
        print('car started....')

    @staticmethod
    def stop():
        print('car stopped....')

class Toyota_car(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(Toyota_car):
    def __init__(self, type):
        self.type = type
        
car1 = Fortuner('diesel')
car1.start()