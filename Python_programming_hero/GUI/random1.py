import random
# print(random.randint(1, 6))

# print(random.random())

print(random.randrange(1,6,2))   #start, stop, step

numbers = [1,2,3,4,5]
print(random.choice(numbers))

random.shuffle(numbers)
print(numbers)
