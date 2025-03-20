# reverse a string by using recursive function
def reverse_recur(str):
    if len(str) == 0:
        return str
    else:
        return reverse_recur(str[1:]) + str[0]

str = input('enter your string: ')
rev_str = reverse_recur(str)
print('reverse: ', rev_str)


#another smart way:

txt = 'welcome'
print(txt[::-1])
