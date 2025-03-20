# # cheak if a number is armstrong number or not
# #কোন সংখ্যার অংকগুলোকে উক্ত সংখ্যায় উপস্থিত মোট অংকের মান দ্বারা পাওয়া েকরে যোগ করা হলে, 
# # প্রাপ্ত যোগফলের মান যদি মূল সংখ্যার সমান হয় তবে সংখ্যাটিকে আর্মস্ট্রং নাম্বার বলে।
# # 371 -->   3^3 + 7^3 + 1^3 = 27+343+1 = 371

# def cheak_armstrong(num):
#     order = len(str(num))
#     sum = 0
#     temp = num
#     while temp>0:
#         digit = temp%10
#         sum = sum + digit ** order
#         temp = temp // 10
#     return num == sum
# num = int(input('enter your num: '))
# if cheak_armstrong(num):
#     print(num, 'is an Armstrong number.')
# else:
#     print(num, 'is not an Armstrong number.')
    
#another solve
def num_slicing(n):
    I = []
    while n>0:
        I.append(n%10)
        n = n//10
    I.reverse()
    sum = 0
    li_len = len(I)
    for i in I:
        x = i ** li_len
        sum = sum + x
    sum2 = ''
    for a in I:
        sum2 = sum2 + str(a)
    if sum2 == str(sum):
        print(sum2, "is an armstrong number.")
    if sum2 != str(sum):
        print(sum2, "is not an armstrong number.")
    
n = int((input('enter integer number: ')))
print(num_slicing(n))