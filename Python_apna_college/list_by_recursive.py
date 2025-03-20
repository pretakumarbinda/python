# write a recursive function to print all elements in a list
def print_list(list, index = 0):
    if(index == len(list)):
        return
    print(list[index])
    print_list(list, index+1)

fruits = ['mango', 'lichi', 'apple', 'banana']
print_list(fruits)