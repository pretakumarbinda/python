#user will give strings, remove all duplicate characters from that string

# def remove_duplicate(your_str):
#     result = ''
#     for char in your_str:
#         if char not in result:
#             result += char
#     return result
# user_input = input("what is your string: ")
# no_duplicate = remove_duplicate(user_input)
# print('without duplicate: ', no_duplicate)

#without function:

input = input("enter your string: ")
result = ''
for char in input:
    if char not in result:
        result = result + char
print("without duplicate: ", result)