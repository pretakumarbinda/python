#find the area of a triangle when 3 ta bahu dewa ase
import math

a = float(input('enter 1st side : '))
b = float(input('enter 2nd side : '))
c = float(input('enter 3rd side : '))

s = (a+b+c)/2

area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print('area =', area)