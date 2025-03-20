# get input from user and detect if it is a number or not

rawstr = input('enter a number: ')
try:
    value = int(rawstr)
except:
    value = -1

if(value > 0):
    print("this is a number.")
else:
    print('this is not a number.')