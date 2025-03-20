from tkinter import *
root = Tk()
root.title("Courses")


python= Button(root, text="Python", width=8)
java = Button(root, text="Java", width=8)
cpp = Button(root, text="C++", width=8)
javascript = Button(root, text="JavaScript", width=8)

python.grid(row=0, column=0)
java.grid(row=0, column=1)
cpp.grid(row=1, column=0)
javascript.grid(row=1, column=1)


root.mainloop()