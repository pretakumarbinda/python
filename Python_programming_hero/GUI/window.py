
from tkinter import *       #imports all from tkinter
root = Tk()     #Tk toolkit is a thin object-oriented layer(helps to create GUI in python). it is creating the root window

root.title("Programming Hero")
# root.geometry("500x200")        #fixes the window size in pixel

course = Label(root, text="Course - Programming", bg="red", fg="blue")  #will display the text in root window, bg= background, fg=foreground
course.pack()    #it is a geometric managers

enroll = Button(root, text='Enroll Now', fg="blue", bg="yellow")        #to add button
enroll.pack()

root.mainloop()     #starts the execution of our program into the main thread