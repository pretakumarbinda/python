#single line if or ternary operator
food = input("food: ")
eat = 'yes' if food == 'cake' else 'no'
print(eat)

#another statement

food = input("food: ")
print("sweet") if food == 'cake' or food == 'jalebi' else print('not sweet')
