class Shopping:
    def __init__(self):
        self.cart = []
    def add_to_cart(self, item):
        self.cart.append(item)

customer1 = Shopping()
customer1.add_to_cart('t-shirt')
print(customer1.cart)

customer2 =Shopping()
customer2.add_to_cart('shoes')
print(customer2.cart)