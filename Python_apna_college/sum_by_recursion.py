#write a recursive function to calculate the sum of first n natural numbers.
def func(n):
    if n == 0:
        return 0
    
    return func(n-1) + n
sum = func(5)
print(sum)