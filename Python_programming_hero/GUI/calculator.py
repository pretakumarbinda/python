from tkinter import *
import tkinter.font as font
root=Tk()

def add():
    x = int(enterOne.get())
    y = int(enterTwo.get())
    result["text"] = x+y
    
def sub():
    x = int(enterOne.get())
    y = int(enterTwo.get())
    result["text"] = x-y

def mul():
    x = int(enterOne.get())
    y = int(enterTwo.get())
    result["text"] = x*y

def div():
    x = int(enterOne.get())
    y = int(enterTwo.get())
    result["text"] = x/y

numOne = Label(root, text="Enter First Number: ", font = ("Serif", 12))
enterOne = Entry(root)
numTwo = Label(root, text="Enter Second Number: ", font = ("Serif", 12))
enterTwo = Entry(root)

add = Button(root, text="Add", width=10, command=add)
sub = Button(root, text="Sub", width=10, command=sub)
div = Button(root, text="div", width=10, command=div)
mul = Button(root, text="mul", width=10, command=mul)

result = Label(root)

numOne.grid(row=0, column=0)
enterOne.grid(row=0, column=1)
numTwo.grid(row=1, column=0)
enterTwo.grid(row=1, column=1)

add.grid(row=2, column=0)
sub.grid(row=2, column=1)
div.grid(row=3, column=0)
mul.grid(row=3, column=1)
result.grid(row=4, column=0)



root=mainloop()