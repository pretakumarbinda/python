print('enter your marks:')
sub1 = int(input("First subject: "))
sub2 = int(input("second subject: "))
sub3 = int(input("third subject: "))
sub4 = int(input("forth subject: "))
sub5= int(input("fifth subject: "))
avg = (sub1 + sub2 + sub3 + sub4 + sub5)/5
if avg >= 90:
    print('Grade: A')
elif avg >= 80:
    print('grade: B')
