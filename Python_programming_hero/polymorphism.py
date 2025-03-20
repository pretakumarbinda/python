class Car:
    car_name = 'Whelljack'
    def move(self):
        print(self.car_name, 'car is moving')
class Truck:
    truck_name = 'Optimus prime'
    def move(self):
        print(self.truck_name, 'Truck is moving')
class Bike:
    bike_name = 'Elita-one'
    def move(self):
        print(self.bike_name, 'bike is moving')
        
vehicles = [Car(), Truck(), Bike()]
for i in vehicles:
    i.move()