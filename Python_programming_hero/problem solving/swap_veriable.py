a = 5
b = 3
print("a, b", a, b )
temp = a
a = b
b = temp
print("a, b", a, b )

#another method using shortcut

a = 5
b = 3
print("a, b", a, b )
a, b = b, a #swaping these two
print("a, b", a, b)

#another hard process:  **********************

a = 5
b = 3
print("a, b", a, b )
a = a + b
b = a - b
a = a - b
print("a, b", a, b)