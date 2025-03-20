astr = 'Bob'
try:
    print('hello') # this will run *******
    istr = int(astr) # this will not run
    print('there') # this will not run
except:
    istr = -1 # this will run *******
print('done', istr)

#that's how try & except works