#wap to ask the user to enter names of their 3 favourite movies & store them in a list.
list = []
first = input("enter your first movie: ")
second = input("enter your second movie: ")
third = input("enter your third movie: ")
list.append(first)
list.append(second)
list.append(third)
print(list)


#another way:
list = []
mov = input("enter your first movie: ")
list.append(mov)
mov = input("enter your second movie: ")
list.append(mov)
mov = input("enter your third movie: ")
list.append(mov)
print(list)


#another way:
list = []
list.append(input("enter your first movie: "))
list.append(input("enter your second movie: "))
list.append(input("enter your third movie: "))
print(list)