#wap to cheak if a list contains a palindrome of elements.
list = [1,2,3,4,3,2,1]

list2 = list.copy()
list2.reverse()
if(list == list2):
    print("the list is palindromic")
else:
    print("the list is not palindromic")