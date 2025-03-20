astr = 'Hello Bob'
try:
    istr = int(astr) #python will firstly try this and if it fails then goes to the except
except:
    istr = -1
print('First', istr)

        #another
astr = '123'
try:
    astr = int(astr)
except:
    astr = -1
print('second', astr)