"""Write a function to find in which line of the file does the word
'learning' occur first. print -1 if word not found"""
def cheak_for_line():
     word = 'learning'
     data = True
     line_no = 1
     with open('practice.txt', 'r') as f:
        while data: #jotokkkhn ei datar moddhe kono value ache totokkhn run hbe
            data = f.readline()
            if (word in data):
                print(line_no)
                return
            line_no += 1
        return print('-1')
cheak_for_line()
    