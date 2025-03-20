# num1 = int(input(" enter first number: "))
# num2 = int(input(" enter second number: "))
# num3 = int(input(" enter third number: "))
# if (num1>num2) and (num1>num3):
#     largest = num1
# elif (num2>num1) and (num2>num3): 
#     largest = num2
# else:
#     largest = num3
# print("largest number is: ", largest)

#another solve using max function

# num1 = int(input(" enter first number: "))
# num2 = int(input(" enter second number: "))
# num3 = int(input(" enter third number: "))
# largest = max(num1, num2, num3)
# print("largest number is: ", largest)


num1 = int(input(" enter first number: "))
num2 = int(input(" enter second number: "))
num3 = int(input(" enter third number: "))
if (num1>num2) and (num1>num3):
    largest = num1
elif (num2>num3): 
    largest = num2
else:
    largest = num3
print("largest number is: ", largest)