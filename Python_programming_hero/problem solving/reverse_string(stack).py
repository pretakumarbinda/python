# reverse a string by using stack
def reverse_stack(enter):
    # create an empty stack(list to use as a stack)
    stack = []
    #push all characters of string to stack
    for char in enter:
        stack.append(char)
        #pop all characters of string
        #and add it to the rev
    rev = ''
    while len(stack)>0:
        last = stack.pop()
        rev = rev + last
    return rev

usr_str = input('what is your string: ')
reverse = reverse_stack(usr_str)
print('Reversed is: ', reverse)