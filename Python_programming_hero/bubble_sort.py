# def bubbleSort(list):
#     n = len(list)
#     for i in range(n):
#         for j in range(n-1):
#             if list[j] > list[j+1]:
#                 temp = list[j]
#                 list[j] = list[j+1]
#                 list[j+1] = temp
#     return list
# nums = [64, 34, 25, 12, 22, 11, 90]
# sorted_num = bubbleSort(nums)
# print(sorted_num) 




#another solve
# def bubble(arr1):
#     n = len(arr1)
#     for i in range(n):
#         swapped = False
#         for j in range(n-i-1):
#             if arr1[j] > arr1[j+1]:
#                 arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
#                 swapped = True
            
# arr1 = [ 15, 18, 16, 33, 22, 55]
# bubble(arr1)
# print(arr1)



#another solve
def sort(nums):
    for i in range(len(nums)-1, 0, -1):  #will run from 5 to 0
        for j in range(i):  #will run from 0 to i. As no need to cheak the last value
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
nums = [5, 3, 8, 6, 7, 2]
sort(nums)
print(nums)