#দুইটা সংখ্যার ভাগফল দশমিক ছাড়া বের কর

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
result = (num1//num2) # here // is used to get the results without remainder
print(result)


#another way:

import math
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
calculation = num1/num2
result = math.floor(calculation) #floor method converts the number to integer(without decimal part)
print(result)