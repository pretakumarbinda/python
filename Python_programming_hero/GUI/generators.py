import random

def Data():                         # Data function is defined as a generator
    for i in range(5):
        yield random.randint(1,10)
        

for num in Data():
    print(num)