# reverse a string using function(without use of list)
def reverse_string(enter):
    reverse = ''
    for char in enter:
        reverse = char + reverse
    return reverse

enter = input('Enter your string: ')
result = reverse_string(enter)
print(result)