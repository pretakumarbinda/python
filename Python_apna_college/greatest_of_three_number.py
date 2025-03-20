# wAP to chrek the greatest of 3 numbers entered by the user
a = int(input('enter 1st num: '))
b = int(input('enter 2nd num: '))
c = int(input('enter 3rd num: '))

if(a>=b and a>=c):
    print('1st number is the greatest number', a)
elif(b>=c):
    print('2nd number is the greatest number', b)
else:
    print('3rd number is the greatest number', c)