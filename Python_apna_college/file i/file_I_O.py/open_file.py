"""Create a new fine 'practice.txt' using python. add the following data in it;
    Hi everyone
    we are learning File I/O
    using Java
    I like programming in Java"""
    
with open('practice.txt', 'w') as f:
    f.write('Hi everyone\nwe are we are learning File I/O\n')
    f.write('using Java\nI like programming in Java')