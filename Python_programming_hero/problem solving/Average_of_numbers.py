# #take input from user how many number he wants to make average and then input the number. solve with for loop

length = int(input("how many number you want to enter? "))
list = []
for i in range(0, length):
    element = int(input("Enter element: "))
    list.append(element)

total = sum(list)
avg = total/length
print("Average of elements you entered: ", round(avg,2))

#another solution:

length = int(input("How many numbers you wants to enter? "))
total = 0
for i in range(0, length):
    element = int(input("Enter your number: "))
    total = total + element
average = total/length
print("Average of the elements you entered: ", round(average, 2))

