# #phone class
# class Phone:
#     video_call = True
#     def __init__(self, brand, price, network):
#         self.brand = brand
#         self.price = price
#         self.network = network
#     def recharge(self):
#         print('eating electron')
        
# my_phone = Phone('Apple', 800, 'TMobile')
# my_phone.recharge()
# print(my_phone.brand)

# #watch class
# class Watch:
#     def __init__(self, brand, price, has_gps):
#         self.brand = brand
#         self.price = price
#         self.has_gps = has_gps
#     def recharge(self):
#         print('Eating electricity')
# my_watch = Watch('Fitbit', 200, False)
# my_watch.recharge()

class SmartDevice:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def recharge(self):
        print('eating electricity')
        
class Watch(SmartDevice):
    def __init__(self, brand, price, has_gps):
        SmartDevice.__init__(self, brand, price)
        self.steps_count = 0
        self.has_gps = has_gps

my_watch = Watch('fitbit', 200, False)
print(my_watch.brand)