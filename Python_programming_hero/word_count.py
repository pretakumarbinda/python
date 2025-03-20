text = 'Love to watching Movie'
count = 0
for char in text:
    if char == ' ':
        count = count + 1

count = count + 1  #this one is for the last word counting
print(count)