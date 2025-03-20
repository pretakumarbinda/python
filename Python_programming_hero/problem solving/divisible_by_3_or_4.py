# #find the numbers between 0 to num divisible by both 3 and 5

def divisible_by_3and5(num):
    result = []
    for i in range(num):
        if i%3 == 0 and i%5 == 0:
            result.append(i)
    return result
num = int(input('Enter your number: '))
result = divisible_by_3and5(num)
print(result)


# #easy solution without function

num = int(input('Enter the number: '))
list = []
for i in range(num):
    if i%3 == 0 and i%5 == 0:
        list.append(i)
print(list)

#another solve with while loop

num = int(input("Enter the numbers: "))
list = []
i = 1
while i<=num:
    if i%3==0 and i%5==0:
        list.append(i)
    i = i+1
print(list)


#another solve with while loop

user_numb = int(input("Enter your number: "))
while user_numb>0:
    if user_numb%5==0 and user_numb%3==0:
        print(user_numb)
    user_numb -= 1
    
    
