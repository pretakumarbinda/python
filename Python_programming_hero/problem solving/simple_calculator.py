def add(num1, num2):
    return num1 + num2
def substract(num1, num2):
    return num1 - num2
def divide(num1, num2):
    return num1 /num2
def multiply(num1, num2):
    return num1 * num2

num1 = int(input('enter first number: '))
operation = input('enter what you want to do(+, -, *, /)')
num2 = int(input('enter second number: '))
result = 0
if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = substract(num1, num2)
elif operation == '*':
    result = multiply(num1 ,num2)
elif operation == '/':
    result = divide (num1 ,num2)
print(num1, operation, num2, '=', result)