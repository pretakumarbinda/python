# #find the greatest common divisor

# def compute_gcd(x,y):
#     smaller = min(x,y)
#     gcd = 1
#     for i in range(2, smaller+1):
#         if (x%i == 0 and y % i == 0):
#             gcd = i
#     return gcd
# num1 = int(input('enter 1st num:'))
# num2 = int(input('enter 2nd number:'))
# gcd = compute_gcd(num1, num2)
# print('GCD of ', num1, 'and', num2, 'is', gcd)


# #using recursive method:
# num1 = int(input('enter the 1st num: '))
# num2 = int(input('enter the 2nd num:'))
# if num1> num2:
#     max = num1
#     min = num2
# else:
#     max = num2
#     min = num1
# def gcd(max, min):
#     if min == 0:
#         return max
#     else:
#         return gcd(min, max%min)
# gcd1 = gcd(max, min)
# print(gcd1)


# #built in gcd
# import math
# a = int(input('enter 1st number: '))
# b = int(input('enter 2nd number: '))
# gcd = math.gcd(a,b)
# print(gcd)

#another solve
def gcd(num):
    factors = []
    for i in range(1, num+1):
        if num%i == 0:
            factors.append(i)
    factors = set(factors)
    return factors

num1 = int(input('enter 1st number: '))
num2 = int(input('enter 2nd number: '))
num1_factors = gcd(num1)
num2_factors = gcd(num2)

common_factors = num1_factors & num2_factors
common_factors = list(common_factors)
print('GCD of two numbers is: ', max(common_factors))
