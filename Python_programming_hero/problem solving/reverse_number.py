#reverse a number
def reverse_num(n):
    reverse = 0
    while(n>0):
        last_digit = n%10
        reverse = reverse * 10 + last_digit
        n = n//10
    return reverse
n = int(input('enter your number: '))
reverse = reverse_num(n)
print('reversed num: ', reverse)

