    #from a list, find the 2nd largest number of the elements

list = [3, 5, 7, 9, 12]
maximum =  max(list)
list.remove(maximum)
second_maximum = max(list)
print(second_maximum)

         #another process
nums = [11,44,83,29,25,76,88]
largest = nums[0]
second_largest = nums[0]          #Initialize largest and second_largest with the first element of the list (nums[0]).
for i in range(1, len(nums)):     #Iterate through the list starting from the second element (nums[1:]).
    if nums[i] > largest:
        second_largest = largest    #If the current element is greater than the current largest, update both largest and second_largest.
        largest = nums[i]
    elif nums[i] > second_largest:
        second_largest = nums[i]        #If the current element is greater than the current second_largest but not greater than largest, update only second_largest.
print("Second largest number is : ", second_largest)



           #another process
def get_second_largest(nums):
    if len(nums) < 2:
        return
    sorted_nums = sorted(nums, reverse = True)
    second_largest = sorted_nums[1]
    return second_largest
my_nums = [44,11,83,29,25,76,88]
second_largest = get_second_largest(my_nums)
print("Second highest number is: ", second_largest)


