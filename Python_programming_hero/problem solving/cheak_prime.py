# moulik naki moulik noy?
num = int(input('enter a number: '))
def is_prime(number):
    for i in range(2,number):
        if(number % i == 0):
            return False
    return True
cheak_prime = is_prime(num)
if cheak_prime:
    print('Your num is a prime')
else:
    print("Your num is not a prime.")