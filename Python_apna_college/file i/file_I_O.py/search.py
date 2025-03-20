"""search if the word 'learning' exists in the file or not"""
def cheak_for_word():
    word = 'learning'
    with open('practice.txt', 'r') as f:
        data = f.read()
        if(data.find(word) != -1):
            print('Found')
        else:
            print('Not found')
            
cheak_for_word()