num1 = int(input(" enter first number: "))
num2 = int(input(" enter second number: "))
if(num2>num1):
    largest = num2
else:
    largest = num1
print("Largest number: ", largest)

#another process (by using max function):

num1 = int(input(" enter first number: "))
num2 = int(input(" enter second number: "))
largest = max(num1, num2)
print("the maximum number is: ", largest)

