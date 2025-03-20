my_str = input('String to cheak: ')
rev_str = my_str[::-1] #shortcut to make reverse
if my_str == rev_str:
    print('It is palindrome')
else:
    print('It is not palindrome')