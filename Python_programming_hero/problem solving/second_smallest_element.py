# #second smallest element in the list
list = [45,34,24,64,623,0,1]
shorted_num = sorted(list, reverse=False)
second_smallest = shorted_num[1]
print(second_smallest)


#another solve:
list = [45,34,24,64,623,0,1]
new_list = min(list)
list.remove(new_list)
minimum = min(list)
print(minimum)


#another process:
list = [45,34,24,64,623,0,1]
smallest = list[0]
second_smallest = list[0]
for i in range(1, len(list)):
    if list[i] < smallest:
        second_smallest = smallest
        smallest = list[i]
    elif list[i] < second_smallest:
        second_smallest = list[i]
print(second_smallest)