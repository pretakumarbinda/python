mark = int(input("enter the marks: "))
if(mark>=90):
    grade = 'A'
elif(mark>=80 and mark<=89):
    grade = 'B'
elif(mark>=70 and mark<=79):
    grade = 'C'
elif(mark<70):
    grade = 'D'
print(grade)