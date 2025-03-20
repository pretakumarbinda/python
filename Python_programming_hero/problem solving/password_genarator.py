# import string
# import random

# def generate_password(size):
#     all_chars = string.ascii_letters + string.digits + string.punctuation
#     password = ''
#     for char in range(size):
#         rand_char =random.choice(all_chars)
#         password = password + rand_char
#     return password

# pass_len = int(input('How many charecters in your password?'))
# new_password = generate_password(pass_len)
# print('Your new pass: ', new_password)

#password with gmail:

import random
import string

first = input('Enter your first name: ')
last = input('enter your last name: ')
num = int(input('enter how long your password will be: '))
all_char = string.ascii_letters + string.punctuation + string.digits
email = first +'.'+ last + '@gmail.com'
password = ''
for i in range(num):
    rand_char = random.choice(all_char)
    password = password + rand_char
    
print('Your gmail id: '+ email)
print('your password: '+ password)