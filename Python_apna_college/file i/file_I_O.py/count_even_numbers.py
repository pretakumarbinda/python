#From a file containing numbers separated by comma, print the count of even numbers # near at (7 hr 50 min)
count = 0
with open("text.txt", "r") as f:
    data = f.read()
    # print(data)
    #spliting numbers(separated by comma) without using split function:
    """
    num = ''
    for i in range(len(data)):
        if(data[i] == ','):
            print(int(num))
            num = ''
        else:
            num += data[i]
    """
    
    #spliting numbers using split function:
    nums = data.split(",")
    
    #now cheak if even:
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
print(count)
