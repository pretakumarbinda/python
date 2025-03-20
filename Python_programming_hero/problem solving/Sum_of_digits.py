# #for a given number. find the sum of every digit.
user_input = int(input("enter the number: "))
def get_sum_of_digits(num):
    sum = 0
    while num>0:
        last_digit = num % 10
        sum = sum + last_digit
        num = num // 10
    return sum
total = get_sum_of_digits(user_input)
print('the total sum of digits is: ', total)


# #another solve
num = input("enter a number: ")
sum = 0
for char in num:
    sum = sum + int(char)
print(sum)


#another solve
num_str = input("enter a number: ")
num_chars = list(num_str) #when you convert a string yo list, it will become a  list of each character. thus 1234 becomes '1', '2','3','4'
sum = 0
for i in num_chars:
    sum = sum + int(i)
print(sum)
