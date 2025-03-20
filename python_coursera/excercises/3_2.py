""" Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
You should use input to read a string and float() to convert the string to a number.
Do not worry about error checking the user input - assume the user types numbers properly."""


sh = input('Enter hours: ')
sr = input('Enter rate: ')
# ei try & except er maddhome cheak korbo j input gulo shonkhay dilo kina
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("error, please enter numeric input")
    quit()
print(fh, fr)
if fh>40:
    regular = fh * fr
    extra = (fh - 40)*(fr * 0.5)
    total = regular + extra
else:
    total = fh * fr
print("Pay:", total)