# # find the sum of 1^3 + 2^3 +.....+ n^3

def cube_sum(n):
    sum = 0
    for n in range(n + 1):
        sum = sum + n ** 3
    return sum
usr_in = int(input('enter a number: '))
result = cube_sum(usr_in)
print('your sum of cubes are: ', result)


#another solve
# formula = (n*(n+1)/2)^2

n = int(input('enter a number: '))
sum = (n*(n+1)/2)**2
print('Your sum of cubes are: ', int(sum))