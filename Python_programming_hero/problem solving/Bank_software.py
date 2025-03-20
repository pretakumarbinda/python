class Bank:
    def __init__(self):
        self.balance = 1000
        self.minimum = 100
    def get_balance(self):
        return self.balance
    def withdraw(self, amount):
        if amount < self.minimum:
            print('No money for you')
        elif amount > self.balance:
            print('You are broke! No money!')
        else:
            self.balance -= amount
            

#now use the class
my_bank = Bank()
my_bank.withdraw(1100)
balance = my_bank.get_balance()
print(balance)
my_bank.withdraw(50)
balance = my_bank.get_balance()
print(balance)

