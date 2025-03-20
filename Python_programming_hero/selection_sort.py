# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_idx = i
#         for j in range(i+1, len(arr)):
#             if arr[min_idx] > arr[j]:
#                 min_idx = j
#         temp = arr[i]
#         arr[i] = arr[min_idx]
#         arr[min_idx] = temp
#     return arr

# nums = [64, 25, 12, 22, 11]
# sorted_num = selection_sort(nums)
# print(sorted_num)



#another way:
def sort(nums):
    for i in range(len(nums)):
        minpos = i
        for j in range(i, len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
        
nums = [5, 3, 8, 6, 7, 2]
sort(nums)
print(nums)