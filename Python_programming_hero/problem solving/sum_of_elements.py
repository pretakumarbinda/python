# #print the sum of elements given in a list:

nums = [13, 89, 64, 34, 56, 24, 243]
def get_sum(nums):
    sum = 0
    for num in nums:
        sum = sum + num
    return sum
total = get_sum(nums)
print("The total of each elements: ", total)


# another method


nums = [13, 89, 64, 34, 56, 24, 243]
sum = 0
for num in nums:
    sum = sum + num
print("The total of each elements: ", sum)



#another method



nums = [13, 11, 16, 78, 31, 128]
total = sum(nums)
print(total)