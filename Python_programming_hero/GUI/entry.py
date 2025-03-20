from tkinter import *
root = Tk()

lbl = Label(root, text="Name")
data=Entry(root)
lbl.grid(row=0, column=0)
data.grid(row=0, column=1)

root.mainloop()