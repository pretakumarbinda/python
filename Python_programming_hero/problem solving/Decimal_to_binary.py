
    
def dec_to_binary(n):
    bits=[]
    while n>0:
        bits.append(n%2)
        n = n // 2
    bits.reverse()
    binary = ''
    for bit in bits:
        binary = binary+str(bit)
    return binary 
num = int(input('your decimal number: '))
binary = dec_to_binary(num)
print("your binary is : ", binary)