
# 1 line e if-else likha jay:
food = input("food: ")
eat = 'Yes' if food == 'cake' else "No"
print(eat)

#another way
food = input("food: ")
print("sweet") if food == 'cake' or food == 'jalebi' else print("not sweet")


# clever if
age = int(input("age "))
vote = ("yes", 'no')[age<18]
print(vote)