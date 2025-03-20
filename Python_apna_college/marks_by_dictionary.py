"""Wap to enter marks of 3 subjects from the user and store them in a dictionary.
Start with an empty dictionary & add one by one. Use subject name as key & marks as value"""
marks = {}
phy = input("enter phy: ")
chem = input("enter math: ")
math = input("enter chem: ")
marks.update({"phy":phy,"chem": chem, "math": math})
print(marks)