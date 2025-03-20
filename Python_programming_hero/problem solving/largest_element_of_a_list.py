nums = [121, 34, 54, 23, 78]
largest = max(nums)
print("The largest num is: ", largest)

# another method: 
nums = [121, 34, 54, 23, 78]
max = nums[0]
for num in nums:
    if num > max:
        max = num

print("The largest number is: ", max)