#decimal to binary function using recursive function
def dec_to_binary(n):
    print(n%2, end = '')
    if n>1:
        dec_to_binary(n//2)
    
    
num = int(input("your decimal number: "))
dec_to_binary(num)



