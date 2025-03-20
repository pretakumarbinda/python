#take a number as input. then get the sum of the numbers. if the number is n. then get 0^2 + 1^2 + .......+ n^2

number = int(input("Enter a number: "))
sum = 0
for i in range(number + 1): #passing the value of i = 0, 1, 2, 3, .........., number
    square = (i**2)
    sum = sum + square
print("sum of the squared numbers: ",sum)


#another process

n = int(input("Enter the number: "))
sum = n*(n+1)*(2*n+1)/6
print(sum)


#if we want to solve it through function:


num = int(input('enter a number: '))
def sum_of_square(n):
    sum = n*(n+1)*(2*n + 1)/6
    return sum
sum1 = sum_of_square(num)
print('Your sum of square is: ', sum1)